import modules.varGlobals as varGlobals
import time
# from lib.pathFinding import calculateRadius
from lib.playGame import playGame 
import modules.dataRobot as dataRobot
from lib.skils import lihatBolaGeser,tendangKencang, pindahAwalKiper,ballPredictKiper,sendGrid ,tendangKencang,kejarBolaPelan, umpanTeman, lihatBolaDiam, kejarBolaCepat, changePos, tendangGiring
import modules.varGlobals as varGlobals

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

def setPosition():
    # #Back
    # idBack = 1
    # xBack = 425
    # yBack = 10 * 50
    # angleBack = 0

    # #Striker
    # idStriker = 2
    # xStriker = 12 * 50
    # yStriker = 11 * 50
    # angleStriker = 0
    position = {
        1: {'x': 425, 'y': 10 * 50},
        2: {'x': 12 * 50, 'y': 11 * 50}
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
        ballPredictKiper()
        lihatBolaDiam(2)
        lihatBolaDiam(1)
        playGame()

def penaltyHandler(isTeamPenalty):
    reset()
    varGlobals.runPenaltyTeam = isTeamPenalty
    varGlobals.runPenaltyMusuh = not isTeamPenalty
    while (varGlobals.runPenaltyTeam or varGlobals.runPenaltyMusuh) and not varGlobals.stop:
        print("Mulai Penalty")
        pindahAwalKiper()
        ballPredictKiper()

        positions = setPosition()
        pergerakan(positions)
        tungguPosisi(positions)

        if varGlobals.runPenaltyMusuh:
            positions = {
                1: {'x': 5 * 50, 'y': 10 * 50},  # Posisi baru untuk robot 1 (Back)
                2: {'x': 12 * 50, 'y': 10 * 50}   # Posisi baru untuk robot 2 (Striker)]
            }
            pergerakan(positions)
            tungguPosisi(positions)

        if varGlobals.start and not varGlobals.stop:
            strategy(positions)
        time.sleep(0.25)

def penaltyTeam():
    penaltyHandler(True)

def penaltyMusuh():
    penaltyHandler(False)