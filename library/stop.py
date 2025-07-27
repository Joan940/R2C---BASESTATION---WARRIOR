##
# @file stop.py
# @brief Modul untuk menghentikan semua aktivitas strategi dan mengatur robot ke mode standby.
#
# Fungsi ini digunakan untuk menghentikan seluruh fase permainan (kickoff, penalty, dll)
# dan mengembalikan robot ke mode diam atau standby.
#
# Fungsi akan mengatur semua flag kontrol menjadi `False` dan mengirim perintah khusus
# ke robot agar masuk ke mode berhenti.
#
# @note
# Fungsi ini sangat penting untuk menjaga keamanan sistem dan mencegah aksi robot
# di luar kontrol saat pertandingan berakhir atau diberi perintah "Stop".
#
# @details
# - Mengatur semua status strategi (kickoff, free kick, throw-in, dll) ke `False`
# - Menyalakan `varGlobals.stop = True` untuk masuk ke mode berhenti
# - Mengirim bytearray berisi perintah spesifik (252 dan 123) ke semua robot sebagai sinyal stop
# - Masuk ke loop standby dengan perintah `data = [i, 1, 1]` hingga flag `stop` dimatikan dari luar
import modules.varGlobals as varGlobals
import time
import modules.dataRobot as dataRobot
from modules.comBasestation import send_robot

##
# @brief Menghentikan semua mode permainan dan mengatur robot ke mode standby.
#
# Fungsi ini akan:
# - Menonaktifkan seluruh flag strategi yang sedang berjalan
# - Mengatur robot agar berhenti bergerak
# - Mengirim sinyal stop ke semua robot sebanyak dua kali
# - Memasukkan robot ke dalam loop standby hingga `varGlobals.stop == False`
#
# @warning Fungsi ini akan terus mengirim perintah standby sampai dihentikan secara eksplisit.
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
