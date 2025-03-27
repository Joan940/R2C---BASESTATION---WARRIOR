import modules.varGlobals as varGlobals
import time
import modules.dataRobot as dataRobot

def endPart():
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
    varGlobals.endPart = True
    
    prestart = False

    while varGlobals.endPart:
        print("ini end part")
        if not prestart:
            for i in range(5):
                print("send prestart end part")
            prestart=True
            while dataRobot.xpos[2]!=400:
                print("cek")
            print("posisi selesai")
        time.sleep(0.50)