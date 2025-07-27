##
# @file dataRobot.py
# @brief Modul untuk menyimpan dan memperbarui data status robot sepak bola (Kiper, Back, Striker).
#
# Modul ini menerima data dalam bentuk array 18-byte dari masing-masing robot,
# lalu menyimpannya dalam variabel global untuk digunakan oleh simulasi, strategi, dan visualisasi.
#
# Fungsi utama:
# - `robotKiper(data, address)`
# - `robotBack(data, address)`
# - `robotStriker(data, address)`
#
# Setiap fungsi akan mem-parsing data yang dikirim robot dan menyimpannya ke dalam
# struktur data global berdasarkan ID robot.
#

##
# @var robot_id
# @brief ID untuk masing-masing robot [Kiper, Back, Striker].

# @var kompas_value
# @brief Nilai sudut kompas dari masing-masing robot.

# @var xpos, ypos
# @brief Posisi X dan Y masing-masing robot dalam koordinat lapangan.

# @var ball_value
# @brief Sudut arah bola relatif terhadap robot.

# @var ball_distance
# @brief Jarak bola dari masing-masing robot (khusus Kiper).

# @var enemy1, enemy2, enemy3
# @brief Sudut arah musuh terhadap masing-masing robot.

# @var catch_ball
# @brief Status kepemilikan bola (1 jika memegang bola, 0 jika tidak).

# @var connect
# @brief Status koneksi antara simulator dan robot (1 jika terhubung).

# @var status_robot
# @brief Status tambahan untuk masing-masing robot (diisi oleh Back dan Striker).

kiper_robot_ip = '0'
back_robot_ip = '0'
striker_robot_ip = '0'
robot_id = [0,1,2]
kompas_value = [0,1,2]
xpos = [0,1,2]
ypos = [0,1,2]
ball_value = [0,1,2]
status_robot = [0,1,2]
ball_distance = [0,1,2]
enemy1 = [0,1,2]
enemy2 = [0,1,2]
enemy3 = [0,1,2]
catch_ball = [0,1,2]
angle = [0,1,2]
connect = [0,1,2]

####################
#  KIPER_ID   = 0  #
#  BACK_ID    = 1  #
#  STRIKER_ID = 2  #
####################

##
# @brief Memproses data dari robot kiper dan menyimpannya ke dalam variabel global.
#
# Fungsi ini mengambil data 18-byte dari kiper dan mengekstrak informasi seperti:
# - ID robot
# - Kompas (sudut orientasi)
# - Posisi (X, Y)
# - Arah dan jarak bola
# - Arah musuh (enemy2 dan enemy3)
# - Status kepemilikan bola dan koneksi
#
# @param data Array 18-byte (list of int) berisi data sensor dan status robot.
# @param address Tuple alamat IP dan port sumber data.

def robotKiper(data, address):
    global kiper_robot_ip

    kiper_robot_ip = address[0]
    robot_id[0] = data[0]

    if data[1]==0:
        kompas_value[0] = data[2]
    elif data[1]==1:
        kompas_value[0]=(360-data[2])

    xpos[0] = (data[3] << 8) | data[4]
    ypos[0] = (data[5] << 8) | data[6]

    if data[7]==0:
        ball_value[0] = data[8]
    elif data[7]==1:
        ball_value[0]=(360-data[8])

    ball_distance[0] = data[10]

    # if data[9]==0:
    #     enemy1[0] = data[10]
    # elif data[9]==1:
    #     enemy1[0]=(360-data[10])

    if data[11]==0:
        enemy2[0] = data[12]
    elif data[11]==1:
        enemy2[0]=(360-data[12])
        
    if data[13]==0:
        enemy3[0] = data[14]
    elif data[13]==1:
        enemy3[0]=(360-data[14])

    catch_ball[0] = data[15]
    connect[0] = data[16]

##
# @brief Memproses data dari robot back dan menyimpannya ke dalam variabel global.
#
# Ekstraksi data mirip seperti kiper, tetapi menambahkan informasi:
# - Sudut enemy1
# - status_robot[1] untuk status tambahan dari robot back.
#
# @param data Array 18-byte dari robot back.
# @param address Tuple alamat IP dan port pengirim.

def robotBack(data, address):
    global back_robot_ip

    back_robot_ip = address[0]
    robot_id[1] = data[0]

    if data[1]==0:
        kompas_value[1] = data[2]
    elif data[1]==1:
        kompas_value[1]=(360-data[2])

    xpos[1] = (data[3] << 8) | data[4]
    ypos[1] = (data[5] << 8) | data[6]

    if data[7]==0:
        ball_value[1] = data[8]
    elif data[7]==1:
        ball_value[1]=(360-data[8])

    if data[9]==0:
        enemy1[1] = data[10]
    elif data[9]==1:
        enemy1[1]=(360-data[10])

    if data[11]==0:
        enemy2[1] = data[12]
    elif data[11]==1:
        enemy2[1]=(360-data[12])
        
    if data[13]==0:
        enemy3[1] = data[14]
    elif data[13]==1:
        enemy3[1]=(360-data[14])

    catch_ball[1] = data[15]
    connect[1] = data[16]

    status_robot[1] = data[17]

##
# @brief Memproses data dari robot striker dan menyimpannya ke dalam variabel global.
#
# Memperbarui:
# - Posisi
# - Sudut orientasi
# - Arah bola dan arah musuh
# - Status pemegang bola dan koneksi
# - status_robot[2] untuk status khusus striker
#
# @param data Array 18-byte dari robot striker.
# @param address Tuple alamat IP dan port pengirim.

def robotStriker(data, address):
    global striker_robot_ip

    striker_robot_ip = address[0]
    robot_id[2] = data[0]

    if data[1]==0:
        kompas_value[2] = data[2]
    elif data[1]==1:
        kompas_value[2]=(360-data[2])

    xpos[2] = (data[3] << 8) | data[4]
    ypos[2] = (data[5] << 8) | data[6]

    if data[7]==0:
        ball_value[2] = data[8]
    elif data[7]==1:
        ball_value[2]=(360-data[8])

    if data[9]==0:
        enemy1[2] = data[10]
    elif data[9]==1:
        enemy1[2]=(360-data[10])

    if data[11]==0:
        enemy2[2] = data[12]
    elif data[11]==1:
        enemy2[2]=(360-data[12])

    if data[13]==0:
        enemy3[2] = data[14]
    elif data[13]==1:
        enemy3[2]=(data[14])

    catch_ball[2] = data[15]
    connect[2] = data[16]

    status_robot[2] = data[17]

    
    
# def cekData():
#     print("--------------------------------")
#     print("RobotKiper")
#     print("Alamat IP Robot  :", kiper_robot_ip)
#     print("ID Robot         :", robot_id[0])
#     print("Kompas Value     :", kompas_value[0])
#     print("XPOS             :", xpos[0])
#     print("XPOS             :", xpos[0])
#     print("Ball Value       :", ball_value[0])
#     print("Enemy1 Value     :", enemy1[0])
#     print("Enemy2 Value     :", enemy2[0])
#     print("Enemy3 Value     :", enemy3[0])
#     print("Catch Ball       :", catch_ball[0])
#     print("--------------------------------")

#     print("RobotBack")
#     print("Alamat IP Robot  :", back_robot_ip)
#     print("ID Robot         :", robot_id[1])
#     print("Kompas Value     :", kompas_value[1])
#     print("XPOS             :", xpos[1])
#     print("XPOS             :", xpos[1])
#     print("Ball Value       :", ball_value[1])
#     print("Enemy1 Value     :", enemy1[1])
#     print("Enemy2 Value     :", enemy2[1])
#     print("Enemy3 Value     :", enemy3[1])
#     print("Catch Ball       :", catch_ball[1])
#     print("--------------------------------")

#     print("RobotStriker")
#     print("Alamat IP Robot  :", striker_robot_ip)
#     print("ID Robot         :", robot_id[2])
#     print("Kompas Value     :", kompas_value[2])
#     print("XPOS             :", xpos[2])
#     print("XPOS             :", xpos[2])
#     print("Ball Value       :", ball_value[2])
#     print("Enemy1 Value     :", enemy1[2])
#     print("Enemy2 Value     :", enemy2[2])
#     print("Enemy3 Value     :", enemy3[1])
#     print("Catch Ball       :", catch_ball[2])
#     print("--------------------------------")
