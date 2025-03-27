import modules.varGlobals as varGlobals
import time
import threading
from library.playGame import playGame 
import modules.dataRobot as dataRobot
from modules.comBasestation import send_robot
from modules.dataRobot import catch_ball
from library.skillBaru import (
    powerShoot,
    pindahAwalKiper,
    ballPredictKiper,
    kejarBolaPelan,
    lihatBolaDiam,
    kejarBolaCepat,
    ubahPosisi,
    lihatBolaGeser,
    dribbling,
    passing,
)

def reset():
    varGlobals.runCornerKanan = False
    varGlobals.runCornerKiri = False

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

def cornerKanan():
    reset()
    varGlobals.runCornerKanan = True

    while (varGlobals.runCornerKanan and varGlobals.runCornerKiri) and not varGlobals.stop:
        print("Ini Corner Kanan")

        if not prestart:
            pindahAwalKiper()
            ballPredictKiper()
            idBack, idStriker, idKiper = 1, 2, 0
            angleBack = 0
            angleStriker = 0

            # Corner kanan bawah
            if varGlobals.setBall_x == 1400 and varGlobals.setBall_y == 774:
                xBack, yBack = 0, 0
                xStriker, yStriker = 0, 0

            time.sleep(0.5)
            prestart = True
            print("posisi selesai")

        elif prestart and varGlobals.start and not varGlobals.stop:
            CornerPlayKanan(idBack, idStriker, idKiper)

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
            ubahPosisi(id1, x1, y1, angle1)
            if id2 is not None:
                ubahPosisi(id2, x2, y2, angle2)

def CornerPlayKanan(idBack, idStriker, idKiper):
    ballPredictKiper()
    kejarBolaCepat(1)
    lihatBolaDiam(2)

    retry_count = 0
    if varGlobals.striker and varGlobals.back:
        while dataRobot.catch_ball[1] == 0 and retry_count <= 1:
            retry_count += 1
            reset()

        passing(1)
        
        target_x_back = dataRobot.xpos[1] + 0.5 * 100
        target_x_striker = dataRobot.xpos[2] + 0.5 * 100
        if dataRobot.catch_ball[2] > 0:
            while abs(dataRobot.xpos[2] - target_x_striker) >= 0.5 * 100:
                lihatBolaDiam(1)
                ubahPosisi(2, target_x_back, 0, 0)

        passing(2)
        
        if dataRobot.catch_ball[1] > 0:
            passing(1)

        if dataRobot.catch_ball[2] > 0:
            while abs(dataRobot.xpos[2] - target_x_striker) >= 0.5 * 100:
                powerShoot(2)
    
    elif not varGlobals.striker and varGlobals.kiper and not varGlobals.back:
        kejarBolaPelan(0)
        dribbling(0)
        powerShoot(0)