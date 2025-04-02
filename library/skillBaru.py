from modules.comBasestation import send_robot
import modules.varGlobals as varGlobals
import modules.dataRobot as dataRobot
import time

#################################
#         Fungsi Pembantu       #
#################################

def setData(id, kecepatan, perintah):
    data = bytearray(3)
    data[0] = int(id)
    data[1] = int(kecepatan)
    data[2] = int(perintah)
    return data

def kirimData(data):
    try:
        send_robot(data)
        time.sleep(0.25)  # Jeda untuk memberi waktu pada pengiriman data
    except Exception as e:
        print(f"Error mengirim data ke robot: {e}")


def ubahPosisi(id, x, y, angle):
    data = bytearray(6)
    data[0] = int(id)
    data[1] = int(255)
    data[4] = int(x) // varGlobals.gridRes
    data[5] = int(y) // varGlobals.gridRes
    if angle >= 0 and angle < 180:
        data[2] = 0
        data[3] = int(angle)
    elif angle >= 180 and angle <= 360:
        data[2] = 1
        data[3] = int(360 - angle)
    kirimData(data)
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
#          Uji Coba Giring      #
#################################

def dribbling(id):
    data=bytearray(3)
    print("Dribling")
    data[0]=int(id)
    data[1]=int(254)
    data[2]=int(5)
    if dataRobot.catch_ball[id]==1:
        if id==1:
            lihatBolaDiam(2)
            ubahPosisi(2,(dataRobot.xpos[1]//50)+1,(dataRobot.ypos[1]//50)+1, 0)
            # time.sleep(3)
        elif id==2:
            lihatBolaDiam(1)
            ubahPosisi(2,(dataRobot.xpos[2]//50)+1,(dataRobot.ypos[2]//50)+1, 0)
            # time.sleep(3)
        passing(id)
    else:
        kirimData(data)
    # time.sleep(0.5)


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

def hindari_dummy(id):
    print("Hindari Dummy")

    x_robot = dataRobot.xpos[id]
    y_robot = dataRobot.ypos[id]

    if varGlobals.index_A == 0: 
        ubahPosisi(1, x_robot - 1, y_robot + 1, 0)
    elif varGlobals.index_A == 1:  
        ubahPosisi(1, x_robot - 1, y_robot, 0)  
    elif varGlobals.index_A == 2:  
        ubahPosisi(1, x_robot - 1, y_robot - 1, 0) 
    elif varGlobals.index_A == 3:  
        ubahPosisi(2, x_robot + 1, y_robot + 1, 0)  
    elif varGlobals.index_A == 4:  
        ubahPosisi(2, x_robot + 1, y_robot, 0)  
    elif varGlobals.index_A == 5:  
        ubahPosisi(2, x_robot + 1, y_robot - 1, 0)  
    else:
        print("Index A tidak valid, tidak ada tindakan")



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
