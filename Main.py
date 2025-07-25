import sys
import math
import time
import pygame
import modules.dataRobot as dataRobot
from modules.dataRobot import (
    robotBack,
    robotKiper,
    robotStriker
)
import modules.varGlobals as varGlobals
from modules.font import text_to_screen as tts
from modules.customColors import customColors as cc, text_to_screen as tts
from modules.simRobot import (
    back, 
    kiper, 
    striker
)
from modules.comBasestation import (
    startBs, 
    send_robot, 
    rec_UDP
)
from library.skillBaru import bezierCurve
from library.algorithm import playGame
from library.kickOffKanan import KickOffKanan
from library.kickOffKiri import KickOffKiri
from library.cornerKanan import cornerKanan
from library.cornerKiri import cornerKiri
from modules.coreMain import (
    gambar_grid, 
    draw_rotated_image, 
    calculate_position,
    # calculate_angle,
    calculate_position_ball_single_robot, 
    draw_ball,
    draw_line_bola, 
    draw_musuh, 
    draw_line_musuh, 
    draw_setBall, 
    move_dummy_sequentially, 
    draw_dummy,
    calculate_distance,
    draw_line_teman,
    draw_bezier_curve,
    read_json
)
from modules.decisionTree import (
    get_strategy,
    get_action
)

#######################################################################################################################################################################################
# from modules.comRefbox import connect_refbox                                                                                                                                        #
# from library.skils import powerShoot, pindahAwalKiper, ballPredictKiper, sendGrid, kejarBolaPelan, passing, lihatBolaDiam, kejarBolaCepat, ubahPosisi, resetGrid, lihatBolaGeser    #
# from lib.goalPosition import drawGoalPosition, drawGoalPositionRandom                                                                                                               #
# from lib.pathFinding import shortestPath                                                                                                                                            #
#######################################################################################################################################################################################

#############################################################################################
#                                     GLOBAL VARIABLE                                       #
#############################################################################################

####################
#  KIPER_ID   = 0  #
#  BACK_ID    = 1  #
#  STRIKER_ID = 2  #
####################

varGlobals.IP = '10.48.132.5'
varGlobals.PORT_IP = '28097'
varGlobals.ADDRESS = '224.16.32.110'
# varGlobals.ADDRESS = '172.11.13.109'
varGlobals.PORT_ADD = '12478'
# varGlobals.PORT_ADD = '8081'
varGlobals.MESSAGE_REFBOX = 'DISCONNECTED'
varGlobals.ref=False
varGlobals.udp=False
varGlobals.runMenu = False
varGlobals.runConf = False
varGlobals.runSim = False
varGlobals.CONNECT= 'CONNECT'
varGlobals.BIND = 'BIND'
varGlobals.conKiper = 'KIPER DISCONNECTED' 
varGlobals.conBack = 'BACK DISCONNECTED' 
varGlobals.conStriker = 'STRIKER DISCONNECTED' 
varGlobals.kiper = False
varGlobals.back = False
varGlobals.striker = False
varGlobals.CONFIG_BACK_GRID_X = '19'
varGlobals.CONFIG_BACK_GRID_Y = '8'
varGlobals.CONFIG_STRIKER_GRID_X = '13'
varGlobals.CONFIG_STRIKER_GRID_Y = '8'
varGlobals.CONFIG_DECISION_TREE = 'Tidak ada aksi yang cocok'

varGlobals.cyan=True
varGlobals.magenta=False

#############################################################################################
#############################################################################################



#############################################################################################
#                               LOGIKA UNTUK TOMBOL MENU                                    #
#############################################################################################

def button_action(text):
    
    data=bytearray(5)

    #LOGIKA TOMBOL
    text = text.lower() 
    if text == 'start':
        print("start")
        varGlobals.runMenu=False
        varGlobals.runConf=False
        Simulator()
        mainMenu()

    elif text == 'exit':
        sys.exit()

    elif text == 'robot configuration':
        print("robot configuration")
        varGlobals.runMenu=False
        varGlobals.runSim=False
        robotConfiguration()

    elif text == 'connect':
        if not varGlobals.ref:
            print("connect refbox")
            # connect_refbox()
            mainMenu()
        else:
            mainMenu()

    elif text == 'connected':
        if varGlobals.ref:
            varGlobals.MESSAGE_REFBOX="DISCONNECTED"
            varGlobals.refbox.close()
            varGlobals.CONNECT='CONNECT'
            varGlobals.ref=False
            mainMenu()
        else:
            mainMenu()

    elif text == 'bind':
        print("bind basestation")
        varGlobals.udp=True
        varGlobals.BIND='SUCCESS'
        startBs()
        # simStart()
        mainMenu()

    elif text == 'success':
        varGlobals.BIND = 'BIND'
        print("unbind basestation")
        varGlobals.kiper = False
        varGlobals.back = False
        varGlobals.striker =False
        varGlobals.conKiper = 'KIPER DISCONNECTED' 
        varGlobals.conBack = 'BACK DISCONNECTED' 
        varGlobals.conStriker = 'STRIKER DISCONNECTED'
        varGlobals.udp = False
        mainMenu()

    elif text =='save':
        print("Configuration Saved")
        mainMenu()

    elif text =='park':
        print("park")
        for i in range(5):
            data[0]=255
            data[1]=71
            send_robot(data)
        data[0]=255
        data[1]=90
        send_robot(data)
        Simulator()

    elif text =='park1':
        print("park1")
        for i in range(5):
            data[0]=255
            data[1]=103
            send_robot(data)
        data[0]=255
        data[1]=90
        send_robot(data)
        Simulator()

    elif text =='grid striker':
        print("grid striker")
        for i in range(5):
            data[0]=255
            data[1]=2
            send_robot(data)
        data[0]=255
        data[1]=90
        send_robot(data)
        Simulator()

    elif text =='grid back':
        print("grid back")
        for i in range(5):
            data[0]=255
            data[1]=1
            send_robot(data)
        data[0]=255
        data[1]=90
        send_robot(data)
        Simulator()

    elif text =='grid kiper':
        print("grid kiper")
        for i in range(5):
            data[0]=255
            data[1]=0
            send_robot(data)
        data[0]=255
        data[1]=90
        send_robot(data)
        Simulator()

    elif text == 'mode 1':
        # print("kick off kanan")
        data[0] = 255
        data[1] = 83
        send_robot(data)
        KickOffKanan()                                                            
        if varGlobals.terimaData == False :
            for i in range(5):
                data[0] = 255
                data[1] = 84
                send_robot(data)
        data[0] = 255
        data[1] = 90
        send_robot(data)
        # Simulator()

    elif text =='mode 2':
        print("kick off kiri")
        data[0] = 255
        data[1] = 84
        send_robot(data)
        KickOffKiri()
        if varGlobals.terimaData == False :
            for i in range(5):
                data[0] = 255
                data[1] = 84
                send_robot(data)
        data[0] = 255
        data[1] = 90
        send_robot(data)
        # Simulator()

    elif text =='mode 3':
        print("corner kanan")
        data[0] = 255
        data[1] = 84
        send_robot(data)
        # cornerKanan()
        # varGlobals.CORNERKANAN = True
        if varGlobals.terimaData == False :
            for i in range(5):
                data[0] = 255
                data[1] = 84
                send_robot(data)
        data[0] = 255
        data[1] = 90
        send_robot(data)
        Simulator()

    elif text == 'mode 4':
        varGlobals.updateDummy = False

        data1 = [1, 255, 1, 90, 14, 18, 160, 1, 85, 0, 110, 0, 0, 0, 0, 0, 1]
        back(data1)
        data2 = [2, 255, 0, 90, 3, 18, 0, 0, 90, 1, 0, 0, 0, 0, 0, 0, 1]
        striker(data2)

        Simulator()
        varGlobals.updateDummy = True

    elif text == 'mode 5':
        varGlobals.updateDummy = False

        data1 = [1, 255, 20, 10, 10, 8, 160, 0, 70, 0, 110, 0, 0, 0, 0, 1, 0]
        back(data1)
        data2 = [2, 255, 10, 5, 5, 5, 0, 1, 90, 0, 35, 0, 0, 0, 0, 0, 1]
        striker(data2)

        Simulator()
        varGlobals.updateDummy = True

    elif text == '1':
        global index_A, index_B, index_C
        varGlobals.updateDummy = True

        pindah_posisi_dummy1()
        varGlobals.index_A -= 1
        varGlobals.index_B -= 1
        varGlobals.index_C -= 1
        Simulator()

    elif text == '2':
        varGlobals.updateDummy = True

        pindah_posisi_dummy2()
        varGlobals.index_A -= 1
        varGlobals.index_B -= 1
        varGlobals.index_C -= 1
        Simulator()

    elif text == '3':
        varGlobals.updateDummy = True
        
        pindah_posisi_dummy3()
        varGlobals.index_A -= 1
        varGlobals.index_B -= 1
        varGlobals.index_C -= 1
        # Simulator()

    elif text =='stop':
        send=bytearray(3)
        print("panic stop")
        for i in range(3):
            send[0]= int(i)
            send[1]=252
            send[2]=123
            send_robot(send)
            time.sleep(0.15)
        Simulator()
        
    elif text =='back':
        print("back to menu")
        mainMenu()

    else:
        print('invalid entry')

#############################################################################################
#                                    MENGGAMBAR DUMMY                                       #
#############################################################################################

def pindah_posisi_dummy1():
    posisi_A = [(4, 16), (4, 18), (4, 20), (13, 16), (13, 18), (13, 20)]
    posisi_return = [(19.92, 4.25), (21.7, 4.25), (23.5, 4.25), (19.92, 11.4), (21.7, 11.4), (23.5, 11.4)]

    data = bytearray(4)
    x1, y1 = move_dummy_sequentially([p[0] for p in posisi_A], [p[1] for p in posisi_A], varGlobals.index_A)
    print(f"Posisi A = {x1}, {y1}")
    data[0] = 1
    data[1] = 1
    data[2] = int(x1)
    data[3] = int(y1)
    send_robot(data)
    
    x1_return, y1_return = posisi_return[varGlobals.index_A]

    varGlobals.index_A += 1
    if varGlobals.index_A >= len(posisi_A):
        varGlobals.index_A = 0

    return (x1_return, y1_return)

def pindah_posisi_dummy2():
    posisi_B = [(8, 18), (8, 20)]
    posisi_return = [(21.7, 7.8), (23.5, 7.8)]

    data = bytearray(4)
    x2, y2 = move_dummy_sequentially([p[0] for p in posisi_B], [p[1] for p in posisi_B], varGlobals.index_B)
    print(f"Posisi B = {x2}, {y2}")
    data[0] = 2
    data[1] = 1
    data[2] = int(x2)
    data[3] = int(y2)
    send_robot(data)

    x2_return, y2_return = posisi_return[varGlobals.index_B]

    varGlobals.index_B += 1
    if varGlobals.index_B >= len(posisi_B):
        varGlobals.index_B = 0 

    return (x2_return, y2_return)

def pindah_posisi_dummy3():
    posisi_C = [(27.1, 7.4), (27.1, 8.3)]
    # posisi_return = [(19.92, 4.25), (21.7, 4.25), (23.5, 4.25)]

    data = bytearray(4)
    x3, y3 = move_dummy_sequentially([p[0] for p in posisi_C], [p[1] for p in posisi_C], varGlobals.index_C)
    data[0] = 3
    data[1] = 1
    data[2] = int(x3)
    data[3] = int(y3)
    send_robot(data)
    
    # x1_return, y1_return = posisi_return[index_B]

    varGlobals.index_C += 1
    if varGlobals.index_C >= len(posisi_C):
        varGlobals.index_C = 0 

    return (x3, y3)

#############################################################################################
#                            LOGIKA UNTUK INPUT TEXT PADA MENU                              #
#############################################################################################

def textActionBackGridX(inp, input_key):
    if inp == varGlobals.CONFIG_BACK_GRID_X:
        print("BackGridX")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            varGlobals.CONFIG_BACK_GRID_X=varGlobals.CONFIG_BACK_GRID_X[:-1]
                        elif event.key == pygame.K_RETURN:
                            Simulator()
                        else:
                            varGlobals.CONFIG_BACK_GRID_X+=event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Simulator()
            pygame.draw.rect(varGlobals.screen, 
                             cc.WHITE, input_key[inp], 
                             border_radius=20)
            tts(varGlobals.screen,
                varGlobals.CONFIG_BACK_GRID_X,
                input_key[inp].centerx,
                input_key[inp].centery,
                int(varGlobals.res[0]/60),
                cc.RED)
            
            pygame.display.flip()
            varGlobals.clock.tick(60)

    else:
        print('invalid entry')
    Simulator()

def textActionBackGridY(inp, input_key):
    if inp == varGlobals.CONFIG_BACK_GRID_Y:
        print("BackGridY")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            varGlobals.CONFIG_BACK_GRID_Y=varGlobals.CONFIG_BACK_GRID_Y[:-1]
                        elif event.key == pygame.K_RETURN:
                            Simulator()
                        else:
                            varGlobals.CONFIG_BACK_GRID_Y+=event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Simulator()
            pygame.draw.rect(varGlobals.screen, 
                             cc.WHITE, input_key[inp], 
                             border_radius=20)
            tts(varGlobals.screen,
                varGlobals.CONFIG_BACK_GRID_Y,
                input_key[inp].centerx,
                input_key[inp].centery,
                int(varGlobals.res[0]/60),
                cc.RED)
            
            pygame.display.flip()
            varGlobals.clock.tick(60)
    else:
        print('invalid entry')
    Simulator()

def textActionStrikerGridX(inp, input_key):
    if inp == varGlobals.CONFIG_STRIKER_GRID_X:
        print("StrikerGridX")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            varGlobals.CONFIG_STRIKER_GRID_X=varGlobals.CONFIG_STRIKER_GRID_X[:-1]
                        elif event.key == pygame.K_RETURN:
                            Simulator()
                        else:
                            varGlobals.CONFIG_STRIKER_GRID_X+=event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Simulator()
            pygame.draw.rect(varGlobals.screen, 
                             cc.WHITE, input_key[inp], 
                             border_radius=20)
            tts(varGlobals.screen,
                varGlobals.CONFIG_STRIKER_GRID_X,
                input_key[inp].centerx,
                input_key[inp].centery,
                int(varGlobals.res[0]/60),
                cc.RED)
            
            pygame.display.flip()
            varGlobals.clock.tick(60)

    else:
        print('invalid entry')
    Simulator()

def textActionStrikerGridY(inp, input_key):
    if inp == varGlobals.CONFIG_STRIKER_GRID_Y:
        print("StrikerGridY")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            varGlobals.CONFIG_STRIKER_GRID_Y=varGlobals.CONFIG_STRIKER_GRID_Y[:-1]
                        elif event.key == pygame.K_RETURN:
                            Simulator()
                        else:
                            varGlobals.CONFIG_STRIKER_GRID_Y+=event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Simulator()
            pygame.draw.rect(varGlobals.screen, 
                             cc.WHITE, input_key[inp], 
                             border_radius=20)
            tts(varGlobals.screen,
                varGlobals.CONFIG_STRIKER_GRID_Y,
                input_key[inp].centerx,
                input_key[inp].centery,
                int(varGlobals.res[0]/60),
                cc.RED)
            
            pygame.display.flip()
            varGlobals.clock.tick(60)
    else:
        print('invalid entry')
    Simulator()

def text_action(inp,input_key):
    #LOGIKA INPUT TEXT
    if inp == varGlobals.IP:
        print ("ipRefbox")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            varGlobals.IP=varGlobals.IP[:-1]
                        elif event.key == pygame.K_RETURN:
                            mainMenu()
                        else:
                            varGlobals.IP+=event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mainMenu()
            pygame.draw.rect(varGlobals.screen, 
                             cc.WHITE, 
                             input_key[inp], 
                             border_radius=20)
            tts(varGlobals.screen,
                varGlobals.IP,input_key[inp].centerx,
                input_key[inp].centery,
                int(varGlobals.res[0]/60),
                cc.RED)
            
            pygame.display.flip()
            varGlobals.clock.tick(120)

    elif inp == varGlobals.PORT_IP:
        print("portRefbox")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            varGlobals.PORT_IP=varGlobals.PORT_IP[:-1]
                        elif event.key == pygame.K_RETURN:
                            mainMenu()
                        else:
                            varGlobals.PORT_IP+=event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mainMenu()
            pygame.draw.rect(varGlobals.screen, 
                             cc.WHITE, input_key[inp], 
                             border_radius=20)
            tts(varGlobals.screen,
                varGlobals.PORT_IP,
                input_key[inp].centerx,
                input_key[inp].centery,
                int(varGlobals.res[0]/60),
                cc.RED)
            
            pygame.display.flip()
            varGlobals.clock.tick(120)

    elif inp == varGlobals.ADDRESS:
        print("addressBS")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            varGlobals.ADDRESS=varGlobals.ADDRESS[:-1]
                        elif event.key == pygame.K_RETURN:
                            mainMenu()
                        else:
                            varGlobals.ADDRESS+=event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mainMenu()
            pygame.draw.rect(varGlobals.screen, 
                             cc.WHITE, 
                             input_key[inp], 
                             border_radius=20)
            tts(varGlobals.screen,
                varGlobals.ADDRESS,
                input_key[inp].centerx,
                input_key[inp].centery,
                int(varGlobals.res[0]/60),
                cc.RED)
            
            pygame.display.flip()
            varGlobals.clock.tick(120)

    elif inp == varGlobals.PORT_ADD:
        print("portBs")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            varGlobals.PORT_ADD=varGlobals.PORT_ADD[:-1]
                        elif event.key == pygame.K_RETURN:
                            mainMenu()
                        else:
                            varGlobals.PORT_ADD+=event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mainMenu()
            pygame.draw.rect(varGlobals.screen, 
                             cc.WHITE, input_key[inp], 
                             border_radius=20)
            tts(varGlobals.screen,
                varGlobals.PORT_ADD,
                input_key[inp].centerx,
                input_key[inp].centery,
                int(varGlobals.res[0]/60),
                cc.RED)
            
            pygame.display.flip()
            varGlobals.clock.tick(120)

    else:
        print('invalid entry')
    mainMenu()

#############################################################################################
#                              LOOPING DAN TAMPILAN UTAMA MENU                              #
#############################################################################################

def mainMenu():
    varGlobals.runConf=False
    varGlobals.runSim=False
    varGlobals.runMenu = True

    window_rect = pygame.Surface.get_rect(varGlobals.screen)
    mainClock = pygame.time.Clock()
    
    varGlobals.screen.blit(varGlobals.bgMenu,(0,0))

    #MENGATUR RESOLUSI TOMBOL
    BUTTON_WIDTH = varGlobals.res[0] * 0.4
    BUTTON_HEIGHT = varGlobals.res[1] * 0.1

    INP_TEXT_WIDTH = varGlobals.res[0] / 6
    INP_TEXT_HEIGHT = varGlobals.res[1] /20

    TEXT_MSG_WIDTH = varGlobals.res[0] / 7
    TEXT_MSG_HEIGHT = varGlobals.res[1] /20

    BUTTON_CONNECT_WIDTH = varGlobals.res[0] / 7
    BUTTON_CONNECT_HEIGHT = varGlobals.res[1] /15

    TEXT_ROBOT_WIDTH = varGlobals.res[0] / 10
    TEXT_ROBOT_HEIGHT = varGlobals.res[1] /30

    #MENGATUR POSISI TOMBOL
    NEW_GAME = pygame.rect.Rect(window_rect.centerx - (BUTTON_WIDTH / 2),
                                window_rect.centery - BUTTON_HEIGHT * 1.5,
                                BUTTON_WIDTH, BUTTON_HEIGHT)

    OPTIONS = pygame.rect.Rect(window_rect.centerx - (BUTTON_WIDTH / 2),
                               window_rect.centery,
                               BUTTON_WIDTH, BUTTON_HEIGHT)

    EXIT = pygame.rect.Rect(window_rect.centerx - (BUTTON_WIDTH / 2),
                            window_rect.centery + BUTTON_HEIGHT * 1.5,
                            BUTTON_WIDTH, BUTTON_HEIGHT)

    CONNECT_REFBOX = pygame.rect.Rect(window_rect.centerx - (BUTTON_CONNECT_WIDTH * 2.89)
                                      ,window_rect.centery + (BUTTON_CONNECT_HEIGHT * 1.4),
                                      BUTTON_CONNECT_WIDTH,BUTTON_CONNECT_HEIGHT)

    CONNECT_BS = pygame.rect.Rect(window_rect.centerx + (BUTTON_CONNECT_WIDTH * 1.91)
                                      ,window_rect.centery + (BUTTON_CONNECT_HEIGHT * 1.4),
                                      BUTTON_CONNECT_WIDTH,BUTTON_CONNECT_HEIGHT)
    buttons = {"START": NEW_GAME, 
               "ROBOT CONFIGURATION": OPTIONS, 
               "EXIT": EXIT, 
               varGlobals.CONNECT : CONNECT_REFBOX,
               varGlobals.BIND : CONNECT_BS}

    #MENGATUR POSISI INPUT TEXT REFBOX
    INP_IP = pygame.rect.Rect(window_rect.centerx - (INP_TEXT_WIDTH * 2.55),
                            window_rect.centery - INP_TEXT_HEIGHT * 2.45,
                            INP_TEXT_WIDTH, INP_TEXT_HEIGHT)

    INP_PORT_REFBOX = pygame.rect.Rect(window_rect.centerx - (INP_TEXT_WIDTH * 2.55),
                            window_rect.centery + INP_TEXT_HEIGHT / 3.45,
                            INP_TEXT_WIDTH, INP_TEXT_HEIGHT)

    #MENGATUR POSISI INPUT TEXT BASESTATION
    INP_ADDRESS = pygame.rect.Rect(window_rect.centerx + (INP_TEXT_WIDTH * 1.55),
                            window_rect.centery - INP_TEXT_HEIGHT * 2.45,
                            INP_TEXT_WIDTH, INP_TEXT_HEIGHT)

    INP_PORT_BS = pygame.rect.Rect(window_rect.centerx + (INP_TEXT_WIDTH * 1.55),
                            window_rect.centery + INP_TEXT_HEIGHT / 3.45,
                            INP_TEXT_WIDTH, INP_TEXT_HEIGHT)

    #MENGATUR POSISI TEXT PESAN ROBOT
    KIPER = pygame.rect.Rect(window_rect.centerx + (TEXT_ROBOT_WIDTH * 3.3),
                            window_rect.centery + (TEXT_ROBOT_HEIGHT * 5.36),
                            TEXT_ROBOT_WIDTH, TEXT_ROBOT_HEIGHT)

    BACK = pygame.rect.Rect(window_rect.centerx + (TEXT_ROBOT_WIDTH * 3.3),
                            window_rect.centery + (TEXT_ROBOT_HEIGHT * 6.7),
                            TEXT_ROBOT_WIDTH, TEXT_ROBOT_HEIGHT)

    STRIKER = pygame.rect.Rect(window_rect.centerx + (TEXT_ROBOT_WIDTH * 3.3),
                            window_rect.centery + (TEXT_ROBOT_HEIGHT * 8),
                            TEXT_ROBOT_WIDTH, TEXT_ROBOT_HEIGHT)

    input_key = {varGlobals.IP:INP_IP, 
                 varGlobals.PORT_IP:INP_PORT_REFBOX, 
                 varGlobals.ADDRESS:INP_ADDRESS, 
                 varGlobals.PORT_ADD:INP_PORT_BS}

    #MENGATUR POSISI TEXT PESAN DARI REFBOX
    MASSAGE = pygame.rect.Rect(window_rect.centerx - (TEXT_MSG_WIDTH * 2.89)
                                      ,window_rect.centery + (TEXT_MSG_HEIGHT * 4.8),
                                      TEXT_MSG_WIDTH,TEXT_MSG_HEIGHT)
    
    #LOOPING MENU
    click = False
    while varGlobals.runMenu:
        #DEKLARASI DATA
        msg_refbox ={varGlobals.MESSAGE_REFBOX:MASSAGE}
        add_kiper = {varGlobals.conKiper:KIPER}
        add_back = {varGlobals.conBack:BACK}
        add_striker = {varGlobals.conStriker:STRIKER}

        #PROTEKSI LOOPING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                varGlobals.runMenu = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                click = True

        mx, my = pygame.mouse.get_pos()

        #TOMBOL MENU
        border_thic = 5
        for button in buttons:
            if buttons[button].collidepoint(mx, my):
                pygame.draw.rect(varGlobals.screen,
                                 cc.FTEK,
                                 buttons[button],
                                 border_thic,
                                 border_radius=50)

                if click:
                    button_action(button)

            else:
                pygame.draw.rect(varGlobals.screen, 
                                 cc.WHITE, 
                                 buttons[button],
                                 border_thic, 
                                 border_radius = 50)
            tts(varGlobals.screen, 
                button, 
                buttons[button].centerx, 
                buttons[button].centery, 
                int(varGlobals.res[0]/50), 
                color=cc.WHITE)

        #INPUT TEXT
        for text in input_key:
            if input_key[text].collidepoint(mx,my):
                pygame.draw.rect(varGlobals.screen, 
                                 cc.FTEK, 
                                 input_key[text], 
                                 border_thic,
                                 border_radius=20)
                if click:
                    text_action(text,input_key)
            else:
                pygame.draw.rect(varGlobals.screen, 
                                 cc.WHITE, 
                                 input_key[text], 
                                 border_thic, 
                                 border_radius=20)
            tts(varGlobals.screen,
                text,
                input_key[text].centerx,
                input_key[text].centery,
                int(varGlobals.res[0]/65),
                cc.WHITE)

        #STATUS CONNECT/DISCONNECT ROBOT KIPER
        for txtKiper in add_kiper:
            if varGlobals.kiper:
                pygame.draw.rect(varGlobals.screen, 
                                 cc.WHITE, 
                                 add_kiper[txtKiper], 
                                 border_radius=20)
                tts(varGlobals.screen,
                    varGlobals.conKiper,
                    add_kiper[txtKiper].centerx,
                    add_kiper[txtKiper].centery,
                    int(varGlobals.res[0]/120), 
                    cc.BLACK)
            else:
                pygame.draw.rect(varGlobals.screen, 
                                 cc.RED, 
                                 add_kiper[txtKiper], 
                                 border_radius=20)
                tts(varGlobals.screen,
                    varGlobals.conKiper,
                    add_kiper[txtKiper].centerx,
                    add_kiper[txtKiper].centery,
                    int(varGlobals.res[0]/125),
                    cc.BLACK)

        #STATUS CONNECT/DISCONNECT ROBOT BACK
        for txtBack in add_back:
            if varGlobals.back:
                pygame.draw.rect(varGlobals.screen, 
                                 cc.WHITE, 
                                 add_back[txtBack], 
                                 border_radius=20)
                tts(varGlobals.screen,
                    varGlobals.conBack,
                    add_back[txtBack].centerx,
                    add_back[txtBack].centery,
                    int(varGlobals.res[0]/120),
                    cc.BLACK)
            else:
                pygame.draw.rect(varGlobals.screen, 
                                 cc.RED, add_back[txtBack], 
                                 border_radius=20)
                tts(varGlobals.screen,
                    varGlobals.conBack,
                    add_back[txtBack].centerx,
                    add_back[txtBack].centery,
                    int(varGlobals.res[0]/125),
                    cc.BLACK)

        #STATUS CONNECT/DISCONNECT ROBOT STRIKER
        for txtStriker in add_striker:
            if varGlobals.striker:
                pygame.draw.rect(varGlobals.screen, 
                                 cc.WHITE, 
                                 add_striker[txtStriker], 
                                 border_radius=20)
                tts(varGlobals.screen,
                    varGlobals.conStriker,
                    add_striker[txtStriker].centerx,
                    add_striker[txtStriker].centery,
                    int(varGlobals.res[0]/120),
                    cc.BLACK)
            else:
                pygame.draw.rect(varGlobals.screen, 
                                 cc.RED, 
                                 add_striker[txtStriker], 
                                 border_radius=20)
                tts(varGlobals.screen,
                    varGlobals.conStriker,
                    add_striker[txtStriker].centerx,
                    add_striker[txtStriker].centery,
                    int(varGlobals.res[0]/125),
                    cc.BLACK)
        
        #STATUS CONNECT/DISCONNECT DAN PESAN DARI REFBOX
        for msg_ref in  msg_refbox:
            if msg_ref=="DISCONNECTED" or msg_ref=="CONNECT AGAIN":
                pygame.draw.rect(varGlobals.screen, cc.RED, msg_refbox[msg_ref], border_radius=20)
            elif msg_ref=="WELCOME":
                pygame.draw.rect(varGlobals.screen, cc.SKY_BLUE, msg_refbox[msg_ref], border_radius=20)
            else:
                pygame.draw.rect(varGlobals.screen, cc.WHITE, msg_refbox[msg_ref], border_radius=20)
            
            tts(varGlobals.screen,
                varGlobals.MESSAGE_REFBOX,
                msg_refbox[msg_ref].centerx,
                msg_refbox[msg_ref].centery,
                int(varGlobals.res[0]/100),
                cc.BLACK)

        #PROTEKSI KETIKA REFBOX MELAKUKAN GAME RESET
        if varGlobals.ref and varGlobals.MESSAGE_REFBOX=="GAME RESET":
            varGlobals.ref=False
            pygame.draw.rect(varGlobals.screen,cc.GRASS_GREEN, MASSAGE, border_radius=20)
            tts(varGlobals.screen,
                varGlobals.MESSAGE_REFBOX,
                msg_refbox[msg_ref].centerx,
                msg_refbox[msg_ref].centery,
                int(varGlobals.res[0]/100),
                cc.BLACK)
            
            pygame.display.flip()
            time.sleep(3)
            # connect_refbox()

        click = False
        mainClock.tick(120)
        pygame.display.flip()
        # pygame.display.update()

#############################################################################################
#                            LOOPING DAN TAMPILAN CONFIGURATION                             #
#############################################################################################

def robotConfiguration():
    varGlobals.runMenu=False
    varGlobals.runSim=False
    varGlobals.runConf=True

    mainClock = pygame.time.Clock()
    
    varGlobals.screen.blit(varGlobals.bgConf,(0,0))

    window_rect = pygame.Surface.get_rect(varGlobals.screen)
    BUTTON_WIDTH = varGlobals.res[0] * 0.4
    BUTTON_HEIGHT = varGlobals.res[1] * 0.1

    SAVE = pygame.rect.Rect(window_rect.centerx - (BUTTON_WIDTH / 2),
                                window_rect.centery + BUTTON_HEIGHT * 3.7,
                                BUTTON_WIDTH, BUTTON_HEIGHT)
    buttons = {"SAVE": SAVE}

    click=False
    while varGlobals.runConf:
        #PROTEKSI LOOPING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                varGlobals.runConf = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                click = True

        mx, my = pygame.mouse.get_pos()

        #TOMBOL SAVE
        for button in buttons:
            if buttons[button].collidepoint(mx, my):
                pygame.draw.rect(varGlobals.screen, cc.FTEK2, buttons[button], border_radius=50)
                if click:
                    button_action(button)

            else:
                pygame.draw.rect(varGlobals.screen, cc.FTEK, buttons[button], border_radius=50)
            tts(varGlobals.screen, 
                button, 
                buttons[button].centerx, 
                buttons[button].centery, 
                int(varGlobals.res[0]/50), 
                color=cc.WHITE)

        click = False
        mainClock.tick(60)
        pygame.display.flip()

#############################################################################################
#                              LOOPING DAN TAMPILAN SIMULATOR                               #
#############################################################################################

def Simulator():
    global posisi_dummy1, posisi_dummy2, posisi_dummy3

    varGlobals.runMenu=False
    varGlobals.runConf=False
    varGlobals.runSim=True

    window_rect = pygame.Surface.get_rect(varGlobals.screen)
    mainClock = pygame.time.Clock()

    #MENGATUR RESOLUSI TOMBOL
    BUTTON_WIDTH = varGlobals.res[0] * 0.10
    BUTTON_HEIGHT = varGlobals.res[1] * 0.06
    TEXT_MSG_WIDTH = varGlobals.res[0] / 10
    TEXT_MSG_HEIGHT = varGlobals.res[1] / 25
    TEXT_ROBOT_WIDTH = varGlobals.res[0] / 10
    TEXT_ROBOT_HEIGHT = varGlobals.res[1] / 30
    INP_TEXT_WIDTH = varGlobals.res[0] / 20
    INP_TEXT_HEIGHT = varGlobals.res[1] / 50
    TEXT_DECISION_WIDTH = varGlobals.res[0] * 0.10
    TEXT_DECISION_HEIGHT = varGlobals.res[1] * 0.06
    
    # textbox config  
    INP_CONFIG_BACK_GRID_X = pygame.rect.Rect(window_rect.centerx + (INP_TEXT_WIDTH * 5.9),
                            window_rect.centery - (INP_TEXT_HEIGHT * 1.4),
                            INP_TEXT_WIDTH, INP_TEXT_HEIGHT)

    INP_CONFIG_BACK_GRID_Y = pygame.rect.Rect(window_rect.centerx + (INP_TEXT_WIDTH * 8),
                            window_rect.centery - (INP_TEXT_HEIGHT * 1.4),
                            INP_TEXT_WIDTH, INP_TEXT_HEIGHT)
    
    INP_CONFIG_STRIKER_GRID_X = pygame.rect.Rect(window_rect.centerx + (INP_TEXT_WIDTH * 5.9),
                            window_rect.centery - (INP_TEXT_HEIGHT * 4.4),
                            INP_TEXT_WIDTH, INP_TEXT_HEIGHT)

    INP_CONFIG_STRIKER_GRID_Y = pygame.rect.Rect(window_rect.centerx + (INP_TEXT_WIDTH * 8),
                            window_rect.centery - (INP_TEXT_HEIGHT * 4.4),
                            INP_TEXT_WIDTH, INP_TEXT_HEIGHT)
    
    INP_CONFIG_DECISION_TREE = pygame.rect.Rect(window_rect.centerx + (TEXT_DECISION_WIDTH * 2.85),
                            window_rect.centery + TEXT_DECISION_HEIGHT * (-4.3),
                            TEXT_DECISION_WIDTH/0.59, TEXT_DECISION_HEIGHT/2)
    

    input_key_back_grid_x = {varGlobals.CONFIG_BACK_GRID_X:INP_CONFIG_BACK_GRID_X}
    input_key_back_grid_y = {varGlobals.CONFIG_BACK_GRID_Y:INP_CONFIG_BACK_GRID_Y}
    input_key_striker_grid_x = {varGlobals.CONFIG_STRIKER_GRID_X:INP_CONFIG_STRIKER_GRID_X}
    input_key_striker_grid_y = {varGlobals.CONFIG_STRIKER_GRID_Y:INP_CONFIG_STRIKER_GRID_Y}

    # checkbox config
    checkbox_size = varGlobals.res[1] * 0.02
    checkbox_pos_x = varGlobals.res[0] * 0.1
    checkbox_pos_y = varGlobals.res[1] * 0.89
    checkbox_margin = varGlobals.res[0] * 0.07

    checkboxCyan = pygame.Rect(checkbox_pos_x, checkbox_pos_y, checkbox_size, checkbox_size)
    checkboxCyan_clicked = False
    checkboxMagenta = pygame.Rect(checkbox_pos_x + checkbox_size + checkbox_margin, 
                                  checkbox_pos_y, 
                                  checkbox_size, 
                                  checkbox_size)
    checkboxGridKiper = pygame.Rect(checkbox_pos_x*7.75, 
                                    checkbox_pos_y/2.53, 
                                    checkbox_size, 
                                    checkbox_size)
    checboxGridKiper_clicked = False

    checkboxGridBack = pygame.Rect(checkbox_pos_x*8.42, 
                                    checkbox_pos_y/2.53, 
                                    checkbox_size, 
                                    checkbox_size)
    checkboxGridBack_clicked = False

    checkboxGridStriker = pygame.Rect(checkbox_pos_x*9.09, 
                                    checkbox_pos_y/2.53, 
                                    checkbox_size, 
                                    checkbox_size)
    checkboxGridStriker_clicked = False
    
    checkboxMagenta_clicked = False

    # frame congfig
    frame_width = varGlobals.res[0] * 0.157
    frame_height = varGlobals.res[1] * 0.14
    frame_color = cc.WHITE
    frame_thickness = 2
    frame_rect = pygame.Rect((varGlobals.screen_width - frame_width) // 2, 
                             varGlobals.screen_height - frame_height - 10, 
                             frame_width, 
                             frame_height)

    # surface frame
    frame_striker = pygame.Surface((frame_width, frame_height))
    frame_back = pygame.Surface((frame_width, frame_height))
    frame_kiper = pygame.Surface((frame_width, frame_height))

    text_font = pygame.font.Font('/media/joan/Windows-SSD/Users/LENOVO/BASESTATION/assets/Consolas.ttf', int(varGlobals.res[0]/75))
    text_color = cc.BLACK

    # inisialisasi posisi 
    content_x = 0
    content_y = 0

    # variabel untuk scrolling
    scrolling = False
    scrolling_pos = None
    scrolling_offset = pygame.Vector2(0, 0)

    #####################################################################################################################################
    #####################################################################################################################################
    #####################################################################################################################################
   
    #MENGATUR POSISI TOMBOL
    # PARK = pygame.rect.Rect(window_rect.centerx + (BUTTON_WIDTH * 2.6),
    #                             window_rect.centery + BUTTON_HEIGHT * 2.2,
    #                             BUTTON_WIDTH, BUTTON_HEIGHT)

    # STOP = pygame.rect.Rect(window_rect.centerx + (BUTTON_WIDTH * 3.65),
    #                             window_rect.centery + BUTTON_HEIGHT * 2.2,
    #                             BUTTON_WIDTH, BUTTON_HEIGHT)

    KOTAK = pygame.rect.Rect(window_rect.centerx + (BUTTON_WIDTH * 2.85),
                                window_rect.centery + BUTTON_HEIGHT * (-5),
                                BUTTON_WIDTH/2, BUTTON_HEIGHT/2)
    DUMMY = pygame.rect.Rect(window_rect.centerx + (BUTTON_WIDTH * 3.45),
                                window_rect.centery + BUTTON_HEIGHT * (-5),
                                BUTTON_WIDTH/2, BUTTON_HEIGHT/2)
    KOTAK_DUMMY = pygame.rect.Rect(window_rect.centerx + (BUTTON_WIDTH * 4.05),
                                window_rect.centery + BUTTON_HEIGHT * (-5),
                                BUTTON_WIDTH/2, BUTTON_HEIGHT/2)
    BACK = pygame.rect.Rect(window_rect.centerx + (BUTTON_WIDTH * 3.44),
                                window_rect.centery + BUTTON_HEIGHT * 3.27,
                                BUTTON_WIDTH/2.5, BUTTON_HEIGHT/2.5)
    RIGHT_KICKOFF = pygame.rect.Rect(window_rect.centerx + (BUTTON_WIDTH * 3.12),
                                window_rect.centery + BUTTON_HEIGHT * 0.2,
                                BUTTON_WIDTH, BUTTON_HEIGHT)
    LEFT_KICKOFF = pygame.rect.Rect(window_rect.centerx + (BUTTON_WIDTH * 2.6),
                                window_rect.centery + BUTTON_HEIGHT * 1.2,
                                BUTTON_WIDTH, BUTTON_HEIGHT)
    LEFT_CORNER = pygame.rect.Rect(window_rect.centerx + (BUTTON_WIDTH * 3.65),
                                window_rect.centery + BUTTON_HEIGHT * 1.2,
                                BUTTON_WIDTH, BUTTON_HEIGHT)
    RIGHT_CORNER = pygame.rect.Rect(window_rect.centerx + (BUTTON_WIDTH * 2.6),
                                window_rect.centery + BUTTON_HEIGHT * 2.2,
                                BUTTON_WIDTH, BUTTON_HEIGHT)
    MODE_5 = pygame.rect.Rect(window_rect.centerx + (BUTTON_WIDTH * 3.65),
                                window_rect.centery + BUTTON_HEIGHT * 2.2,
                                BUTTON_WIDTH, BUTTON_HEIGHT)

    buttons = {"MODE 1": RIGHT_KICKOFF,
               "MODE 2": LEFT_KICKOFF,
               "MODE 3": RIGHT_CORNER,
               "MODE 4": LEFT_CORNER,
               "MODE 5": MODE_5,
               "BACK": BACK,
               "1": KOTAK,
               "2": DUMMY,
               "3": KOTAK_DUMMY}
    
    #####################################################################################################################################
    #####################################################################################################################################
    #####################################################################################################################################

    #MENGATUR POSISI TEXT PESAN DARI REFBOX
    MASSAGE = pygame.rect.Rect(window_rect.centerx - (TEXT_MSG_WIDTH * 3.6)
                                      ,window_rect.centery + (TEXT_MSG_HEIGHT * 7.75),
                                      TEXT_MSG_WIDTH,TEXT_MSG_HEIGHT)

    #MENGATUR POSISI TEXT PESAN ROBOT
    KIPER = pygame.rect.Rect(window_rect.centerx + (TEXT_ROBOT_WIDTH * 3.5),
                            window_rect.centery + (TEXT_ROBOT_HEIGHT * 7.52),
                            TEXT_ROBOT_WIDTH, TEXT_ROBOT_HEIGHT)

    BACK = pygame.rect.Rect(window_rect.centerx + (TEXT_ROBOT_WIDTH * 1.19),
                            window_rect.centery + (TEXT_ROBOT_HEIGHT * 7.52),
                            TEXT_ROBOT_WIDTH, TEXT_ROBOT_HEIGHT)

    STRIKER = pygame.rect.Rect(window_rect.centerx - (TEXT_ROBOT_WIDTH * 1.15),
                            window_rect.centery + (TEXT_ROBOT_HEIGHT * 7.52),
                            TEXT_ROBOT_WIDTH, TEXT_ROBOT_HEIGHT)
    click=False

    #####################################################################################################################################
    #####################################################################################################################################
    #####################################################################################################################################

    #MENGGAMBIL NILAI DUMMY
    if varGlobals.updateDummy:
        posisi_dummy1 = pindah_posisi_dummy1()
        posisi_dummy2 = pindah_posisi_dummy2()
        posisi_dummy3 = pindah_posisi_dummy3()

    #####################################################################################################################################
    #####################################################################################################################################
    #####################################################################################################################################

    while varGlobals.runSim:

        playGame()

        textsKiper = [
        "robot_id       : " + str(dataRobot.robot_id[0]),
        "kompas_value   : " + str(dataRobot.kompas_value[0]),
        "xpos           : " + str(dataRobot.xpos[0]),
        "ypos           : " + str(dataRobot.ypos[0]),
        "ball_value     : " + str(dataRobot.ball_value[0]),
        # "ball_distance: " + str(dataRobot.ball_distance[0]),
        "enemy1_value   : " + str(dataRobot.enemy1[0]),
        "enemy2_value   : " + str(dataRobot.enemy2[0]),
        "enemy3_value   : " + str(dataRobot.enemy3[0]),
        "catch_ball     : " + str(dataRobot.catch_ball[0]),
        "dummy 3        : " + str(varGlobals.index_C)
        ]

        textsBack = [
        "robot_id       : " + str(dataRobot.robot_id[1]),
        "kompas_value   : " + str(dataRobot.kompas_value[1]),
        "xpos           : " + str(dataRobot.xpos[1]),
        "ypos           : " + str(dataRobot.ypos[1]),
        "ball_value     : " + str(dataRobot.ball_value[1]),
        # "ball_distance: " + str(dataRobot.ball_distance[1]),
        "status_robot   : " + str(dataRobot.status_robot[1]),
        "enemy1_value   : " + str(dataRobot.enemy1[1]),
        "enemy2_value   : " + str(dataRobot.enemy2[1]),
        "enemy3_value   : " + str(dataRobot.enemy3[1]),
        "catch_ball     : " + str(dataRobot.catch_ball[1]),
        "dummy 2        : " + str(varGlobals.index_B)
        ]

        textsStriker = [
        "robot_id       : " + str(dataRobot.robot_id[2]),
        "kompas_value   : " + str(dataRobot.kompas_value[2]),
        "xpos           : " + str(dataRobot.xpos[2]),
        "ypos           : " + str(dataRobot.ypos[2]),
        "ball_value     : " + str(dataRobot.ball_value[2]),
        # "ball_distance: " + str(dataRobot.ball_distance[2]),
        "status_robot   : " + str(dataRobot.status_robot[2]),
        "enemy1_value   : " + str(dataRobot.enemy1[2]),
        "enemy2_value   : " + str(dataRobot.enemy2[2]),
        "enemy3_value   : " + str(dataRobot.enemy3[2]),
        "catch_ball     : " + str(dataRobot.catch_ball[2]),
        "dummy 1        : " + str(varGlobals.index_A)
        ]

        # tinggi total konten
        content_total_height = len(textsKiper) * int(varGlobals.res[0]/50)

        varGlobals.screen.blit(varGlobals.bgSim,(0,0))
        varGlobals.screen.blit(varGlobals.lapanganBawah, (varGlobals.offsetX-varGlobals.offsetResetPosX,varGlobals.offsetY-varGlobals.offsetResetPosY))
        varGlobals.screen.blit(varGlobals.lapangan, (varGlobals.offsetX,varGlobals.offsetY))
        gambar_grid()

        #####################################################################################################################################
        #####################################################################################################################################
        #####################################################################################################################################
        
        # SIMULASI ROBOT
        if varGlobals.cyan:                                                                                                                         
            draw_rotated_image(varGlobals.kiperCyan,                    
                               (varGlobals.offsetX+(dataRobot.ypos[0]*varGlobals.skala)-varGlobals.offsetResetPosX),                    
                               (varGlobals.offsetY+(dataRobot.xpos[0]*varGlobals.skala)-varGlobals.offsetResetPosY),                    
                               dataRobot.kompas_value[0])                   

            draw_rotated_image(varGlobals.backCyan,                 
                               (varGlobals.offsetX+(dataRobot.ypos[1]*varGlobals.skala)-varGlobals.offsetResetPosX),                    
                               (varGlobals.offsetY+(dataRobot.xpos[1]*varGlobals.skala)-varGlobals.offsetResetPosY),                    
                               dataRobot.kompas_value[1])                   

            draw_rotated_image(varGlobals.strikerCyan,                  
                               (varGlobals.offsetX+(dataRobot.ypos[2]*varGlobals.skala)-varGlobals.offsetResetPosX),                    
                               (varGlobals.offsetY+(dataRobot.xpos[2]*varGlobals.skala)-varGlobals.offsetResetPosY),                    
                               dataRobot.kompas_value[2])

            # drawGoalPositionRandom((varGlobals.offsetX+(dataRobot.ypos[1]*varGlobals.skala)-varGlobals.offsetResetPosX),                  
            #                     (varGlobals.offsetY+(dataRobot.xpos[1]*varGlobals.skala)-varGlobals.offsetResetPosY),                     
            #                     dataRobot.kompas_value[1])                    

            # drawGoalPositionRandom((varGlobals.offsetX+(dataRobot.ypos[2]*varGlobals.skala)-varGlobals.offsetResetPosX),                  
            #                    (varGlobals.offsetY+(dataRobot.xpos[2]*varGlobals.skala)-varGlobals.offsetResetPosY),                  
            #                     dataRobot.kompas_value[2])                    

            # shortestPath((varGlobals.offsetX+(dataRobot.ypos[1]*varGlobals.skala)-varGlobals.offsetResetPosX),                    
            # (varGlobals.offsetY+(dataRobot.xpos[1]*varGlobals.skala)-varGlobals.offsetResetPosY),1,1)

        #####################################################################################################################################
        #####################################################################################################################################
        #####################################################################################################################################

        elif varGlobals.magenta:
            draw_rotated_image(varGlobals.kiperMagenta,
                               (varGlobals.offsetX+(dataRobot.ypos[0]*varGlobals.skala)-varGlobals.offsetResetPosX), 
                               (varGlobals.offsetY+(dataRobot.xpos[0]*varGlobals.skala)-varGlobals.offsetResetPosY), 
                               dataRobot.kompas_value[0])
            
            draw_rotated_image(varGlobals.backMagenta,
                               (varGlobals.offsetX+(dataRobot.ypos[1]*varGlobals.skala)-varGlobals.offsetResetPosX), 
                               (varGlobals.offsetY+(dataRobot.xpos[1]*varGlobals.skala)-varGlobals.offsetResetPosY), 
                               dataRobot.kompas_value[1])
            
            draw_rotated_image(varGlobals.strikerMagenta,
                               (varGlobals.offsetX+(dataRobot.ypos[2]*varGlobals.skala)-varGlobals.offsetResetPosX), 
                               (varGlobals.offsetY+(dataRobot.xpos[2]*varGlobals.skala)-varGlobals.offsetResetPosY), 
                               dataRobot.kompas_value[2])
            
            # drawGoalPositionRandom((varGlobals.offsetX+(dataRobot.ypos[1]*varGlobals.skala)-varGlobals.offsetResetPosX), 
            #                     (varGlobals.offsetY+(dataRobot.xpos[1]*varGlobals.skala)-varGlobals.offsetResetPosY), 
            #                     dataRobot.kompas_value[1])
            
            # drawGoalPositionRandom((varGlobals.offsetX+(dataRobot.ypos[2]*varGlobals.skala)-varGlobals.offsetResetPosX), 
            #                    (varGlobals.offsetY+(dataRobot.xpos[2]*varGlobals.skala)-varGlobals.offsetResetPosY), 
            #                     dataRobot.kompas_value[2])
            
            # shortestPath((varGlobals.offsetX+(dataRobot.ypos[1]*varGlobals.skala)-varGlobals.offsetResetPosX),
            # (varGlobals.offsetY+(dataRobot.xpos[1]*varGlobals.skala)-varGlobals.offsetResetPosY),varGlobals.musuh3_x,varGlobals.musuh3_y)

        #####################################################################################################################################
        #####################################################################################################################################
        #####################################################################################################################################

        # MENGGAMBAR HEADING
        draw_rotated_image(varGlobals.headingKiper,
                           varGlobals.res[0]/15, 
                           varGlobals.res[1]/3.155,
                           dataRobot.kompas_value[0])
        
        draw_rotated_image(varGlobals.headingBack,
                           varGlobals.res[0]/15, 
                           varGlobals.res[1]/2.12,
                           dataRobot.kompas_value[1])
        
        draw_rotated_image(varGlobals.headingStriker,
                           varGlobals.res[0]/15, 
                           varGlobals.res[1]/1.595,
                           dataRobot.kompas_value[2])
        
        #####################################################################################################################################
        #####################################################################################################################################
        #####################################################################################################################################

        # DETEKSI KOORDINAT BOLA
        robo1_x = varGlobals.offsetX + (dataRobot.ypos[1] * varGlobals.skala) - varGlobals.offsetResetPosX
        robo1_y = varGlobals.offsetY + (dataRobot.xpos[1] * varGlobals.skala) - varGlobals.offsetResetPosY

        robo2_x = varGlobals.offsetX + (dataRobot.ypos[2] * varGlobals.skala) - varGlobals.offsetResetPosX
        robo2_y = varGlobals.offsetY + (dataRobot.xpos[2] * varGlobals.skala) - varGlobals.offsetResetPosY

        varGlobals.ball_x, varGlobals.ball_y = calculate_position(
            robo1_x, robo1_y, dataRobot.ball_value[1],  # Posisi & sudut bola dari robot 1
            robo2_x, robo2_y, dataRobot.ball_value[2]   # Posisi & sudut bola dari robot 2
        )
        
        if (((varGlobals.ball_x < varGlobals.offsetX + ((varGlobals.lapanganResX) * varGlobals.skala) and 
           varGlobals.ball_x > varGlobals.offsetX)) and 
           (varGlobals.ball_y < varGlobals.offsetY + ((varGlobals.lapanganResY) * varGlobals.skala) and 
           varGlobals.ball_y > varGlobals.offsetY)):
            
            bezierCurve(1, robo1_x, robo1_y, robo2_x, robo2_y, 50)
            draw_ball(varGlobals.ball_x, varGlobals.ball_y)
            draw_line_bola(robo1_x, robo1_y, varGlobals.ball_x, varGlobals.ball_y)
            draw_line_bola(robo2_x, robo2_y, varGlobals.ball_x, varGlobals.ball_y)

            # getBall = True
            # if getBall:
            #     send_robot(draw_line_bola)
                
            '''
            print("X_bola:")
            print(ball_x)
            print("Y_bola:")
            print(ball_y)
            '''

        #####################################################################################################################################
        #####################################################################################################################################
        #####################################################################################################################################

        # DETEKSI MUSUH 1
        varGlobals.musuh1_x, varGlobals.musuh1_y = calculate_position(
            robo1_x, robo1_y, dataRobot.enemy1[1],  # Posisi & sudut musuh dari robot 1
            robo2_x, robo2_y, dataRobot.enemy1[2]   # Posisi & sudut musuh dari robot 2
        )
        
        if (((varGlobals.musuh1_x < varGlobals.offsetX + ((varGlobals.lapanganResX) * varGlobals.skala) and 
           varGlobals.musuh1_x > varGlobals.offsetX)) and 
           (varGlobals.musuh1_y < varGlobals.offsetY + ((varGlobals.lapanganResY) * varGlobals.skala) and 
           varGlobals.musuh1_y > varGlobals.offsetY)):
            
            draw_musuh(varGlobals.musuh1_x, varGlobals.musuh1_y)
            draw_line_musuh(robo1_x, robo1_y, varGlobals.musuh1_x, varGlobals.musuh1_y)
            draw_line_musuh(robo2_x, robo2_y, varGlobals.musuh1_x, varGlobals.musuh1_y)
            
        #####################################################################################################################################
        #####################################################################################################################################
        #####################################################################################################################################

        # DETEKSI MUSUH 2
        varGlobals.musuh2_x, varGlobals.musuh2_y = calculate_position(
            robo1_x, robo1_y, dataRobot.enemy2[1],  # Posisi & sudut musuh dari robot 1
            robo2_x, robo2_y, dataRobot.enemy2[2]   # Posisi & sudut musuh dari robot 2
        )
        
        if (((varGlobals.musuh2_x < varGlobals.offsetX + ((varGlobals.lapanganResX) * varGlobals.skala) and 
           varGlobals.musuh2_x > varGlobals.offsetX)) and 
           (varGlobals.musuh2_y < varGlobals.offsetY + ((varGlobals.lapanganResY) * varGlobals.skala) and 
           varGlobals.musuh2_y > varGlobals.offsetY)):
            
            draw_musuh(varGlobals.musuh2_x, varGlobals.musuh2_y)
            draw_line_musuh(robo1_x, robo1_y, varGlobals.musuh2_x, varGlobals.musuh2_y)
            draw_line_musuh(robo2_x, robo2_y, varGlobals.musuh2_x, varGlobals.musuh2_y)
            
        #####################################################################################################################################
        #####################################################################################################################################
        #####################################################################################################################################

        # DETEKSI MUSUH 3  
        varGlobals.musuh3_x, varGlobals.musuh3_y = calculate_position(
            robo1_x, robo1_y, dataRobot.enemy3[1],  # Posisi & sudut musuh dari robot 1
            robo2_x, robo2_y, dataRobot.enemy3[2]   # Posisi & sudut musuh dari robot 2
        )
        
        if (((varGlobals.musuh3_x < varGlobals.offsetX + ((varGlobals.lapanganResX) * varGlobals.skala) and 
           varGlobals.musuh3_x > varGlobals.offsetX)) and 
           (varGlobals.musuh3_y < varGlobals.offsetY + ((varGlobals.lapanganResY) * varGlobals.skala) and 
           varGlobals.musuh3_y > varGlobals.offsetY)):
            
            draw_musuh(varGlobals.musuh3_x, varGlobals.musuh3_y)
            draw_line_musuh(robo1_x, robo1_y, varGlobals.musuh3_x, varGlobals.musuh3_y)
            draw_line_musuh(robo2_x, robo2_y, varGlobals.musuh3_x, varGlobals.musuh3_y)
            
        #####################################################################################################################################
        #####################################################################################################################################
        #####################################################################################################################################

        # DETEKSI TEMAN
        
        #####################################################################################################################################
        #####################################################################################################################################
        #####################################################################################################################################

        # JARAK ROBOT MUSUH
        sudut1_rad = math.radians(dataRobot.enemy1[1])
        sudut2_rad = math.radians(dataRobot.enemy1[2])

        m1 = math.sin(sudut1_rad)
        m2 = math.sin(sudut2_rad)

        c1 = dataRobot.ypos[1] - m1 * dataRobot.xpos[1]
        c2 = dataRobot.ypos[2] - m2 * dataRobot.xpos[2]

        if m1 != m2:
            x_potong = (c2 - c1) / (m1 - m2)
            y_potong = m1 * x_potong + c1

            jarak_robot_musuh1 = calculate_distance(dataRobot.xpos[1], dataRobot.ypos[1], x_potong, y_potong)
            jarak_robot_musuh2 = calculate_distance(dataRobot.xpos[2], dataRobot.ypos[2], x_potong, y_potong)
        else:
            jarak_robot_musuh1 = None
            jarak_robot_musuh2 = None

        varGlobals.jarak_musuh1 = jarak_robot_musuh1
        varGlobals.jarak_musuh2 = jarak_robot_musuh2

        #####################################################################################################################################
        #####################################################################################################################################
        #####################################################################################################################################

        # DECISION TREE
        json_filename = '/media/joan/Windows-SSD/Users/LENOVO/BASESTATION/modules/strategy.json'
        data = read_json(json_filename) 

        aksi = get_strategy(dataRobot.catch_ball[1], dataRobot.catch_ball[2])
        strategi = get_action(aksi, 
                              jarak_robot_musuh1,
                              jarak_robot_musuh2, 
                              dataRobot.ball_distance[1], 
                              dataRobot.enemy1[1], 
                              dataRobot.status_robot[1], 
                              dataRobot.catch_ball[1], 
                              dataRobot.catch_ball[2])
        varGlobals.CONFIG_DECISION_TREE = strategi

        # Cek perubahan strategi atau aksi
        # if strategi != varGlobals.last_strategy or aksi != varGlobals.last_action:
        #     print(f"Strategi : {varGlobals.CONFIG_DECISION_TREE}")
        #     print(f"Aksi : {aksi}")
        #     print(f"Jarak : {varGlobals.jarak_musuh1}")

        #     # Simpan strategi & aksi terakhir agar tidak nge-print terus
        #     varGlobals.last_strategy = strategi
        #     varGlobals.last_action = aksi

        # INISIALISASI TEXT DI SIMULATOR
        input_key_decision_tree = {varGlobals.CONFIG_DECISION_TREE:INP_CONFIG_DECISION_TREE}

        #####################################################################################################################################
        #####################################################################################################################################
        #####################################################################################################################################

        # REFBOX
        msg_refbox ={varGlobals.MESSAGE_REFBOX:MASSAGE}
        add_kiper = {varGlobals.conKiper:KIPER}
        add_back = {varGlobals.conBack:BACK}
        add_striker = {varGlobals.conStriker:STRIKER}

        #####################################################################################################################################
        #####################################################################################################################################
        #####################################################################################################################################

        # MENGGAMBAR DUMMY
        draw_dummy(posisi_dummy1[0], posisi_dummy1[1])
        draw_dummy(posisi_dummy2[0], posisi_dummy2[1])
        draw_dummy(posisi_dummy3[0], posisi_dummy3[1])

        #####################################################################################################################################
        #####################################################################################################################################
        #####################################################################################################################################

        #PROTEKSI LOOPING
        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                varGlobals.runConf = False
                varGlobals.runSim = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                click = True
                scrolling = False
                if checkboxCyan.collidepoint(event.pos):
                    checkboxCyan_clicked = not checkboxCyan_clicked
                    if checkboxCyan_clicked:
                        checkboxMagenta_clicked = False  # uncheck checkbox lainnya
                        varGlobals.cyan=True
                        varGlobals.magenta=False
                        print("cyan")
                elif checkboxMagenta.collidepoint(event.pos):
                    checkboxMagenta_clicked = not checkboxMagenta_clicked
                    if checkboxMagenta_clicked:
                        checkboxCyan_clicked = False  # uncheck checkbox lainnya
                        varGlobals.magenta=True
                        varGlobals.cyan=False
                        print("magenta")
                elif checkboxGridKiper.collidepoint(event.pos):
                    checboxGridKiper_clicked = not checboxGridKiper_clicked
                    if checboxGridKiper_clicked:
                        varGlobals.gridKiper = True
                        varGlobals.gridBack = False
                        varGlobals.gridStriker = False
                        varGlobals.wasdKiper = True
                        varGlobals.wasdBack = False
                        varGlobals.wasdStriker = False
                        print("gridKiper")
                elif checkboxGridBack.collidepoint(event.pos):
                    checkboxGridBack_clicked = not checkboxGridBack_clicked
                    if checkboxGridBack_clicked:
                        varGlobals.gridKiper = False
                        varGlobals.gridBack = True
                        varGlobals.gridStriker = False
                        varGlobals.wasdKiper = False
                        varGlobals.wasdBack = True
                        varGlobals.wasdStriker = False
                        print("gridBack")
                elif checkboxGridStriker.collidepoint(event.pos):
                    checkboxGridStriker_clicked = not checkboxGridStriker_clicked
                    if checkboxGridStriker_clicked:
                        varGlobals.gridKiper = False
                        varGlobals.gridBack = False
                        varGlobals.gridStriker = True
                        varGlobals.wasdKiper = False
                        varGlobals.wasdBack = False
                        varGlobals.wasdStriker = True
                        print("gridStriker")    
                        
            elif event.type == varGlobals.KEYDOWN:
                if event.key in keys:
                    keys[event.key] = True
            elif event.type == varGlobals.KEYUP:
                if event.key in keys:
                    keys[event.key] = False
                    

            # content_total_height = 50
            if event.type == pygame.MOUSEBUTTONDOWN :
                if event.button == 4:  # Scroll mouse ke atas
                    content_y += 30
                    content_y = min(0, content_y)  # Batas scroll ke atas
                elif event.button == 5:  # Scroll mouse ke bawah
                    content_y -= 30
                    content_y = max(-(content_total_height - frame_height), content_y)  # Batas scroll ke bawah
                    if event.button == 1:
                        scrolling = True
                        scrolling_pos = pygame.mouse.get_pos()
                        scrolling_offset = pygame.Vector2(content_x, content_y) - scrolling_pos

            # Mengatur scrolling saat mouse digerakkan
            elif event.type == pygame.MOUSEMOTION:
                if scrolling:
                    new_pos = pygame.mouse.get_pos()
                    content_x, content_y = (scrolling_offset + new_pos)
                    content_y = min(0, content_y)  # Batas scroll ke atas
                    content_y = max(-(content_total_height - frame_height), content_y)  # Batas scroll ke bawah

        #####################################################################################################################################
        #####################################################################################################################################
        #####################################################################################################################################

        mx, my = pygame.mouse.get_pos()
        #titik 1
        if click:
            if(mx>=450 and mx<=550 and my>=190 and my<=280):
                draw_setBall((varGlobals.offsetX+((250*varGlobals.skala)-varGlobals.offsetResetPosX)), 
                            (varGlobals.offsetY+((250*varGlobals.skala)-varGlobals.offsetResetPosY)))

                varGlobals.setBall_x = (varGlobals.offsetX+((250*varGlobals.skala)-varGlobals.offsetResetPosX))
                varGlobals.setBall_y = (varGlobals.offsetY+((250*varGlobals.skala)-varGlobals.offsetResetPosY))
            #titik 2
            elif(mx>=450 and mx<=550 and my>=370 and my<=460):
                draw_setBall((varGlobals.offsetX+((250*varGlobals.skala)-varGlobals.offsetResetPosX)), 
                            (varGlobals.offsetY+((450*varGlobals.skala)-varGlobals.offsetResetPosY)))

                varGlobals.setBall_x = (varGlobals.offsetX+((250*varGlobals.skala)-varGlobals.offsetResetPosX)) 
                varGlobals.setBall_y = (varGlobals.offsetY+((450*varGlobals.skala)-varGlobals.offsetResetPosY))
            #titik 3
            elif(mx>=450 and mx<=550 and my>=550 and my<=640):
                draw_setBall((varGlobals.offsetX+((250*varGlobals.skala)-varGlobals.offsetResetPosX)), 
                            (varGlobals.offsetY+((650*varGlobals.skala)-varGlobals.offsetResetPosY)))

                varGlobals.setBall_x = (varGlobals.offsetX+((250*varGlobals.skala)-varGlobals.offsetResetPosX))
                varGlobals.setBall_y = (varGlobals.offsetY+((650*varGlobals.skala)-varGlobals.offsetResetPosY))
            #titik 4
            elif(mx>=815 and mx<=900 and my>=190 and my<=280):
                draw_setBall((varGlobals.offsetX+((650*varGlobals.skala)-varGlobals.offsetResetPosX)), 
                            (varGlobals.offsetY+((250*varGlobals.skala)-varGlobals.offsetResetPosY)))
            
                varGlobals.setBall_x = (varGlobals.offsetX+((650*varGlobals.skala)-varGlobals.offsetResetPosX))
                varGlobals.setBall_y = (varGlobals.offsetY+((250*varGlobals.skala)-varGlobals.offsetResetPosY))
            #titik 5
            elif(mx>=815 and mx<=900 and my>=550 and my<=640):
                draw_setBall((varGlobals.offsetX+((650*varGlobals.skala)-varGlobals.offsetResetPosX)), 
                            (varGlobals.offsetY+((650*varGlobals.skala)-varGlobals.offsetResetPosY)))
            
                varGlobals.setBall_x = (varGlobals.offsetX+((650*varGlobals.skala)-varGlobals.offsetResetPosX))
                varGlobals.setBall_y = (varGlobals.offsetY+((650*varGlobals.skala)-varGlobals.offsetResetPosY))
            #titik 6
            elif(mx>=1180 and mx<=1270 and my>=190 and my<=280):
                draw_setBall((varGlobals.offsetX+((1050*varGlobals.skala)-varGlobals.offsetResetPosX)), 
                            (varGlobals.offsetY+((250*varGlobals.skala)-varGlobals.offsetResetPosY)))
            
                varGlobals.setBall_x = (varGlobals.offsetX+((1050*varGlobals.skala)-varGlobals.offsetResetPosX)) 
                varGlobals.setBall_y = (varGlobals.offsetY+((250*varGlobals.skala)-varGlobals.offsetResetPosY))
            #titik 7
            elif(mx>=1180 and mx<=1270 and my>=370 and my<=460):
                draw_setBall((varGlobals.offsetX+((1050*varGlobals.skala)-varGlobals.offsetResetPosX)), 
                            (varGlobals.offsetY+((450*varGlobals.skala)-varGlobals.offsetResetPosY)))
            
                varGlobals.setBall_x = (varGlobals.offsetX+((1050*varGlobals.skala)-varGlobals.offsetResetPosX))
                varGlobals.setBall_y = (varGlobals.offsetY+((450*varGlobals.skala)-varGlobals.offsetResetPosY))
            #titik 8
            elif(mx>=1180 and mx<=1270 and my>=550 and my<=640):
                draw_setBall((varGlobals.offsetX+((1050*varGlobals.skala)-varGlobals.offsetResetPosX)), 
                            (varGlobals.offsetY+((650*varGlobals.skala)-varGlobals.offsetResetPosY)))

                varGlobals.setBall_x = (varGlobals.offsetX+((1050*varGlobals.skala)-varGlobals.offsetResetPosX)) 
                varGlobals.setBall_y = (varGlobals.offsetY+((650*varGlobals.skala)-varGlobals.offsetResetPosY))
            #titik musuh corner atas
            elif(mx>=1313 and mx<=1400 and my>=55 and my<=140):
                draw_setBall((varGlobals.offsetX+((1250*varGlobals.skala)-varGlobals.offsetResetPosX)), 
                            (varGlobals.offsetY+((50*varGlobals.skala)-varGlobals.offsetResetPosY)))
                
                varGlobals.setBall_x = (varGlobals.offsetX+((1250*varGlobals.skala)-varGlobals.offsetResetPosX)) 
                varGlobals.setBall_y = (varGlobals.offsetY+((50*varGlobals.skala)-varGlobals.offsetResetPosY))
            #titik musuh corner bawah
            elif(mx>=1313 and mx<=1400 and my>=684 and my<=772):
                draw_setBall((varGlobals.offsetX+((1250*varGlobals.skala)-varGlobals.offsetResetPosX)), 
                            (varGlobals.offsetY+((850*varGlobals.skala)-varGlobals.offsetResetPosY)))
                
                varGlobals.setBall_x = (varGlobals.offsetX+((1250*varGlobals.skala)-varGlobals.offsetResetPosX)) 
                varGlobals.setBall_y = (varGlobals.offsetY+((850*varGlobals.skala)-varGlobals.offsetResetPosY))
            #titik kawan corner atas
            elif(mx>=320 and mx<=410 and my>=55 and my<=150):
                draw_setBall((varGlobals.offsetX+((50*varGlobals.skala)-varGlobals.offsetResetPosX)), 
                            (varGlobals.offsetY+((50*varGlobals.skala)-varGlobals.offsetResetPosY)))
                
                varGlobals.setBall_x = (varGlobals.offsetX+((50*varGlobals.skala)-varGlobals.offsetResetPosX)) 
                varGlobals.setBall_y = (varGlobals.offsetY+((50*varGlobals.skala)-varGlobals.offsetResetPosY))
            #titik kawan corner bawah
            elif(mx>=320 and mx<=410 and my>=685 and my<=775):
                draw_setBall((varGlobals.offsetX+((50*varGlobals.skala)-varGlobals.offsetResetPosX)), 
                            (varGlobals.offsetY+((850*varGlobals.skala)-varGlobals.offsetResetPosY)))
                
                varGlobals.setBall_x = (varGlobals.offsetX+((50*varGlobals.skala)-varGlobals.offsetResetPosX)) 
                varGlobals.setBall_y = (varGlobals.offsetY+((850*varGlobals.skala)-varGlobals.offsetResetPosY))
            else:
                draw_setBall(-100,-100)

        #if (mx+varGlobals.offsetResetPosX)
        # print("mx= ",int(varGlobals.setBall_x))
        # print("my=", int(varGlobals.setBall_y))

        #####################################################################################################################################
        #####################################################################################################################################
        #####################################################################################################################################
        
        # UNTUK BUTTON MENU
        for button in buttons:
            if buttons[button].collidepoint(mx, my):
                pygame.draw.rect(varGlobals.screen, cc.FTEK, buttons[button], 3, border_radius=50)
                if click:
                    button_action(button)
            else:
                pygame.draw.rect(varGlobals.screen, cc.BLUE_STONE, buttons[button], 3, border_radius=50)
            tts(varGlobals.screen, 
                button, 
                buttons[button].centerx, 
                buttons[button].centery, 
                int(varGlobals.res[0]/90), 
                color=cc.WHITE)

        #####################################################################################################################################
        #####################################################################################################################################
        #####################################################################################################################################

        # STATUS CONNECT/DISCONNECT DAN PESAN DARI REFBOX
        for msg_ref in  msg_refbox:
            if msg_ref=="DISCONNECTED" or msg_ref=="CONNECT AGAIN":
                pygame.draw.rect(varGlobals.screen, cc.RED, msg_refbox[msg_ref], border_radius=20)
            elif msg_ref=="WELCOME":
                pygame.draw.rect(varGlobals.screen, cc.SKY_BLUE, msg_refbox[msg_ref], border_radius=20)
            else:
                pygame.draw.rect(varGlobals.screen, cc.WHITE, msg_refbox[msg_ref], border_radius=20)
            
            tts(varGlobals.screen,
                varGlobals.MESSAGE_REFBOX,
                msg_refbox[msg_ref].centerx,
                msg_refbox[msg_ref].centery,
                int(varGlobals.res[0]/100),
                cc.BLACK)
            
        #####################################################################################################################################
        #####################################################################################################################################
        #####################################################################################################################################    

        # PROTEKSI KETIKA REFBOX MELAKUKAN GAME RESET
        if varGlobals.ref and varGlobals.MESSAGE_REFBOX=="GAME RESET":
            varGlobals.ref=False
            pygame.draw.rect(varGlobals.screen,cc.GRASS_GREEN, MASSAGE, border_radius=20)
            
            tts(varGlobals.screen,
                varGlobals.MESSAGE_REFBOX,
                msg_refbox[msg_ref].centerx,
                msg_refbox[msg_ref].centery,
                int(varGlobals.res[0]/100),
                cc.BLACK)
            
            pygame.display.flip()
            time.sleep(3)
            # connect_refbox()

        #####################################################################################################################################
        #####################################################################################################################################\
        #####################################################################################################################################

        #STATUS CONNECT/DISCONNECT ROBOT BACK
        for txtBack in add_back:
            if varGlobals.back:
                pygame.draw.rect(varGlobals.screen, cc.SKY_BLUE, add_back[txtBack], border_radius=20)
                
                tts(varGlobals.screen,
                    varGlobals.conBack,
                    add_back[txtBack].centerx,
                    add_back[txtBack].centery,
                    int(varGlobals.res[0]/100),
                    cc.BLACK)
            else:
                pygame.draw.rect(varGlobals.screen, cc.RED, add_back[txtBack], border_radius=20)
                
                tts(varGlobals.screen,
                    varGlobals.conBack,
                    add_back[txtBack].centerx,
                    add_back[txtBack].centery,
                    int(varGlobals.res[0]/110),
                    cc.BLACK)
                
        #####################################################################################################################################
        #####################################################################################################################################
        #####################################################################################################################################

        #STATUS CONNECT/DISCONNECT ROBOT STRIKER
        for txtStriker in add_striker:
            if varGlobals.striker:
                pygame.draw.rect(varGlobals.screen, cc.SKY_BLUE, add_striker[txtStriker], border_radius=20)
                
                tts(varGlobals.screen,
                    varGlobals.conStriker,
                    add_striker[txtStriker].centerx,
                    add_striker[txtStriker].centery,
                    int(varGlobals.res[0]/100),
                    cc.BLACK)
                
            else:
                pygame.draw.rect(varGlobals.screen, cc.RED, add_striker[txtStriker], border_radius=20)
                
                tts(varGlobals.screen,
                    varGlobals.conStriker,
                    add_striker[txtStriker].centerx,
                    add_striker[txtStriker].centery,
                    int(varGlobals.res[0]/110),
                    cc.BLACK)
                
        #####################################################################################################################################
        #####################################################################################################################################
        #####################################################################################################################################

        #STATUS CONNECT/DISCONNECT ROBOT KIPER
        for txtKiper in add_kiper:
            if varGlobals.kiper:
                pygame.draw.rect(varGlobals.screen, cc.SKY_BLUE, add_kiper[txtKiper], border_radius=20)
                
                tts(varGlobals.screen,
                    varGlobals.conKiper,
                    add_kiper[txtKiper].centerx,
                    add_kiper[txtKiper].centery,
                    int(varGlobals.res[0]/100),
                    cc.BLACK)
                
            else:
                pygame.draw.rect(varGlobals.screen, cc.RED, add_kiper[txtKiper], border_radius=20)
                
                tts(varGlobals.screen,
                    varGlobals.conKiper,
                    add_kiper[txtKiper].centerx,
                    add_kiper[txtKiper].centery,
                    int(varGlobals.res[0]/110),
                    cc.BLACK)
        
        #####################################################################################################################################
        #####################################################################################################################################
        #####################################################################################################################################

        #INPUT TEXT
        mx, my = pygame.mouse.get_pos()
        if varGlobals.magenta == True or varGlobals.cyan == True:
            for text in input_key_striker_grid_x:
                if input_key_striker_grid_x[text].collidepoint(mx,my):
                    varGlobals.CONFIG_STRIKER_GRID_X = ''
                    pygame.draw.rect(varGlobals.screen, 
                                    cc.GRAY, 
                                    input_key_striker_grid_x[text], 
                                    border_radius=20)
                    if click:
                        textActionStrikerGridX(text,input_key_striker_grid_x)
                else:
                    pygame.draw.rect(varGlobals.screen, 
                                    cc.WHITE, input_key_striker_grid_x[text], 
                                    border_radius=20)
                tts(varGlobals.screen,
                    text,
                    input_key_striker_grid_x[text].centerx,
                    input_key_striker_grid_x[text].centery,
                    int(varGlobals.res[0]/65),
                    cc.BLACK)
            for text in input_key_striker_grid_y:
                if input_key_striker_grid_y[text].collidepoint(mx,my):
                    varGlobals.CONFIG_STRIKER_GRID_Y = ''
                    pygame.draw.rect(varGlobals.screen, 
                                    cc.GRAY, 
                                    input_key_striker_grid_y[text], 
                                    border_radius=20)
                    if click:
                        textActionStrikerGridY(text,input_key_striker_grid_y)
                else:
                    pygame.draw.rect(varGlobals.screen, 
                                    cc.WHITE, input_key_striker_grid_y[text], 
                                    border_radius=20)
                tts(varGlobals.screen,
                    text,
                    input_key_striker_grid_y[text].centerx,
                    input_key_striker_grid_y[text].centery,
                    int(varGlobals.res[0]/65),
                    cc.BLACK)
                
            for text in input_key_back_grid_x:
                if input_key_back_grid_x[text].collidepoint(mx,my):
                    varGlobals.CONFIG_BACK_GRID_X = ''
                    pygame.draw.rect(varGlobals.screen, 
                                    cc.GRAY, 
                                    input_key_back_grid_x[text], 
                                    border_radius=20)
                    if click:
                        textActionBackGridX(text,input_key_back_grid_x)
                        
                else:
                    pygame.draw.rect(varGlobals.screen, 
                                    cc.WHITE, input_key_back_grid_x[text], 
                                    border_radius=20)
                tts(varGlobals.screen,
                    text,
                    input_key_back_grid_x[text].centerx,
                    input_key_back_grid_x[text].centery,
                    int(varGlobals.res[0]/65),
                    cc.BLACK)
            for text in input_key_back_grid_y:
                if input_key_back_grid_y[text].collidepoint(mx,my):
                    varGlobals.CONFIG_BACK_GRID_Y = ''
                    pygame.draw.rect(varGlobals.screen, 
                                    cc.GRAY, 
                                    input_key_back_grid_y[text], 
                                    border_radius=20)
                    if click:
                        textActionBackGridY(text,input_key_back_grid_y)
                else:
                    pygame.draw.rect(varGlobals.screen, 
                                    cc.WHITE, input_key_back_grid_y[text], 
                                    border_radius=20)
                tts(varGlobals.screen,
                    text,
                    input_key_back_grid_y[text].centerx,
                    input_key_back_grid_y[text].centery,
                    int(varGlobals.res[0]/65),
                    cc.BLACK)
                
            for text in input_key_decision_tree:
                pygame.draw.rect(varGlobals.screen, 
                                cc.WHITE, input_key_decision_tree[text], 
                                border_radius=20)
                tts(varGlobals.screen,
                    text,
                    input_key_decision_tree[text].centerx,
                    input_key_decision_tree[text].centery,
                    int(varGlobals.res[0]/115),
                    cc.BLACK)

        frame_striker.fill(cc.WHITE)
        frame_back.fill(cc.WHITE)
        frame_kiper.fill(cc.WHITE)
        pygame.draw.rect(frame_striker, frame_color, frame_rect, frame_thickness,border_radius=20)
        pygame.draw.rect(frame_back, frame_color, frame_rect, frame_thickness,border_radius=20)
        pygame.draw.rect(frame_kiper, frame_color, frame_rect, frame_thickness,border_radius=20)

        #####################################################################################################################################
        #####################################################################################################################################
        #####################################################################################################################################
        
        # menambahkan teks pada frame_striker
        for i, text in enumerate(textsStriker):
            text_surface = text_font.render(text, True, text_color)
            text_rect = text_surface.get_rect()
            text_rect.topleft = (0, i * int(varGlobals.res[0]/60) + content_y)
            frame_striker.blit(text_surface, text_rect)
        
        for i, text in enumerate(textsBack):
            text_surface = text_font.render(text, True, text_color)
            text_rect = text_surface.get_rect()
            text_rect.topleft = (0, i * int(varGlobals.res[0]/60) + content_y)
            frame_back.blit(text_surface, text_rect)
    
        for i, text in enumerate(textsKiper):
            text_surface = text_font.render(text, True, text_color)
            text_rect = text_surface.get_rect()
            text_rect.topleft = (0, i * int(varGlobals.res[0]/60) + content_y)
            frame_kiper.blit(text_surface, text_rect)

        #####################################################################################################################################
        #####################################################################################################################################
        #####################################################################################################################################

        # MENGGAMBAR FRAME (DI BAWAH STATUS DISCONECT ROBOT)
        varGlobals.screen.blit(frame_striker, 
                               ((window_rect.centerx - frame_width * 1.16), 
                               window_rect.centery + frame_height * 2.23))
        
        varGlobals.screen.blit(frame_back, 
                               ((window_rect.centerx + frame_width * 0.34), 
                               window_rect.centery + frame_height * 2.23))
        
        varGlobals.screen.blit(frame_kiper, 
                               ((window_rect.centerx + frame_width * 1.81), 
                               window_rect.centery + frame_height * 2.23))

        pygame.draw.circle(varGlobals.screen, 
                           cc.BLACK, 
                           checkboxCyan.center, 
                           checkboxCyan.width // 2, 2)
        pygame.draw.circle(varGlobals.screen, 
                           cc.BLACK, 
                           checkboxMagenta.center, 
                           checkboxMagenta.width // 2, 2)
        pygame.draw.circle(varGlobals.screen, 
                            cc.BLACK, 
                            checkboxGridKiper.center, 
                            checkboxGridKiper.width // 2 ,2)
        pygame.draw.circle(varGlobals.screen, 
                            cc.BLACK, 
                            checkboxGridBack.center, 
                            checkboxGridBack.width // 2 ,2)
        pygame.draw.circle(varGlobals.screen, 
                            cc.BLACK, 
                            checkboxGridStriker.center, 
                            checkboxGridStriker.width // 2 ,2)
        
        if varGlobals.cyan==True:
            pygame.draw.circle(varGlobals.screen, 
                               cc.BLACK, 
                               checkboxCyan.center, 
                               checkboxCyan.width // 2 - 6)

        if varGlobals.magenta==True:
           pygame.draw.circle(varGlobals.screen, 
                              cc.BLACK, 
                              checkboxMagenta.center, 
                              checkboxMagenta.width // 2 - 6)
        
        if varGlobals.gridKiper==True:
           pygame.draw.circle(varGlobals.screen, 
                              cc.BLACK, 
                              checkboxGridKiper.center, 
                              checkboxGridKiper.width // 2 - 6)
           varGlobals.wasdKiper = True
        
        if varGlobals.gridBack==True:
            pygame.draw.circle(varGlobals.screen, 
                              cc.BLACK, 
                              checkboxGridBack.center, 
                              checkboxGridBack.width // 2 - 6)
            varGlobals.wasdBack = True
        
        if varGlobals.gridStriker==True:
            pygame.draw.circle(varGlobals.screen, 
                              cc.BLACK, 
                              checkboxGridStriker.center, 
                              checkboxGridStriker.width // 2 - 6)
            varGlobals.wasdStriker = True
        
        data=bytearray(3)
        keys = pygame.key.get_pressed()

        for key in varGlobals.key_pressed.keys():
            if keys[key] and not varGlobals.key_pressed[key]:
                print(f"{pygame.key.name(key)} pressed")
                if (pygame.key.name(key)=="down"):
                    for i in range (5):
                        if(varGlobals.wasdKiper == True):
                            data[0]=0
                        elif(varGlobals.wasdBack == True):
                            data[0]=1
                        elif(varGlobals.wasdStriker == True):
                            data[0]=2
                        data[1]=252
                        data[2]=123
                        send_robot(data)
                        print(data[0],data[1],data[2])
                else :
                    for i in range (5):
                        if(varGlobals.wasdKiper == True):
                            data[0]=0
                        elif(varGlobals.wasdBack == True):
                            data[0]=1
                        elif(varGlobals.wasdStriker == True):
                            data[0]=2
                        data[1]=252
                        data[2]=ord(pygame.key.name(key)[0])
                        send_robot(data)
                varGlobals.key_pressed[key] = True
                print(data[0],data[1],data[2])

            elif not keys[key] and varGlobals.key_pressed[key]:
                print(f"{pygame.key.name(key)} released")
                if(varGlobals.wasdKiper == True):
                    data[0]=0
                elif(varGlobals.wasdBack == True):
                    data[0]=1
                elif(varGlobals.wasdStriker == True):
                    data[0]=2
                data[1]=252
                data[2]=90
                for i in range (5):
                    send_robot(data)
                varGlobals.key_pressed[key] = False
                print(data[0],data[1],data[2])

        # pygame.display.update()
        click=False
        pygame.display.flip()
        varGlobals.clock.tick(60)

###############################################################################################################################################################################################
###############################################################################################################################################################################################
###############################################################################################################################################################################################

mainMenu()


