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
    position = {
        1: {'x': 5 * 50, 'y': 12 * 50, 'angle': 90},
        2: {'x': 11 * 50, 'y': 12 * 50, 'angle': 270}
    }
    return position

def pergerakan(position):
    for robot_id, pos in position.items():
        changePos(robot_id, pos['x'], pos['y'], pos['angle'])

def tungguPosisi(position):
    waktuMulai = time.time()
    while time.time() - waktuMulai < 10:
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
        lihatBolaDiam(1)
        kejarBolaPelan(2)
        print("selesai kejar bola")
        umpanTeman(2)
        print("selesai umpan teman")
        kejarBolaCepat(1)
        print("selesai umpan teman")
        while not (dataRobot.xpos[1]//50==5 and 
                    dataRobot.ypos[1]//50==15) and not varGlobals.stop:
            if varGlobals.stop==True:
                break
            else:
                print("Tunggu position siap tendang")
                changePos(1, 5 * 50, 15 * 50, 45)
                tendangKencang(1)
        while not (dataRobot.kompas_value[2] > 10 and dataRobot.kompas_value[2] < 350):
            if varGlobals.stop==True:
                break
            else:
                changePos(2, 8 * 50, 10 * 50, 0)
        while (dataRobot.xpos[2]//(11 * 50)//50 and
                dataRobot.ypos[2]//(12 * 50)//50):
            if varGlobals.stop==True:
                break
            else:
                changePos(2, 8 * 50, 10 * 50, 0)

        while not varGlobals.stop:
            if varGlobals.stop==True:
                break
            else:
                if varGlobals.ball_x<860 and dataRobot.catch_ball[2]==0:
                    kejarBolaCepat(2)
                    lihatBolaDiam(1)
                    umpanTeman(2)
                    kejarBolaCepat(1)
                    tendangKencang(1)
                elif varGlobals.ball_x>860:
                    lihatBolaGeser(2)
                    lihatBolaDiam(1)
                    #kejarBolaCepat(idStriker)
                    kejarBolaCepat(1)
                    tendangKencang(1)
                elif varGlobals.ball_x<860 and dataRobot.catch_ball[2]==1:
                    lihatBolaDiam(1)
                    umpanTeman(2)
                    kejarBolaCepat(1)
                    tendangKencang(1)
    #jika hanya striker
    elif varGlobals.striker and not varGlobals.back:
        while not varGlobals.stop:
            if varGlobals.stop==True:
                break
            else:
                kejarBolaPelan(2)
                tendangGiring(2)
                kejarBolaCepat(2)
                tendangKencang(2)
                print("selesai tendang gawang") 
    
    #jika hanya back
    elif not varGlobals.striker and varGlobals.back:
        while not varGlobals.stop:
            if varGlobals.stop==True:
                break
        else:
            kejarBolaPelan(1)
            tendangGiring(1)
            kejarBolaCepat(1)
            tendangKencang(1)
            print("selesai tendang gawang")
time.sleep(0.25)

def KickOffHandler(isTeamKickoff):
    reset() 
    varGlobals.runKickoffTeam = isTeamKickoff
    varGlobals.runKickoffMusuh = not isTeamKickoff
    while (varGlobals.runKickoffTeam or varGlobals.runKickoffMusuh) and not varGlobals.stop:
        print("Mulai Kick Off")
        pindahAwalKiper()
        ballPredictKiper()

        positions = setPosition(varGlobals.setBall_x, varGlobals.setBall_y)
        if varGlobals.runKickoffTeam:
            pergerakan(positions)
            tungguPosisi(positions)
            strategy(positions)

        if varGlobals.runKickoffMusuh:
            position = {
                1: {'x': 6 * 50, 'y': 10 * 50, 'angle': 45},
                2: {'x': 11 * 50, 'y': 12 * 50, 'angle': 315}
            }
            pergerakan(position)
            tungguPosisi(position)
            strategy(position)
            
        time.sleep(0.25)

def KickOffTeam():
    KickOffHandler(True)

def KickOffMusuh():
    KickOffHandler(False)