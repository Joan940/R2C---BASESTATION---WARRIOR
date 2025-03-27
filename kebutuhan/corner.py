import modules.varGlobals as varGlobals
import time
# from lib.pathFinding import calculateRadius
from lib.playGame import playGame 
import modules.dataRobot as dataRobot
from lib.skils import lihatBolaGeser,tendangKencang, pindahAwalKiper,ballPredictKiper,sendGrid ,tendangKencang,kejarBolaPelan, umpanTeman, lihatBolaDiam, kejarBolaCepat, changePos, tendangGiring
import modules.varGlobals as varGlobals

corner1=False
corner2=False

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

def cornerTeam():
    reset()
    varGlobals.runCornerTeam = True
    prestart = False

    while varGlobals.runCornerTeam and not varGlobals.stop:
        print("Ini Corner Team")
        global corner1, corner2

        if not prestart:
            pindahAwalKiper()
            ballPredictKiper()
            idBack, idStriker = 1, 2
            angleBack = 0
            angleStriker = 0

            # Corner kanan atas
            if varGlobals.setBall_x == 1400 and varGlobals.setBall_y == 54:
                xBack, yBack = 3 * 50, 25 * 50
                xBack2, yBack2 = 0 * 50, 25 * 50
                xStriker, yStriker = 3 * 50, 19 * 50
                corner1 = True
                corner2 = False

            # Corner kanan bawah
            elif varGlobals.setBall_x == 1400 and varGlobals.setBall_y == 774:
                xBack, yBack = 11 * 50, 19 * 50
                xStriker, yStriker = 14 * 50, 12 * 50
                xStriker2, yStriker2 = 14 * 50, 24 * 50
                corner1 = False
                corner2 = True

            if corner1:
                waitPosition(idBack, xBack, yBack, angleBack, idStriker, xStriker, yStriker, angleStriker)
                waitPosition(idBack, xBack2, yBack2, angleBack)
            if corner2:
                waitPosition(idBack, xBack, yBack, angleBack, idStriker, xStriker, yStriker, angleStriker)
                waitPosition(idStriker, xStriker2, yStriker2, angleStriker)

            time.sleep(0.5)
            prestart = True
            print("posisi selesai")

        elif prestart and varGlobals.start and not varGlobals.stop:
            CornerPlay(idBack, idStriker)

        time.sleep(0.25)

def cornerMusuh():
    reset()
    varGlobals.runCornerMusuh = True
    prestart = False

    while varGlobals.runCornerMusuh:
        print("ini Corner Musuh")
        idBack, idStriker = 1, 2
        xBack, yBack, angleBack = 0, 0, 0
        xStriker, yStriker, angleStriker = 0, 0, 0

        if not prestart:
            pindahAwalKiper()
            ballPredictKiper()

            # Corner kiri atas
            if varGlobals.setBall_x == 320 and varGlobals.setBall_y == 54:
                xBack, yBack = 5 * 50, 6 * 50
                xStriker, yStriker = 12 * 50, 7 * 50
            
            # Corner kiri bawah
            elif varGlobals.setBall_x == 320 and varGlobals.setBall_y == 774:
                xBack, yBack = 9 * 50, 7 * 50
                xStriker, yStriker = 12 * 50, 6 * 50

            waitPosition(idBack, xBack, yBack, angleBack, idStriker, xStriker, yStriker, angleStriker)
            time.sleep(0.5)
            prestart = True
            print("posisi selesai")

        elif prestart and varGlobals.start and not varGlobals.stop:
            CornerPlay(idBack, idStriker)

        time.sleep(0.25)

def waitPosition(id1, x1, y1, angle1, id2=None, x2=None, y2=None, angle2=None):
    i = 0
    while not (
        (dataRobot.xpos[id1] // 50 == x1 // 50 and dataRobot.ypos[id1] // 50 == y1 // 50) and
        (id2 is None or (dataRobot.xpos[id2] // 50 == x2 // 50 and dataRobot.ypos[id2] // 50 == y2 // 50)) and
        not varGlobals.stop
    ):
        if varGlobals.stop:
            break
        elif i >= 20:
            print("sudah 5 detik")
            break
        else:
            i += 1
            print("wait position")
            pindahAwalKiper()
            changePos(id1, x1, y1, angle1)
            if id2 is not None:
                changePos(id2, x2, y2, angle2)

def CornerPlay(idBack, idStriker):
    ballPredictKiper()
    while not varGlobals.stop:
        if varGlobals.stop == True:
            break
        elif varGlobals.ball_x < 860 and dataRobot.catch_ball[idStriker] == 0:
            kejarBolaCepat(idStriker)
            lihatBolaDiam(idBack)
            umpanTeman(idStriker)
            kejarBolaCepat(idBack)
            tendangKencang(idBack)
        elif varGlobals.ball_x > 860:
            lihatBolaGeser(idStriker)
            lihatBolaDiam(idBack)
            kejarBolaCepat(idBack)
            tendangKencang(idBack)
        elif varGlobals.ball_x < 860 and dataRobot.catch_ball[idStriker] == 1:
            lihatBolaDiam(idBack)
            umpanTeman(idStriker)
            kejarBolaCepat(idBack)
            tendangKencang(idBack)