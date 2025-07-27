##
# @file coreMain.py
# @brief Modul utama visualisasi simulasi sepak bola robot menggunakan pygame.
#
# Menyediakan fungsi untuk menggambar berbagai elemen seperti robot, bola, musuh, heading,
# dummy, dan grid. Juga terdapat fungsi perhitungan geometri untuk heading, posisi bola,
# dan jarak antar objek.
#
# Modul ini digunakan untuk memvisualisasikan data robot secara real-time dalam tampilan lapangan.
#

import modules.varGlobals as varGlobals
import pygame
import math
import json
from modules.customColors import customColors as cc, text_to_screen as tts


#############################################################################################
#                           UNTUK MENAMPILKAN ROBOT DI LAPANGAN                             #
#############################################################################################
##
# @brief Menggambar gambar robot yang telah diputar berdasarkan arah (sudut).
#
# Fungsi ini memutar citra robot, menggambar arah (heading), dan menampilkannya di layar pygame.
#
# @param image Gambar robot.
# @param x Posisi X pada layar.
# @param y Posisi Y pada layar.
# @param angle Sudut rotasi robot dalam derajat (0–360).

def draw_rotated_image(image, x, y, angle):
    
    rotated_image = pygame.transform.rotate(image, 360-angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)

    if image != varGlobals.headingKiper and image != varGlobals.headingBack and image != varGlobals.headingStriker:
        drawHeading(x,y,360-angle)
        drawCenterHeading(x, y)
        
        #drawBallHeading(x,y,(angle-45))
    varGlobals.screen.blit(rotated_image, new_rect)

##
# @brief Menggambar garis heading arah hadap robot berdasarkan sudut.
#
# Garis heading ini membantu memperlihatkan orientasi robot di lapangan.
#
# @param x Koordinat X robot.
# @param y Koordinat Y robot.
# @param angle Sudut arah hadap robot (dalam derajat).
#
# @return pygame.Rect Batas area garis heading.

def drawHeading(x,y,angle):
    if 360-angle >= 0 and 360-angle <= 90:
        line_length_x = abs((varGlobals.lapanganResX*varGlobals.skala+varGlobals.offsetX - x) 
                            / math.cos(math.radians(angle))) if angle != 90 and angle != 270 else float('inf')
        line_length_y = abs((varGlobals.lapanganResY*varGlobals.skala+varGlobals.offsetY- y) 
                            / math.sin(math.radians(angle))) if angle != 0 and angle != 180 else float('inf')
        
        line_length = min(line_length_x, line_length_y)
      
    elif 360-angle >= 90 and 360-angle <= 180:
        line_length_x = abs((varGlobals.lapanganResX*varGlobals.skala+varGlobals.offsetX 
                             - (x+varGlobals.lapanganResX*varGlobals.skala)) 
                            / math.cos(math.radians(angle))) if angle != 90 and angle != 270 else float('inf')
        line_length_y = abs((varGlobals.lapanganResY*varGlobals.skala+varGlobals.offsetY- y) 
                            / math.sin(math.radians(angle))) if angle != 0 and angle != 180 else float('inf')
        
        line_length = min(line_length_x, line_length_y)
    
    elif 360-angle >= 180 and 360-angle <= 270:
        line_length_x = abs((varGlobals.lapanganResX*varGlobals.skala+varGlobals.offsetX 
                             - (x+varGlobals.lapanganResX*varGlobals.skala)) 
                            / math.cos(math.radians(angle))) if angle != 90 and angle != 270 else float('inf')
        line_length_y = abs((varGlobals.lapanganResY*varGlobals.skala+varGlobals.offsetY 
                             - (y+varGlobals.lapanganResY*varGlobals.skala)) 
                            / math.sin(math.radians(angle))) if angle != 0 and angle != 180 else float('inf')
        
        line_length = min(line_length_x, line_length_y)
        
    elif 360-angle >= 270 and 360-angle <= 360:
        line_length_x = abs((varGlobals.lapanganResX*varGlobals.skala+varGlobals.offsetX - x) 
                            / math.cos(math.radians(angle))) if angle != 90 and angle != 270 else float('inf')
        line_length_y = abs((varGlobals.lapanganResY*varGlobals.skala+varGlobals.offsetY
                             - (y+varGlobals.lapanganResY*varGlobals.skala)) 
                            / math.sin(math.radians(angle))) if angle != 0 and angle != 180 else float('inf')
        
        line_length = min(line_length_x, line_length_y)
        
    angle_rad = math.radians(int(angle %360))
    
    end_x = x + line_length * math.cos(angle_rad)
    end_y = y - line_length * math.sin(angle_rad)

    pygame.draw.line(varGlobals.screen, cc.RED, (x, y), (end_x, end_y), 2)
    return pygame.Rect(min(x, end_x), min(y, end_y), abs(x - end_x), abs(y - end_y))

##
# @brief Menggambar heading dari robot ke titik target.
#
# @param x Koordinat X robot.
# @param y Koordinat Y robot.
# @param target_x Koordinat X target.
# @param target_y Koordinat Y target.
#
# @return float Sudut antara robot dan target (dalam derajat).

def drawCenterHeading(x,y):
    line_length=100

    angle_rad = math.radians(0)
    end_x = x + line_length * math.cos(angle_rad)
    end_y = y - line_length * math.sin(angle_rad)

    pygame.draw.line(varGlobals.screen, cc.NAVY_BLUE, (x, y), (end_x, end_y), 2)

##
# @brief Menggambar heading bola dari posisi robot berdasarkan sudut tertentu.
#
# @param x Koordinat X robot.
# @param y Koordinat Y robot.
# @param theta Sudut arah bola dalam derajat.

def drawBallHeading(x,y,theta):
    line_length= 1200

    angle_rad = math.radians(theta %360)
    end_x = x + line_length * math.cos(angle_rad)
    end_y = y - line_length * math.sin(angle_rad)

    pygame.draw.line(varGlobals.screen, cc.PURPLE, (x, y), (end_x, end_y), 2)

##
# @brief Menghitung sudut relatif bola terhadap arah robot.
#
# @param robot_x Posisi X robot.
# @param robot_y Posisi Y robot.
# @param robot_angle Sudut arah robot.
# @param ball_x Posisi X bola.
# @param ball_y Posisi Y bola.
#
# @return float Sudut relatif bola terhadap robot (0–360).

def calculate_ball_angle(robot_x, robot_y, robot_angle, ball_x, ball_y):
    # Menghitung delta X dan delta Y antara robot dan bola
    dx = ball_x - robot_x
    dy = ball_y - robot_y

    # Menghitung sudut bola relatif terhadap robot
    angle_to_ball = math.degrees(math.atan2(dy, dx))
    
    # Menyesuaikan sudut dengan arah robot (kompas/sensor)
    relative_angle = (angle_to_ball - robot_angle) % 360

    if relative_angle < 0:
        relative_angle += 360

    return relative_angle

##
# @brief Menghitung koordinat bola berdasarkan jarak dari robot.
#
# @param robot_x Posisi X robot.
# @param robot_y Posisi Y robot.
# @param robot_angle Sudut arah robot.
# @param ball_distance Jarak bola dari robot.
#
# @return (x, y) Posisi bola.

def calculate_position_ball_single_robot(robot_x, robot_y, robot_angle, ball_distance):
    # Menghitung posisi bola berdasarkan jarak dari robot
    angle_rad = math.radians(robot_angle)
    
    # Menghitung koordinat bola
    ball_x = robot_x + ball_distance * math.cos(angle_rad)
    ball_y = robot_y + ball_distance * math.sin(angle_rad)

    return round(ball_x), round(ball_y)

##
# @brief Menghitung titik potong garis heading dari dua robot.
#
# @param robot_x1, robot_y1 Posisi robot pertama.
# @param robot_angle1 Sudut arah robot pertama.
# @param robot_x2, robot_y2 Posisi robot kedua.
# @param robot_angle2 Sudut arah robot kedua.
#
# @return (x, y) Titik potong garis heading, atau (-100, -100) jika sejajar.

def calculate_position(robot_x1, robot_y1, robot_angle1, robot_x2, robot_y2, robot_angle2):
    # Mencari persamaan garis dari setiap robot
    m1 = math.tan(math.radians(robot_angle1))
    b1 = robot_y1 - m1 * robot_x1

    m2 = math.tan(math.radians(robot_angle2))
    b2 = robot_y2 - m2 * robot_x2

    if m1 != m2: 
        intersection_x = (b2 - b1) / (m1 - m2)
        intersection_y = m1 * intersection_x + b1
    else:
        intersection_x = -100
        intersection_y = -100

    return round(intersection_x), round(intersection_y)


#############################################################################################
#                                   UNTUK MENAMPILKAN DUMMY                                 #
#############################################################################################

##
# @brief Menggambar dummy pada posisi tertentu di grid.
#
# @param x Koordinat grid X.
# @param y Koordinat grid Y.

def draw_dummy(x, y):
    width = 45
    height = 45

    pygame.draw.rect(varGlobals.screen, cc.BLACK, (x * 50, y * 50, width, height))

##
# @brief Menggeser dummy secara berurutan berdasarkan daftar posisi.
#
# @param x_options Daftar posisi X yang tersedia.
# @param y_options Daftar posisi Y yang tersedia.
# @param current_index Indeks sekarang untuk pemilihan posisi.
#
# @return (x, y) Posisi dummy saat ini.

def move_dummy_sequentially(x_options, y_options, current_index):
    x = x_options[current_index % len(x_options)]
    y = y_options[current_index % len(y_options)]
    return x, y


#############################################################################################
#                                 UNTUK MENAMPILKAN BOLA                                    #
#############################################################################################

##
# @brief Menggambar bola pada posisi tertentu.
#
# @param x Posisi X bola.
# @param y Posisi Y bola.

def draw_setBall(x, y):
    if x == -100 and y == -100:
        # Ball not detected, do not draw the circle
        return
    pygame.draw.circle(varGlobals.screen, cc.GRAY, ((x), (y)), 10)

def draw_ball(x, y):
    if x == -100 and y == -100:
        return
    pygame.draw.circle(varGlobals.screen, cc.RED, ((x), (y)), 10)

##
# @brief Menggambar garis lintasan bola.
#
# @param x1 Titik awal X.
# @param y1 Titik awal Y.
# @param x2 Titik akhir X.
# @param y2 Titik akhir Y.

def draw_line_bola(x1, y1, x2, y2):
    pygame.draw.aaline(varGlobals.screen, cc.GRASS_GREEN, (x1, y1), (x2, y2))


#############################################################################################
#                                UNTUK MENAMPILKAN MUSUH                                    #
#############################################################################################
##
# @brief Menggambar ikon robot musuh di lapangan.
#
# Konsepnya adalah ketika salah dua robot melihat robot musuh, akan didapatkan nilai/value berupa sudut.
# Lalu sudut yang didapatkan akan diolah, ditarik garis lurus sehingga mendapatkan perpotongan garis.
# Perpotongan garis tersebutlah yang akan menjadi prediksi di mana robot musuh berada.
# Konsep ini sama dengan bagaimana cara dalam memprediksi posisi bola.
#
# @param x Posisi X musuh.
# @param y Posisi Y musuh.

def draw_musuh(x, y):
    if varGlobals.cyan:
        new_rectMagenta = varGlobals.musuhMagenta.get_rect(center=varGlobals.musuhMagenta.get_rect(center=(x, y)).center)
        varGlobals.screen.blit(varGlobals.musuhMagenta,new_rectMagenta)
    if varGlobals.magenta:
        new_rectCyan = varGlobals.musuhCyan.get_rect(center=varGlobals.musuhCyan.get_rect(center=(x, y)).center)
        varGlobals.screen.blit(varGlobals.musuhCyan,new_rectCyan)

def draw_line_musuh(x1, y1, x2, y2):
    pygame.draw.line(varGlobals.screen, cc.BROWN, (x1, y1), (x2, y2), 2)

def draw_line_teman(x1, y1, x2, y2):
    pygame.draw.line(varGlobals.screen, cc.WHITE, (x1, y1), (x2, y2), 2)

##
# @brief Menggambar grid lapangan beserta label sumbu X dan Y.
#
# Label numerik akan ditampilkan pada setiap baris dan kolom grid.

def gambar_grid():
    for xGrid in range(int(varGlobals.offsetX-varGlobals.offsetResetPosX), 
                       int(varGlobals.lapanganResX*varGlobals.skala)+int(varGlobals.offsetX+varGlobals.offsetResetPosX)+int(varGlobals.gridRes*varGlobals.skala), 
                       int(varGlobals.gridRes*varGlobals.skala)):
        # 
        pygame.draw.line(varGlobals.screen, 
                         cc.AXOLOTL, 
                         (xGrid, varGlobals.offsetY-varGlobals.offsetResetPosY), 
                         (xGrid, int(varGlobals.lapanganResY*varGlobals.skala)+int(varGlobals.offsetY+varGlobals.offsetResetPosY)))
        # 
        angka = (xGrid - (varGlobals.offsetX-varGlobals.offsetResetPosX)) // int(varGlobals.gridRes*varGlobals.skala)
        # 
        if(angka<=25):
            tts(varGlobals.screen, 
                int(angka), 
                xGrid+((varGlobals.gridRes*varGlobals.skala)/2), 
                varGlobals.offsetY*0.6, 
                size=int(varGlobals.res[0]/90), 
                color=cc.AXOLOTL)

    for yGrid in range(int(varGlobals.offsetY-varGlobals.offsetResetPosY), 
                       int(varGlobals.lapanganResY*varGlobals.skala)+int(varGlobals.offsetY+varGlobals.offsetResetPosY)+int(varGlobals.gridRes*varGlobals.skala), 
                       int(varGlobals.gridRes*varGlobals.skala)):
        # 
        pygame.draw.line(varGlobals.screen, 
                         cc.AXOLOTL, 
                         (varGlobals.offsetX-varGlobals.offsetResetPosX, yGrid), 
                         (int(varGlobals.lapanganResX*varGlobals.skala)+int(varGlobals.offsetX+varGlobals.offsetResetPosX), yGrid))
        # 
        angka = (yGrid - (varGlobals.offsetY-varGlobals.offsetResetPosY)) // int(varGlobals.gridRes*varGlobals.skala)
        if(angka<=17):
            tts(varGlobals.screen, 
                int(angka), varGlobals.offsetX*0.93, 
                yGrid+((varGlobals.gridRes*varGlobals.skala)/2), 
                size=int(varGlobals.res[0]/90), 
                color=cc.AXOLOTL)

##
# @brief Membaca file JSON dan mengembalikan isi sebagai dictionary.
#
# @param filename Nama file JSON.
# @return Dict berisi data hasil parsing JSON.

def read_json(filename):  
    with open(filename, 'r') as file:  
        data = json.load(file)  
    return data  

################################################
#                   PERCOBAAN                  #
################################################

##
# @brief Menghitung jarak Euclidean antara dua titik.
#
# @param x1, y1 Titik 1.
# @param x2, y2 Titik 2.
# @return float Jarak Euclidean.

def calculate_distance(x1, y1, x2, y2):
    # menggunakan rumus Euclidean
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

##
# @brief Menentukan robot kita yang paling dekat dengan robot musuh.
#
# @param our_robots Dictionary berisi ID dan data posisi robot kita.
# @param enemy_robot Tuple berisi posisi musuh (x, y).
# @return (robot_id, distance) ID robot terdekat dan jaraknya.

def find_nearest_robot(our_robots, enemy_robot):
    nearest_robot = None
    min_distance = float('inf')
    
    for robot_id, (x, y, angle, image) in our_robots.items():
        distance = calculate_distance(x, y, enemy_robot[0], enemy_robot[1])
        
        if distance < min_distance:
            min_distance = distance
            nearest_robot = robot_id
    
    return nearest_robot, min_distance

##
# @brief Menghitung titik lintasan pada kurva Bézier berdasarkan kontrol poin.
#
# Fungsi ini masih dalam tahap pengembangan dengan tujuan awalnya adalah untuk menghindari musuh/dummy
# menggunakan pendekatan berzier curve
#
# @param t Parameter interpolasi (0–1).
# @param points Daftar koordinat kontrol.
# @return (x, y) Titik pada kurva Bézier.

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

##
# @brief Menghitung koefisien binomial (nCk).
#
# @param n Jumlah total.
# @param k Jumlah yang dipilih.
# @return int Nilai kombinasi nCk.

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

##
# @brief Menggambar kurva Bézier di layar pygame.
#
# @param screen Objek layar pygame.
# @param control_points Daftar titik kontrol.
# @param iterasi Jumlah segmen (semakin besar semakin halus).
# @param color Warna garis kurva.

def draw_bezier_curve(screen, control_points, iterasi, color):
    for i in range(iterasi):  
        t0 = i / iterasi  
        t1 = (i + 1) / iterasi  
        point0 = bezier(t0, control_points)  
        point1 = bezier(t1, control_points)  
        pygame.draw.line(screen, color, point0, point1, 2)