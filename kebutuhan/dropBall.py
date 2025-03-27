import modules.varGlobals as varGlobals
import time
import modules.dataRobot as dataRobot
from lib.skils import lihatBolaGeser,umpanTeman, lihatBolaDiam,tendangKencang,tendangGiring,sendGrid,pindahAwalKiper,ballPredictKiper,kejarBolaCepat,changePos

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
    if(setBall_x, setBall_y) in [(860, 234), (860, 594)]:
        position = {
            (860, 234): {
                1: {'x': 2 * 50, 'y': 16 * 50},
                2: {'x': 6 * 50, 'y': 9 * 50}
            },
            (860, 594): {
                1: {'x': 6 * 50, 'y': 15 * 50},
                2: {'x': 12 * 50, 'y': 9 * 50}
            }
        }
    return position

def pergerakan(position):
    if varGlobals.striker and varGlobals.back:
        i=0
        xBack = position[1]['x']
        yBack = position[1]['y']
        xBack2 = 14 * 50
        yBack2 = 14 * 50
        xStriker = position[2]['x']
        yStriker = position[2]['y']

        while not (dataRobot.xpos[2]//50 == xStriker//50 and 
                    dataRobot.ypos[2]//50 == yStriker//50 and
                    dataRobot.xpos[1]//50 == xBack//50 and 
                    dataRobot.ypos[1]//50 == yBack//50 and not varGlobals.stop
                    ):
            if varGlobals.stop == True or i >= 20:
                print("sudah 5 detik")
                break
            else: 
                i+=1
                print("tunggu posisi")
                pindahAwalKiper()
                changePos(1,xBack,yBack,0)
                changePos(2,xStriker,yStriker,0)
        #untuk back ke-2
        while not (dataRobot.xpos[1]//50 == xBack2//50 and 
                    dataRobot.ypos[1]//50 == yBack2//50 and not varGlobals.stop
                    ):
            if varGlobals.stop == True:
                break
            else:
                print("tunggu posisi 2")
                changePos(1,xBack2,xBack2,0)
    
    #jika hanya striker
    elif varGlobals.striker and not varGlobals.back:
        i=0
        while not (dataRobot.xpos[2]//50==xStriker//50 and 
                    dataRobot.ypos[2]//50==yStriker//50 and not varGlobals.stop
                    ):
            if varGlobals.stop==True:
                break
            elif i>=20:
                print("sudah 5 detik")
                break
            else:
                i+=1
                print("wait position")
                changePos(2,xStriker,yStriker,0)
                pindahAwalKiper()
    
    #jika hanya back    
    elif not varGlobals.striker and varGlobals.back:
        i=0
        while not (dataRobot.xpos[1]//50==xBack//50 and 
                    dataRobot.ypos[1]//50==yBack//50 and not varGlobals.stop
                    ):
            if varGlobals.stop==True:
                break
            elif i>=20:
                print("sudah 5 detik")
                break
            else:
                i+=1
                print("wait position")
                changePos(1,xBack,yBack,0)
                pindahAwalKiper()
        
        while not (dataRobot.xpos[1]//50==xBack2//50 and 
                    dataRobot.ypos[1]//50==yBack2//50 and not varGlobals.stop
                    ):
            if varGlobals.stop==True or i >= 20:
                print("sudah 5 detik")
                break
            else: 
                i+=1
                print("Tunggu Posisi 2")
                changePos(1,xBack2,yBack2,0)

def strategy(idBack, idStriker):
    lihatBolaDiam(idStriker)
    lihatBolaDiam(idBack)
    ballPredictKiper()

    while varGlobals.start:
        if varGlobals.striker and varGlobals.back:
            ballPredictKiper()
            kejarBolaCepat(idBack)
            lihatBolaDiam(idStriker)
            tendangGiring(idBack)
            kejarBolaCepat(idBack)
            tendangKencang(idBack)
        
            #playGame
            while not varGlobals.stop:
                if varGlobals.ball_x<860 and dataRobot.catch_ball[2]==0:
                    kejarBolaCepat(idStriker)
                    lihatBolaDiam(idBack)
                    umpanTeman(idStriker)
                    kejarBolaCepat(idBack)
                    tendangKencang(idBack)
                elif varGlobals.ball_x>860:
                    lihatBolaGeser(idStriker)
                    lihatBolaDiam( idBack)
                    kejarBolaCepat(idBack)
                    tendangKencang(idBack)
                elif varGlobals.ball_x<860 and dataRobot.catch_ball[2]==1:
                    lihatBolaDiam(idBack)
                    umpanTeman(idStriker)
                    kejarBolaCepat(idBack)
                    tendangKencang(idBack)
        #striker
        elif varGlobals.striker and not varGlobals.back:
            ballPredictKiper()
            kejarBolaCepat(idStriker)
            tendangGiring(idStriker)
            kejarBolaCepat(idStriker)
            tendangKencang(idStriker)
            
            while not varGlobals.stop:
                if varGlobals.stop==True:
                    break
                else:
                    kejarBolaCepat(2)
                    tendangGiring(2)
                    kejarBolaCepat(2)
                    tendangKencang(2)
                    print("selesai tendang gawang")  
        #back  
        elif not varGlobals.striker and varGlobals.back:
            ballPredictKiper()
            kejarBolaCepat(idBack)
            tendangGiring(idBack)
            kejarBolaCepat(idBack)
            tendangKencang(idBack)
            while not varGlobals.stop:
                if varGlobals.stop==True:
                    break
                else:
                    kejarBolaCepat(1)
                    tendangGiring(1)
                    kejarBolaCepat(1)
                    tendangKencang(1)
                    print("selesai tendang gawang")

def dropBallTeam():
    reset()
    varGlobals.dropBall = True
    prestart = False

    while varGlobals.dropBall and not varGlobals.stop:
        print("Drop Ball Team")
        if not prestart:
            print("Drop Ball Team")
            position = setPosition(varGlobals.setBall_x, varGlobals.setBall_y)
            pergerakan(position)
            prestart = True
        elif prestart and varGlobals.start and not varGlobals.stop:
            strategy(1, 2)
        time.sleep(0.5)

def dropBallMusuh():
    reset()
    varGlobals.dropBall = True
    prestart = False

    while varGlobals.dropBall and not varGlobals.stop:
        print("Drop Ball Musuh")
        if not prestart:
            print("Drop Ball Musuh")
            position = setPosition(varGlobals.setBall_x, varGlobals.setBall_y)
            pergerakan(position)
            prestart = True
        elif prestart and varGlobals.start and not varGlobals.stop:
            strategy(1, 2)
        time.sleep(0.5)