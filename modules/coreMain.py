import modules.varGlobals as varGlobals
import pygame
import math
import json
from modules.customColors import customColors as cc, text_to_screen as tts


#############################################################################################
#                           UNTUK MENAMPILKAN ROBOT DI LAPANGAN                             #
#############################################################################################

def draw_rotated_image(image, x, y, angle):
    
    rotated_image = pygame.transform.rotate(image, 360-angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)

    if image != varGlobals.headingKiper and image != varGlobals.headingBack and image != varGlobals.headingStriker:
        drawHeading(x,y,360-angle)
        drawCenterHeading(x, y)
        
        #drawBallHeading(x,y,(angle-45))
    varGlobals.screen.blit(rotated_image, new_rect)

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

def drawCenterHeading(x, y, target_x, target_y):  
    line_length = 100

    angle_rad = math.atan2(target_y - y, target_x - x) 
    angle_deg = math.degrees(angle_rad)
    end_x = x + line_length * math.cos(angle_rad)  
    end_y = y - line_length * math.sin(angle_rad)  

    pygame.draw.line(varGlobals.screen, cc.NAVY_BLUE, (x, y), (end_x, end_y), 2)
    return angle_deg 

def drawCenterHeading(x,y):
    line_length=100

    angle_rad = math.radians(0)
    end_x = x + line_length * math.cos(angle_rad)
    end_y = y - line_length * math.sin(angle_rad)

    pygame.draw.line(varGlobals.screen, cc.NAVY_BLUE, (x, y), (end_x, end_y), 2)

def drawBallHeading(x,y,theta):
    line_length= 1200

    angle_rad = math.radians(theta %360)
    end_x = x + line_length * math.cos(angle_rad)
    end_y = y - line_length * math.sin(angle_rad)

    pygame.draw.line(varGlobals.screen, cc.PURPLE, (x, y), (end_x, end_y), 2)

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

def calculate_position_ball_single_robot(robot_x, robot_y, robot_angle, ball_distance):
    # Menghitung posisi bola berdasarkan jarak dari robot
    angle_rad = math.radians(robot_angle)
    
    # Menghitung koordinat bola
    ball_x = robot_x + ball_distance * math.cos(angle_rad)
    ball_y = robot_y + ball_distance * math.sin(angle_rad)

    return round(ball_x), round(ball_y)

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


# def calculate_angle(x1, y1, xGoal, yGoal):
#     dx = xGoal - x1
#     dy = yGoal - y1

#     angle_rad = math.atan2(dy, dx)
#     angle_deg = math.degrees(angle_rad)

#     angle_deg = angle_deg % 360

#     return angle_deg

def draw_dummy(x, y):
    width = 45
    height = 45

    pygame.draw.rect(varGlobals.screen, cc.BLACK, (x * 50, y * 50, width, height))

def move_dummy_sequentially(x_options, y_options, current_index):
    x = x_options[current_index % len(x_options)]
    y = y_options[current_index % len(y_options)]
    return x, y


#############################################################################################
#                                 UNTUK MENAMPILKAN BOLA                                    #
#############################################################################################


def draw_setBall(x, y):
    if x == -100 and y == -100:
        # Ball not detected, do not draw the circle
        return
    pygame.draw.circle(varGlobals.screen, cc.GRAY, ((x), (y)), 10)

def draw_ball(x, y):
    if x == -100 and y == -100:
        return
    pygame.draw.circle(varGlobals.screen, cc.RED, ((x), (y)), 10)

def draw_line_bola(x1, y1, x2, y2):
    pygame.draw.aaline(varGlobals.screen, cc.GRASS_GREEN, (x1, y1), (x2, y2))


#############################################################################################
#                                UNTUK MENAMPILKAN MUSUH                                    #
#############################################################################################


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
            
def read_json(filename):  
    with open(filename, 'r') as file:  
        data = json.load(file)  
    return data  

################################################
#                   PERCOBAAN                  #
################################################

def calculate_distance(x1, y1, x2, y2):
    # menggunakan rumus Euclidean
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def find_nearest_robot(our_robots, enemy_robot):
    nearest_robot = None
    min_distance = float('inf')
    
    for robot_id, (x, y, angle, image) in our_robots.items():
        distance = calculate_distance(x, y, enemy_robot[0], enemy_robot[1])
        
        if distance < min_distance:
            min_distance = distance
            nearest_robot = robot_id
    
    return nearest_robot, min_distance

def draw_our_robots(our_robots, nearest_robot_id):
    for robot_id, (x, y, angle, image) in our_robots.items():
        draw_rotated_image(image, x, y, angle)
        
        if robot_id == nearest_robot_id:
            pygame.draw.circle(varGlobals.screen, cc.YELLOW, (x, y), 20, 2)

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

def draw_bezier_curve(screen, control_points, iterasi, color):
    for i in range(iterasi):  
        t0 = i / iterasi  
        t1 = (i + 1) / iterasi  
        point0 = bezier(t0, control_points)  
        point1 = bezier(t1, control_points)  
        pygame.draw.line(screen, color, point0, point1, 2)