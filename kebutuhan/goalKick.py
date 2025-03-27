import modules.varGlobals as varGlobals
import time
# from lib.pathFinding import calculateRadius
from lib.playGame import playGame 
import modules.dataRobot as dataRobot
from lib.skils import lihatBolaGeser,tendangKencang, pindahAwalKiper,ballPredictKiper,sendGrid ,tendangKencang,kejarBolaPelan, umpanTeman, lihatBolaDiam, kejarBolaCepat, changePos, tendangGiring
import modules.varGlobals as varGlobals

titik1=False
titik3=False
titik6=False
titik8=False

def reset():
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
    if (setBall_x, setBall_y) in [(500, 234), (500, 594)]:
        position = {
            (500, 234): {
                1: {'x': 3 * 50, 'y': 1 * 50},
                2: {'x': 5 * 50, 'y': 7 * 50}
            },
            (500, 594): {
                1: {'x': 5 * 50, 'y': 8 * 50},
                2: {'x': 13 * 50, 'y': 1 * 50}
            }
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
        
def strategy(position):
    if varGlobals.striker and varGlobals.back:
        if titik1:
            while not varGlobals.stop:
                if varGlobals.stop==True:
                    break
                else:
                    if varGlobals.back:
                        ballPredictKiper()
                        lihatBolaDiam(1)
                        kejarBolaCepat(1)
                        tendangGiring(1)
                        kejarBolaCepat(1)
                        tendangKencang(1)
                    elif varGlobals.striker and not varGlobals.back:
                        ballPredictKiper()
                        lihatBolaDiam(2)
                        kejarBolaPelan(2)
                        tendangGiring(2)
                        kejarBolaCepat(2)
                        tendangKencang(2)
        elif titik3:
            while not varGlobals.stop:
                if varGlobals.stop==True:
                    break
                else:
                    if varGlobals.striker:
                        ballPredictKiper()
                        lihatBolaDiam(2)
                        kejarBolaPelan(2)
                        tendangGiring(2)
                        kejarBolaCepat(2)
                        tendangKencang(2)
                    elif varGlobals.back and not varGlobals.striker:
                        ballPredictKiper()
                        lihatBolaDiam(1)
                        kejarBolaCepat(1)
                        tendangGiring(1)
                        kejarBolaCepat(1)
                        tendangKencang(1)

def goalKickHandler(isTeamGoalKick):
    reset()
    varGlobals.runGoalKickTeam = isTeamGoalKick
    varGlobals.runGoalKickMusuh = not isTeamGoalKick
    while (varGlobals.runGoalKickTeam or varGlobals.runGoalKickMusuh) and not varGlobals.stop:
        print("Mulai Goal Kick")
        pindahAwalKiper()
        ballPredictKiper()

        positions = setPosition(varGlobals.setBall_x, varGlobals.setBall_y)
        
        if varGlobals.runGoalKickTeam:
            pergerakan(positions)
            tungguPosisi(positions)
            strategy(positions)

        if varGlobals.runGoalKickMusuh:
            if (positions) in [(1220, 234), (1220, 594)]:
                position = {
                    (1220, 234): {
                        1: {'x': 3 * 50, 'y': 1 * 50},
                        2: {'x': 5 * 50, 'y': 7 * 50}
                    },
                    (1220, 594): {
                        1: {'x': 5 * 50, 'y': 8 * 50},
                        2: {'x': 13 * 50, 'y': 1 * 50}
                    }
                }
            pergerakan(position)
            tungguPosisi(position)
            strategy(position)

        time.sleep(0.25)

def goalKickTeam():
    goalKickHandler(True)

def goalKickMusuh():
    goalKickHandler(False)