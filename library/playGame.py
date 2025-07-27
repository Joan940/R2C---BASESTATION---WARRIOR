##
# @file playGame.py
# @brief Modul loop utama permainan robot sepak bola.
#
# Fungsi `playGame()` merupakan loop utama saat pertandingan dimulai.
# Fungsi ini dijalankan setelah semua kondisi dan strategi awal telah ditentukan.
#
# Selama flag `varGlobals.stop` bernilai False, maka sistem akan terus berada dalam loop ini.
# Di dalam loop ini seharusnya diisi oleh logika permainan seperti:
# - Strategi menyerang (Attack)
# - Strategi bertahan (Defense)
# - Pengambilan keputusan berdasarkan posisi bola dan lawan
#
# @details
# Loop ini berjalan setiap 2 detik dan akan berhenti hanya jika `varGlobals.stop` diset menjadi True.
# Fungsi ini menjadi kerangka utama untuk menjalankan AI atau rule engine selama pertandingan.
import time
import modules.varGlobals as varGlobals

def playGame():
    while not varGlobals.stop:
        print("Setelah semua state langsung ingame disini, isinya algoritma defend dan attack untuk mencetak gol")
        time.sleep(2)
