##
# @file start.py
# @brief Modul untuk menginisialisasi dan menjalankan loop start sistem robot.
#
# File ini mengatur inisialisasi awal mode start pada sistem robot.
# Ia mengaktifkan flag `start`, menonaktifkan `stop`, dan mengirim sinyal prestart
# satu kali sebelum memasuki loop operasi aktif.
#
# @author Joan
# @date 2025-07-27
#
# @details
# Modul ini bergantung pada:
# - `modules.varGlobals` untuk memantau dan mengubah status sistem global.
# - `modules.dataRobot` untuk akses ke status robot (meskipun tidak digunakan langsung di script ini).
#
# Saat dijalankan, fungsi `start()` akan melakukan:
# 1. Set `varGlobals.stop = False`
# 2. Set `varGlobals.start = True`
# 3. Jika `prestart` belum dijalankan, cetak 5 kali "send prestart Start"
# 4. Masuk ke loop yang terus berjalan selama `varGlobals.start == True`
import modules.varGlobals as varGlobals
import time
import modules.dataRobot as dataRobot

def start():
    varGlobals.stop = False
    varGlobals.start = True
    
    prestart = False

    while varGlobals.start:
        print("ini Start")
        if not prestart:
            for i in range(5):
                print("send prestart Start")
            prestart=True
        time.sleep(0.50)