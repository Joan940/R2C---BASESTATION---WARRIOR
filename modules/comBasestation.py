##
# @file comBasestation.py
# @brief Modul komunikasi antara simulasi dan robot menggunakan protokol UDP multicast.
#
# Modul ini berfungsi untuk:
# - Menerima data dari robot melalui UDP multicast
# - Mengirim perintah ke robot
# - Memproses data dari robot dan menyimpannya ke struktur data global
#
# Komunikasi ini penting untuk menyinkronkan status robot dalam simulasi dengan data sebenarnya.
#

import time
import socket
import struct
import threading
from collections import deque
import modules.varGlobals as varGlobals
import modules.dataRobot as dataRobot

buffer_data = deque(maxlen=50)

prestart = False
rec_thread = None

##
# @brief Memulai thread penerimaan data dari robot melalui UDP multicast.
#
# Fungsi ini membuat dan menjalankan thread `rec_UDP()` secara daemon jika belum aktif.
# Thread ini akan menerima data UDP dari robot secara asynchronous.
#
# @note Hanya satu thread akan dijalankan untuk mencegah duplikasi.
# @return Tidak ada.

def startBs():
    global prestart, rec_thread
    if not prestart or (rec_thread is not None and not rec_thread.is_alive()):
        prestart = True
        rec_thread = threading.Thread(target=rec_UDP, daemon=True)
        rec_thread.start()
        print("Masuk Thread bind")

#############################################################################################
#                        MENERIMA DATA UDP MULTICAST DARI ROBOT                             #
#############################################################################################
##
# @brief Menerima data UDP multicast dari robot dan menyimpannya ke dalam buffer.
#
# Fungsi ini:
# - Membuka socket UDP multicast
# - Bergabung ke grup multicast berdasarkan alamat dan port dari `varGlobals`
# - Menerima paket data 18-byte dari robot
# - Memasukkan data yang valid ke `buffer_data` untuk diproses selanjutnya
#
# @exception BlockingIOError Ditangani saat socket tidak memiliki data (non-blocking).
# @exception socket.error Ditangani jika ada kesalahan pada socket.
# @exception Exception Ditangani untuk semua error lainnya.
# @return Tidak ada.

def rec_UDP():
    recUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    recUDP.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    recUDP.bind(('', int(varGlobals.PORT_ADD)))
    recUDP.setblocking(0)  # Set socket to non-blocking mode
    mreq = struct.pack("4sl", socket.inet_aton(varGlobals.ADDRESS), socket.INADDR_ANY)
    recUDP.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    try:
        while varGlobals.udp:
            try:
                data, address = recUDP.recvfrom(1024)
                
                if len(data) != 18:
                    continue
                
                buffer_data.append((data, address))

            except BlockingIOError:
                time.sleep(0.01)
            except socket.error as e:
                print("Socket error:", e)
            except Exception as e:
                print("Gagal Terima:", e)
    finally:
        recUDP.close()
        print("Socket telah ditutup.")

#############################################################################################
#                        MEMPROSES DATA DARI BUFFER                                         #
#############################################################################################
##
# @brief Memproses data yang diterima dari buffer dan menyimpannya ke struktur global.
#
# Fungsi ini dijalankan dalam thread daemon dan akan terus:
# - Mengambil data dari buffer (`buffer_data`)
# - Menentukan jenis robot (0 = Kiper, 1 = Back, 2 = Striker)
# - Memanggil fungsi `robotKiper()`, `robotBack()`, atau `robotStriker()` berdasarkan data
# - Menentukan status koneksi masing-masing robot berdasarkan byte ke-17 (data[16])
#
# @note Fungsi ini berjalan terus-menerus selama program aktif.
# @return Tidak ada.

def process_buffer():
    while True:
        if buffer_data:
            data, address = buffer_data.popleft()  # Ambil data pertama dari buffer
            
            if data[0] == 0:  # Kiper
                if data[16] == 1:
                    varGlobals.terimaData = True
                    varGlobals.kiper = True
                    varGlobals.conKiper = address[0]
                    dataRobot.robotKiper(data, address)
                elif data[16] == 0:
                    varGlobals.kiper = False

            elif data[0] == 1:  # Back
                if data[16] == 1:
                    varGlobals.terimaData = True
                    varGlobals.back = True
                    varGlobals.conBack = address[0]
                    dataRobot.robotBack(data, address)
                elif data[16] == 0:
                    varGlobals.back = False

            elif data[0] == 2:  # Striker
                if data[16] == 1:
                    varGlobals.terimaData = True
                    varGlobals.striker = True
                    varGlobals.conStriker = address[0]
                    dataRobot.robotStriker(data, address)
                elif data[16] == 0:
                    varGlobals.striker = False

        time.sleep(0.01)

#############################################################################################
#                         MENGIRIM DATA UDP MULTICAST KE ROBOT                              #
#############################################################################################
##
# @brief Mengirim data UDP multicast ke robot.
#
# Fungsi ini digunakan untuk mengirim perintah atau instruksi dalam bentuk `bytearray`
# ke alamat multicast yang telah dikonfigurasi di `varGlobals.ADDRESS` dan `PORT_ADD`.
#
# @param data Array of bytes (bytearray) berisi perintah yang akan dikirim ke robot.
#
# @exception Exception Ditangkap untuk menghindari crash jika pengiriman gagal.
# @return Tidak ada.

def send_robot(data):
    sendrobot = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sendrobot.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
    try:
        if varGlobals.udp:
            sendrobot.sendto(data, (varGlobals.ADDRESS, int(varGlobals.PORT_ADD)))
    except Exception as e:
        print("")
    finally:
        sendrobot.close()

##
# @brief Thread daemon yang menjalankan fungsi `process_buffer()`.
#
# Thread ini otomatis dimulai saat modul dijalankan dan terus aktif di latar belakang.
# Ini memungkinkan pemrosesan data robot secara asynchronous tanpa mengganggu thread utama.

process_thread = threading.Thread(target=process_buffer, daemon=True)
process_thread.start()
