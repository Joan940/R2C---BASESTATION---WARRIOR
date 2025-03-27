import modules.varGlobals as varGlobals
import time
import modules.dataRobot as dataRobot
from modules.comBasestation import send_robot


def stop():
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

    varGlobals.stop = True
    varGlobals.start = False
    varGlobals.dropBall = False
    varGlobals.park = False
    varGlobals.endPart = False
    
    prestart = False

    if varGlobals.stop:
        print("ini stop")
        data=bytearray(3)
        for i in range (2):
            for i in range (3):
                data[0]= int(i)
                data[1]= 252
                data[2]=123
                print(i)
                send_robot(data)
                time.sleep(0.15)
            time.sleep(0.15)
        while varGlobals.stop:
            for i in range (3):
                if not varGlobals.stop:
                    break
                else:
                    print("Robot Standby")
                    data[0]= int(i)
                    data[1]= 1
                    data[2]=1
                    print(i)
                    send_robot(data)
                    time.sleep(0.15)
            time.sleep(0.15)
