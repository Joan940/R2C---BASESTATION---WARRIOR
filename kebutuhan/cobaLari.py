import modules.varGlobals as varGlobals
import time
# from lib.pathFinding import calculateRadius
from lib.playGame import playGame 
import modules.dataRobot as dataRobot
from lib.skils import lariBiasa,lihatBolaGeser,tendangKencang,pindahAwalKiper,ballPredictKiper,sendGrid ,tendangKencang,kejarBolaPelan, umpanTeman, lihatBolaDiam, kejarBolaCepat, changePos, tendangGiring

def reset():
    varGlobals.runLariTeam = False
    varGlobals.runLariMusuh = False

    varGlobals.runKickoffTeam = False
    varGlobals.runKickoffMusuh = False

    varGlobals.runFreeKickTeam = False
    varGlobals.runFreeKickMusuh = False

    varGlobals.runGoalKickTeam = False
    varGlobals.runGoalKickMusuh = False

    varGlobals.runThrowInTeam = False
    varGlobals.runThrowInMusuh = False

    varGlobals.runCornerTeam = False
    varGlobals.runCornerMusuh = False

    varGlobals.runPenaltyTeam = False
    varGlobals.runPenaltyMusuh = False

    varGlobals.stop = False
    varGlobals.start = False
    varGlobals.dropBall = False
    varGlobals.park = False
    varGlobals.endPart = False

def setPosition(setBall_x, setBall_y):
    position = {}
    if (setBall_x, setBall_y) in [(500, 234), (500, 414), (500, 594)]:
        position = {
            1: {'x': 14 * 50, 'y': 10 * 50},
            2: {'x': 12 * 50, 'y': 11 * 50}
        }
    elif (setBall_x, setBall_y) in [(860, 234), (860, 594)]:
        position = {
            1: {'x': 5 * 50, 'y': 10 * 50},
            2: {'x': 10 * 50, 'y': 9 * 50}
        }
    elif (setBall_x, setBall_y) in [(1220, 234), (1220, 414), (1220, 594)]:
        position = {
            1: {'x': 4 * 50, 'y': 18 * 50},
            2: {'x': 5 * 50, 'y': 10 * 50}
        }
    return position

def pergerakan(position):
    for robot_id, pos in position.items():
        changePos(robot_id, pos['x'], pos['y'], 0)

def tungguPosisi(position):
    waktuMulai = time.time()
    while time.time() - waktuMulai < 5:
        diPosisi = True
        for robot_id, pos in position.items():
            if dataRobot.xpos[robot_id]//50 != pos['x']//50 or dataRobot.ypos[robot_id]//50 != pos['y']//50:
                diPosisi = False
                tungguPosisi(position)
                time.sleep(0.015)
                break
        if diPosisi:
            print("Sudah Di Posisi")
            return

def strategi(position):
    if varGlobals.striker:
        lariBiasa(2)
    elif varGlobals.back:
        lariBiasa(1)

def lariHandler(isTeamLari):
    reset()
    varGlobals.runLariTeam = isTeamLari
    varGlobals.runLariMusuh = not isTeamLari
    
    while (varGlobals.runLariTeam or varGlobals.runLariMusuh) and not varGlobals.stop:
        print("Mulai Lari")
        pindahAwalKiper()
        ballPredictKiper()

        positions = setPosition(varGlobals.setBall_x, varGlobals.setBall_y)
        pergerakan(positions)
        tungguPosisi(positions)

        if varGlobals.start and not varGlobals.stop:
            strategi(positions)
        time.sleep(0.25)

def lariTeam():
    lariHandler(True)

def lariMusuh():
    lariHandler(False)
