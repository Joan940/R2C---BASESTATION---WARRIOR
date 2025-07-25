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
