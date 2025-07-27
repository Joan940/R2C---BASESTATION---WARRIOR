##
# @file simRobot.py
# @brief Modul simulasi pengiriman data ke robot (Kiper, Back, Striker) melalui UDP multicast.
#
# File ini menyediakan fungsi untuk membentuk dan mengirim paket data ke masing-masing robot
# berdasarkan ID dan perintah tertentu. Modul ini digunakan dalam lingkungan simulasi sepak bola robot.
#
# Format data dikirim dalam bentuk `bytearray(18)` dan mencakup informasi posisi, arah, status bola, dll.
#

from time import sleep
import modules.varGlobals as varGlobals
import socket

##
# @var robot_id
# @brief ID unik masing-masing robot (0 = Kiper, 1 = Back, 2 = Striker).
#
# Digunakan sebagai identifikasi pada byte pertama dalam paket data.

# Variabel-variabel lain seperti:
# kompas_value, xpos, ypos, ball_value, enemy1, enemy2, enemy3, catch_ball, connect
# bersifat placeholder/list default dan bisa digunakan sebagai penyimpanan sementara status robot.

robot_id = [0,1,2]
kompas_value = [0,1,2]
xpos = [0,1,2]
ypos = [0,1,2]
ball_value = [0,1,2]
enemy1 = [0,1,2]
enemy2 = [0,1,2]
enemy3 = [0,1,2]
catch_ball = [0,1,2]
connect = [0,1,2]

##
# @brief Mengirim data simulasi ke robot kiper.
#
# Fungsi ini memproses array `data` dan mengubahnya menjadi format `bytearray(18)`
# yang sesuai dengan protokol komunikasi robot kiper, kemudian mengirimkannya melalui UDP multicast.
#
# @param data Array dari nilai integer yang mencakup instruksi dan data posisi, arah, dan status robot.
#
# @note
# - data[1] == 255: mengirim perintah penuh (dengan arah dan posisi)
# - data[1] == 251: hanya mengirim posisi target (tanpa arah atau kontrol lain)
# - Byte ke-16 (index 15) digunakan untuk status, byte ke-17 (index 16) untuk status aktif
#
# @return Tidak ada.

def kiper(data):
    send=bytearray(18)
    if data[1]==255:
        send[0]=0
        send[1]=data[2]
        send[2]=data[3]
        send[3]=(((data[4]*50)+25) >> 8) & 0xFF
        send[4]=((data[4]*50)+25) & 0xFF
        send[5]=(((data[5]*50)+25) >> 8) & 0xFF
        send[6]=((data[5]*50)+25) & 0xFF
        send[7]=data[7]
        send[8]=data[8]
        send[9]=data[9]
        send[10]=data[10]
        send[11]=data[11]
        send[12]=data[12]
        send[13]=data[13]
        send[14]=data[14]
        send[15]=data[15]
        send[16]=1
        send[17]=data[16]
        sleep(0.15)
        send_robot(send)

    if data[1]==251:
        send[0]=0
        send[1]=0
        send[2]=0
        send[3]=(((data[2]*50)+25) >> 8) & 0xFF
        send[4]=((data[2]*50)+25) & 0xFF
        send[5]=(((data[3]*50)+25) >> 8) & 0xFF
        send[6]=((data[3]*50)+25) & 0xFF
        send[16]=1
        sleep(0.15)
        send_robot(send)
    print("kiper")

##
# @brief Mengirim data simulasi ke robot Back.
#
# Memproses array `data` menjadi `bytearray(18)` dan mengirimkannya ke robot Back.
# Mendukung 3 jenis perintah:
# - data[1] == 255: perintah kontrol penuh (arah, posisi, status)
# - data[1] == 254: perintah skill khusus (menghidupkan/mematikan flag tertentu)
# - data[1] == 251: perintah posisi target saja
#
# @param data Array integer yang mencakup kode perintah dan data status.
# @return Tidak ada.

def back(data):
    send=bytearray(18)
    if data[1]==255:
        send[0]=1
        send[1]=data[2]
        send[2]=data[3]
        send[3]=(((data[4]*50)+25) >> 8) & 0xFF
        send[4]=((data[4]*50)+25) & 0xFF
        send[5]=(((data[5]*50)+25) >> 8) & 0xFF
        send[6]=((data[5]*50)+25) & 0xFF
        send[7]=data[7]
        send[8]=data[8]
        send[9]=data[9]
        send[10]=data[10]
        send[11]=data[11]
        send[12]=data[12]
        send[13]=data[13]
        send[14]=data[14]
        send[15]=data[15]
        send[16]=1
        send[17]=data[16]
        # send[17]=data[6]
        # print("send[3]:", send[3])
        # print("send[4]:", send[4])
        # print("send[5]:", send[5])
        # print("send[6]:", send[6])
        sleep(0.15)
        send_robot(send)

    if data[1]==254:
        if data[2]==1:
            send[0]=1
            send[15]=1
            send[16]=1
            send[17]=1
            sleep(0.15)
            send_robot(send)
        elif data [2]==2:
            send[0]=1
            send[15]=0
            send[16]=1
            # send[17]=0
            sleep(0.15)
            send_robot(send)

    if data[1]==251:
        send[0]=1
        send[1]=0
        send[2]=0
        send[3]=(((data[2]*50)+25) >> 8) & 0xFF
        send[4]=((data[2]*50)+25) & 0xFF
        send[5]=(((data[3]*50)+25) >> 8) & 0xFF
        send[6]=((data[3]*50)+25) & 0xFF
        send[16]=1
        # send[17]=0
        sleep(0.15)
        send_robot(send)
    print("back")

##
# @brief Mengirim data simulasi ke robot Striker.
#
# Menerjemahkan data masukan ke format bytearray(18) dan mengirim melalui UDP.
# Mendukung perintah untuk kontrol penuh, aksi skill (mengatur bit tertentu), dan posisi target.
#
# @param data Array integer, sama seperti pada fungsi `kiper()` dan `back()`.
#
# @note
# - data[1] == 255: kontrol penuh
# - data[1] == 254: mengatur flag skill (bit ke-15)
# - data[1] == 251: hanya posisi
#
# @return Tidak ada.

def striker(data):
    send=bytearray(18)
    if data[1]==255:
        send[0]=2
        send[1]=data[2]
        send[2]=data[3]
        send[3]=(((data[4]*50)+25) >> 8) & 0xFF
        send[4]=((data[4]*50)+25) & 0xFF
        send[5]=(((data[5]*50)+25) >> 8) & 0xFF
        send[6]=((data[5]*50)+25) & 0xFF
        send[7]=data[7]
        send[8]=data[8]
        send[9]=data[9]
        send[10]=data[10]
        send[11]=data[11]
        send[12]=data[12]
        send[13]=data[13]
        send[14]=data[14]
        send[15]=data[15]
        send[16]=1
        send[17]=data[16]
        # send[17]=data[6]

        # print("send[3]:", send[3])
        # print("send[4]:", send[4])
        sleep(0.15)
        send_robot(send)

    if data[1]==254:
        print("masuk skill")
        if data[2]==1:
            send[0]=2
            send[15]=1
            send[16]=1
            sleep(0.15)
            send_robot(send)
        elif data [2]==2:
            send[0]=2
            send[15]=0
            send[16]=1
            sleep(0.15)
            send_robot(send)

    if data[1]==251:
        send[0]=2
        send[1]=0
        send[2]=0
        send[3]=(((data[2] * 50) + 25) >> 8) & 0xFF
        send[4]=((data[2] * 50) + 25) & 0xFF
        send[5]=(((data[3] * 50) + 25) >> 8) & 0xFF
        send[6]=((data[3] * 50) + 25) & 0xFF
        send[16]=1
        sleep(0.15)
        send_robot(send)
    print("striker")

##
# @brief Mengirim bytearray data ke robot melalui socket UDP multicast.
#
# Fungsi ini membuat socket UDP dengan TTL = 3 dan mengirim data ke alamat dan port yang didefinisikan
# dalam modul `varGlobals`.
#
# @param data Bytearray berisi 18 byte yang akan dikirim ke robot.
#
# @note Socket akan ditutup jika varGlobals.udp bernilai False.
# @return Tidak ada.

def send_robot(data):
    sendrobot=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sendrobot.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 3)
    if varGlobals.udp:
        sendrobot.sendto(data, (varGlobals.ADDRESS, int(varGlobals.PORT_ADD)))
        #print(len(data),data)
    else:
        sendrobot.close()