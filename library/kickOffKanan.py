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
    siapTendang
)

# Fungsi reset tetap diperlukan untuk menginisialisasi variabel global
def KickOffKanan():
    varGlobals.runCornerKanan = False
    varGlobals.runCornerKiri = False
    
    varGlobals.runKickoffKanan = True
    varGlobals.runKickoffKiri = False
    
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

    print("Mulai Kick Off Kanan")

    # pindahAwalKiper()
    # ballPredictKiper()

    # positions = {
    #     1: {'x': 0, 'y': 0, 'angle': 360},  # Back
    #     2: {'x': 0, 'y': 0, 'angle': 90}   # Striker
    # }

    # # Lakukan pergerakan
    # for robot_id, pos in positions.items():
    #     ubahPosisi(robot_id, pos['x'], pos['y'], pos['angle'])

    # # Cek posisi
    # diPosisi = all(
    #     dataRobot.xpos[robot_id] // 50 == pos['x'] // 50 and 
    #     dataRobot.ypos[robot_id] // 50 == pos['y'] // 50 
    #     for robot_id, pos in positions.items()
    # )
    
    # print("Sudah Di Posisi" if diPosisi else "Belum Di Posisi")

    if varGlobals.runKickoffKanan:
        kejarBolaPelan(2)
        passing(1)
        lihatBolaDiam(2)
        lihatBolaDiam(1)

        # while dataRobot.status_robot[2] == 1 and dataRobot.catch_ball[2] == 1:
        #     siapTendang(1)
        #     break
        
        # if dataRobot.status_robot[1] == 0 and dataRobot.catch_ball[1] == 0:
        #     lihatBolaGeser(1)

        # if dataRobot.status_robot[1] == 5 and dataRobot.status_robot[2] == 5:
        #     passing(2)

        # dribbling(1)
        # # hindari_dummy(1)
        # lihatBolaGeser(2)
        # if dataRobot.status_robot[1] == 5 and dataRobot.status_robot[2] == 5:
        #     passing(1)

        # dribbling(2)
        # lihatBolaGeser(1)
        # if dataRobot.status_robot[1] == 5 and dataRobot.status_robot[2] == 5:
        #     passing(2)
        
        # dribbling(1)
        # lihatBolaGeser(2)
        # if dataRobot.status_robot[1] == 5 and dataRobot.status_robot[2] == 5:
        #     passing(1)

        # if dataRobot.catch_ball[1] == 1:
        #     varGlobals.jumlahPassing += 1

        # dribbling(1)
        # lihatBolaGeser(2)
        # passing(1)

        # if dataRobot.catch_ball[2] == 1:
        #     jumlahPassing += 1

        # dribbling(2)
        # passing(2)

        # if dataRobot.catch_ball[1] == 1:
        #     jumlahPassing += 1

        # dribbling(1)

        # print("Back berpindah 0,5 meter")
        # powerShoot(1)

    # if varGlobals.striker and not varGlobals.back:
    #     kejarBolaPelan(2)
    #     dribbling(2)
    #     powerShoot(2)
    #     print("Selesai tendang gawang") 

    # elif not varGlobals.striker and varGlobals.back:
    #     kejarBolaPelan(1)
    #     dribbling(1)
    #     powerShoot(1)
    #     print("Selesai tendang gawang")
                
    # if not varGlobals.striker and varGlobals.kiper and not varGlobals.back:
    #     pindahAwalKiper()
    #     ballPredictKiper()
    #     kejarBolaPelan(0)
    #     print("Selesai tendang gawang")

