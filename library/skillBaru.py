##
# @file skillBaru.py
# @brief Modul kontrol aksi robot sepak bola: pergerakan, tendangan, giring, prediksi, dan grid.
#
# File ini berisi kumpulan fungsi untuk mengendalikan robot sepak bola
# seperti kejar bola, tendang, passing, dribble, serta manajemen grid posisi.
# Juga mencakup fungsi bantu seperti Bezier Curve untuk pergerakan dinamis.
#
# Digunakan oleh sistem simulasi dan real-time controller berbasis Python.
#
# @author Joan
# @date 2025-07-27
#
# @details
# Modul ini berinteraksi dengan modul lain:
# - modules.comBasestation: untuk mengirim data ke robot.
# - modules.varGlobals: menyimpan konfigurasi grid dan resolusi.
# - modules.dataRobot: menyimpan status posisi dan status robot.
#
# Format data yang dikirim ke robot adalah bytearray 3–6 byte tergantung aksi.
# Setiap perintah diberi kode tertentu sesuai dengan protokol komunikasi.
from modules.comBasestation import send_robot
from modules.coreMain import drawCenterHeading
import modules.varGlobals as varGlobals
import modules.dataRobot as dataRobot
import time

#################################
#         Fungsi Pembantu       #
#################################

## Membuat paket data standar (3 byte) untuk dikirim ke robot.
# @param id ID robot (0–2)
# @param kecepatan Nilai kecepatan (0–255)
# @param perintah Kode aksi (1–11)
# @return bytearray dengan 3 elemen
def setData(id, kecepatan, perintah):
    data = bytearray(3)
    data[0] = int(id)
    data[1] = int(kecepatan)
    data[2] = int(perintah)
    return data

## Mengirim data ke robot dengan penanganan error.
# @param data Bytearray yang akan dikirim
def kirimData(data):
    try:
        send_robot(data)
        time.sleep(0.25)  # Jeda untuk memberi waktu pada pengiriman data
    except Exception as e:
        print(f"Error mengirim data ke robot: {e}")

## Mengatur posisi robot berdasarkan koordinat dan sudut orientasi.
# @param id ID robot (0–2)
# @param x Koordinat X (pixel)
# @param y Koordinat Y (pixel)
# @param angle Sudut orientasi (0–360 derajat)
# @return Nilai gridX setelah diubah
def ubahPosisi(id, x, y, angle):
    data = bytearray(6)
    data[0] = int(id)
    data[1] = int(255)
    data[4] = int(x) // varGlobals.gridRes
    data[5] = int(y) // varGlobals.gridRes
    # print(data[4])
    if angle >= 0 and angle < 180:
        data[2] = 0
        data[3] = int(angle)
    elif angle >= 180 and angle <= 360:
        data[2] = 1
        data[3] = int(360 - angle)
    kirimData(data)
    return data[4]
    # time.sleep(1)




#################################
#     Fungsi Utama Permainan    #
#################################

def kejarBolaPelan(id):
    print("Kejar bola pelan")
    data = setData(id, 254, 1)
    kirimData(data)

def shoot(id):
    print("Tendang Gawang")
    data = setData(id, 254, 2)
    kirimData(data)

def passing(id):
    data = setData(id, 254, 3)
    print("Passing")
    kirimData(data)

def lihatBolaDiam(id):
    print("Lihat bola diam")
    data = setData(id, 254, 4)
    kirimData(data)

def lihatBolaGeser(id):
    print("lihat bola geser")
    data = setData(id, 254, 5)

    if id==1:
        ubahPosisi(2,(dataRobot.xpos[2]//50)+1, (dataRobot.ypos[2]//50)+1, 0)
        # time.sleep(3)
    elif id==2:
        ubahPosisi(1, (dataRobot.xpos[1]//50)+1, (dataRobot.ypos[1]//50)+1, 0)
        # time.sleep(3)
    else:
        kirimData(data)
    # time.sleep(0.5)

def kejarBolaCepat(id):
    print("Kejar bola cepat", id)
    data = setData(id, 254, 6)
    kirimData(data)
    if id == 1:
        lihatBolaDiam(2)
    if id == 2:
        lihatBolaDiam(1)

#################################
#          Fungsi Kiper         #
#################################

def pindahAwalKiper():
    print("Pindah ke posisi awal kiper")
    data = setData(0, 254, 8)
    kirimData(data)

def ballPredictKiper():
    print("Prediksi posisi bola kiper")
    data = setData(0, 254, 9)
    kirimData(data)

def powerShoot(id):
    print("Tendang Kencang")
    if (dataRobot.xpos[id] >= 50 and dataRobot.xpos[id] <= 400 and dataRobot.ypos[id] <= 650):
        ubahPosisi(id, dataRobot.xpos[id], dataRobot.ypos[id], 35)
    elif (dataRobot.xpos[id] >= 400 and dataRobot.xpos[id] <= 800 and dataRobot.ypos[id] <= 650):
        ubahPosisi(id, dataRobot.xpos[id], dataRobot.ypos[id], 340)
    else:
        shoot(id)

    data = setData(id, 254, 10)
    kirimData(data)

def siapTendang(id):
    print("trigger")
    data = setData(id, 254, 11)
    kirimData(data)    


#################################
#     Fungsi Manajemen Grid     #
#################################

def resetGrid(id, x, y):
    print(f"Reset grid robot {id}")
    data = bytearray(4)
    data[0] = int(id)
    data[1] = 253
    data[2] = int(x)
    data[3] = int(y)
    kirimData(data)

def sendGrid():
    print("Mengirim data grid")
    for i in range(2):
        data = bytearray(6)
        data[0] = i + 1
        data[1] = 255
        data[2] = 0
        data[3] = 0
        data[4] = int(varGlobals.CONFIG_BACK_GRID_X if i == 0 else varGlobals.CONFIG_STRIKER_GRID_X)
        data[5] = int(varGlobals.CONFIG_BACK_GRID_Y if i == 0 else varGlobals.CONFIG_STRIKER_GRID_Y)
        kirimData(data)


###########################################################
#        Fungsi Percobaan Masih Dalam Pengembangan        #
###########################################################

def bezier(t, points):
    n = len(points) - 1  
    x = sum(  
        binomial(n, i) * (1 - t) ** (n - i) * (t ** i) * points[i][0]  
        for i in range(n + 1)  
    )  
    y = sum(  
        binomial(n, i) * (1 - t) ** (n - i) * (t ** i) * points[i][1]  
        for i in range(n + 1)  
    )  
    return (x, y)  

def binomial(n, k):  
    if k < 0 or k > n:  
        return 0  
    if k == 0 or k == n:  
        return 1  
    k = min(k, n - k)
    c = 1  
    for i in range(k):  
        c = c * (n - i) // (i + 1)  
    return c

def bezierCurve(id, robo1_x, robo1_y, robo2_x, robo2_y, gridRes):  
    data = bytearray(3)  
    data[0] = int(id)  
    data[1] = 255  
    data[2] = 12  

    t = 0  # Mengatur nilai awal t  
    position = (0, 0)  

    if id == 1:  
        if dataRobot.status_robot[1] == 0 and dataRobot.status_robot[2] == 1:  
            control_points = [  
                (robo1_x, robo1_y),  # Titik awal  
                ((robo1_x + 800) / 2, robo1_y + 50),  # Titik kontrol  
                (robo1_x + 100, robo1_y)   # Titik akhir  
            ]  
            for i in range(10):  
                t = i / 10  # Memperoleh nilai t dalam rentang [0, 1]  
                position = bezier(t, control_points)  

                # Pembulatan pada posisi Y untuk menghindari kesalahan  
                rounded_y = round(position[1])  
                if rounded_y // gridRes <= 255:  
                    ubahPosisi(id, position[0], rounded_y, 0)  
                else:  
                    print(f"Warning: position[1] exceeds bounds after division: {rounded_y // gridRes}")  

    elif id == 2:  
        if dataRobot.status_robot[1] == 1 and dataRobot.status_robot[2] == 0:  
            control_points = [  
                (robo2_x, robo2_y),  # Titik awal  
                ((robo2_x + 700) / 2, robo2_y + 50),    # Titik kontrol  
                (robo2_x + 100, robo2_y)   # Titik akhir  
            ]  
            for i in range(100):  
                t = i / 100  
                position = bezier(t, control_points)  

                # Pembulatan pada posisi Y untuk menghindari kesalahan  
                rounded_y = round(position[1])  
                if rounded_y // gridRes <= 255:  
                    ubahPosisi(id, position[0], rounded_y, 0)  
                else:  
                    print(f"Warning: position[1] exceeds bounds after division: {rounded_y // gridRes}")
                time.sleep(0.15)

    kirimData(data)  
    return position

def dribbling(id):
    data=bytearray(3)
    print("Dribling")
    data[0]=int(id)
    data[1]=int(254)
    data[2]=7
    if dataRobot.catch_ball[id]==1:
        if id==1:
            lihatBolaDiam(2)
            ubahPosisi(2,(dataRobot.xpos[1]//50)+1,(dataRobot.ypos[1]//50)+1, 0)
        elif id==2:
            lihatBolaDiam(1)
            ubahPosisi(2,(dataRobot.xpos[2]//50)+1,(dataRobot.ypos[2]//50)+1, 0)
        passing(id)
    else:
        kirimData(data)