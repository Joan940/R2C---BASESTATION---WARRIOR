import modules.varGlobals as varGlobals
import time
import modules.dataRobot as dataRobot
from lib.skils import lihatBolaGeser,umpanTeman, lihatBolaDiam,tendangKencang,tendangGiring,sendGrid, pindahAwalKiper,ballPredictKiper, kejarBolaCepat

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
    idBack = 1
    xBack = int(varGlobals.CONFIG_BACK_GRID_X)
    yBack = int(varGlobals.CONFIG_BACK_GRID_Y)

    idStriker = 2
    xStriker = int(varGlobals.CONFIG_STRIKER_GRID_X)
    yStriker = int(varGlobals.CONFIG_STRIKER_GRID_Y)

    if varGlobals.striker and varGlobals.back:
        i = 0
        while not (dataRobot.xpos[2] // 50 == xStriker and 
                    dataRobot.ypos[2] // 50 == yStriker and
                    dataRobot.xpos[1] // 50 == xBack and 
                    dataRobot.ypos[1] // 50 == yBack and not varGlobals.stop
                    ):
            if varGlobals.stop or i >= 20:
                break
            
            i += 1
            print("Tunggu Posisi")
            pindahAwalKiper()
            sendGrid()
    
    elif varGlobals.striker and not varGlobals.back:
        i = 0
        while not (dataRobot.xpos[2] // 50 == xStriker and 
                    dataRobot.ypos[2] // 50 == yStriker and not varGlobals.stop
                    ):
            if varGlobals.stop or i >= 20:
                break
            
            i += 1
            print("Tunggu Posisi")
            pindahAwalKiper()
            sendGrid()

    elif not varGlobals.striker and varGlobals.back:
        i = 0
        while not (dataRobot.xpos[2] // 50 == xBack and 
                    dataRobot.ypos[2] // 50 == yBack and not varGlobals.stop
                    ):
            if varGlobals.stop or i >= 20:
                break
            
            i += 1
            print("Tunggu Posisi")
            pindahAwalKiper()
            sendGrid()
        print("Posisi selesai")
        time.sleep(0.5)

def strategy(idBack, idStriker):
    ballPredictKiper()

    if varGlobals.striker and varGlobals.back:
        lihatBolaDiam(idBack)
        kejarBolaCepat(idBack)
        tendangGiring(idBack)
        kejarBolaCepat(idBack)
        tendangKencang(idBack)

        while not varGlobals.stop:
            if varGlobals.ball_x < 860 and dataRobot.catch_ball[2] == 0:
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
            elif varGlobals.ball_x < 860 and dataRobot.catch_ball[2] == 1:
                lihatBolaDiam(idBack)
                umpanTeman(idStriker)
                kejarBolaCepat(idBack)
                tendangKencang(idBack)

    elif varGlobals.striker and not varGlobals.back:
        while not varGlobals.stop:
            kejarBolaCepat(idStriker)
            tendangGiring(idStriker)
            kejarBolaCepat(idStriker)
            tendangKencang(idStriker)
            print("Selesai")

    elif not varGlobals.striker and varGlobals.back:
        while not varGlobals.stop:
            kejarBolaCepat(idBack)
            tendangGiring(idBack)
            kejarBolaCepat(idBack)
            tendangKencang(idBack)
            print("Selesai")

def throwInTeam():
    reset()
    varGlobals.runThrowInTeam = True
    prestart = False

    while varGlobals.runThrowInTeam and not varGlobals.stop:
        print("Throw In Team")
        if not prestart:
            print("ThrowInTeam")
            setPosition()
            prestart = True
        elif prestart and varGlobals.start and not varGlobals.stop:
            strategy(1, 2)
        time.sleep(0.5)

def throwInMusuh():
    reset()
    varGlobals.runThrowInMusuh = True
    prestart = False

    while varGlobals.runThrowInMusuh and not varGlobals.stop:
        print("Throw In Musuh")
        if not prestart:
            print("ThrowInMusuh")
            setPosition()
            prestart = True
        elif prestart and varGlobals.start and not varGlobals.stop:
            strategy(1, 2)
        time.sleep(0.5)