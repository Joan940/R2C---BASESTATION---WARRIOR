##
# @file park.py
# @brief Modul untuk mengatur mode parkir robot setelah pertandingan atau saat transisi.
#
# Fungsi `park()` bertugas menonaktifkan semua strategi permainan
# dan menjaga robot dalam status diam sambil menunggu posisi robot sesuai syarat tertentu.
#
# Mode ini umum digunakan saat pertandingan selesai, time-out, atau saat fase transisi
# menuju kondisi idle dengan memantau posisi tertentu.
#
# @details
# Fungsi ini menonaktifkan semua flag strategi (kickoff, penalty, throw-in, dll),
# dan mengaktifkan flag `varGlobals.park = True` untuk masuk ke mode "park".
#
# Mode ini akan terus berjalan hingga `varGlobals.park == False` atau program dihentikan.
import modules.varGlobals as varGlobals
import time
import modules.dataRobot as dataRobot

##
# @brief Menjalankan mode parkir robot untuk memastikan posisi akhir sesuai.
#
# Fungsi ini akan:
# - Mematikan seluruh strategi permainan
# - Menyalakan mode `park`
# - Mengirim sinyal prestart 5x sekali saja
# - Mengecek posisi robot 2 hingga berada di x == 400
# - Looping dengan delay 0.5 detik selama mode `park` masih aktif
#
# @note
# Digunakan di akhir pertandingan atau saat robot harus diam terkontrol.
def park():
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
    varGlobals.park = True
    varGlobals.endPart = False
    
    prestart = False

    while varGlobals.park:
        print("ini Park")
        if not prestart:
            for i in range(5):
                print("send prestart Park")
            prestart=True
            while dataRobot.xpos[2]!=400:
                print("cek")
            print("posisi selesai")
        time.sleep(0.50)