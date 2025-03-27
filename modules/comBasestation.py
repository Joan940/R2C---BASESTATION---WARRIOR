# import socket
# import struct
# import modules.varGlobals as varGlobals
# import modules.dataRobot as dataRobot
# import threading
# from modules.simRobot import kiper, back, striker
# import time

# prestart = False
# rec_thread = None  # Variabel untuk menyimpan thread penerimaan UDP

# def startBs():
#     global prestart, rec_thread
#     # Cek apakah thread sudah berjalan atau belum
#     if not prestart or (rec_thread is not None and not rec_thread.is_alive()):
#         prestart = True
#         rec_thread = threading.Thread(target=rec_UDP, daemon=True)
#         rec_thread.start()
#         print("Masuk Thread bind")

# #############################################################################################
# #                        MENERIMA DATA UDP MULTICAST DARI ROBOT                             #
# #############################################################################################
# def rec_UDP():
#     recUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#     recUDP.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     recUDP.bind(('', int(varGlobals.PORT_ADD)))
#     recUDP.setblocking(0)  # Set socket to non-blocking mode
#     mreq = struct.pack("4sl", socket.inet_aton(varGlobals.ADDRESS), socket.INADDR_ANY)
#     recUDP.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

#     # LOOPING UNTUK MENERIMA DATA
#     try:
#         while varGlobals.udp:
#             try:
#                 data, address = recUDP.recvfrom(1024)
#                 # print("Terima data:", data)  # Debug log

#                 # Validasi panjang data yang diterima
#                 if len(data) != 17:
#                     # print("Data Tidak Valid")
#                     continue

#                 # Proses data berdasarkan tipe robot
#                 if data[0] == 0:  # Kiper
#                     if data[16] == 1:
#                         varGlobals.terimaData = True
#                         varGlobals.kiper = True
#                         varGlobals.conKiper = address[0]
#                         dataRobot.robotKiper(data, address)
#                     elif data[16] == 0:
#                         varGlobals.kiper = False

#                 elif data[0] == 1:  # Back
#                     if data[16] == 1:
#                         varGlobals.terimaData = True
#                         varGlobals.back = True
#                         varGlobals.conBack = address[0]
#                         dataRobot.robotBack(data, address)
#                     elif data[16] == 0:
#                         varGlobals.back = False

#                 elif data[0] == 2:  # Striker
#                     if data[16] == 1:
#                         varGlobals.terimaData = True
#                         varGlobals.striker = True
#                         varGlobals.conStriker = address[0]
#                         dataRobot.robotStriker(data, address)
#                     elif data[16] == 0:
#                         varGlobals.striker = False

#             except BlockingIOError:
#                 # Jika tidak ada data, lanjutkan loop
#                 time.sleep(0.01)
#             except socket.error as e:
#                 print("Socket error:", e)
#             except Exception as e:
#                 print("Gagal Terima:", e)
#     finally:
#         recUDP.close()
#         print("Socket telah ditutup.")

# #############################################################################################
# #                         MENGIRIM DATA UDP MULTICAST KE ROBOT                              #
# #############################################################################################
# def send_robot(data):
#     sendrobot = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     sendrobot.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
#     try:
#         if varGlobals.udp:
#             sendrobot.sendto(data, (varGlobals.ADDRESS, int(varGlobals.PORT_ADD)))
#     except Exception as e:
#         print("")
#     finally:
#         sendrobot.close()



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
                
                # Validasi panjang data
                if len(data) != 17:
                    continue  # Lewati data yang tidak valid
                
                # Simpan ke buffer sebelum diproses
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
def process_buffer():
    while True:
        if buffer_data:
            data, address = buffer_data.popleft()  # Ambil data pertama dari buffer
            
            # Proses berdasarkan tipe robot
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

# Jalankan thread untuk memproses buffer
process_thread = threading.Thread(target=process_buffer, daemon=True)
process_thread.start()
