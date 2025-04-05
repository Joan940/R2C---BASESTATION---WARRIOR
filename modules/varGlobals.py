import pygame
import os,sys
from pygame.locals import KEYDOWN, KEYUP, K_q,K_e,K_z,K_c, K_w, K_a, K_s, K_d, K_UP, K_DOWN, K_LEFT, K_RIGHT,K_k,K_l,K_1,K_2


if sys.platform in ["win32", "win64"]: os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.init()
clock = pygame.time.Clock()

os.environ['SDL_VIDEO_CENTERED']='1'
info = pygame.display.Info()
screen_width,screen_height = info.current_w, info.current_h
res = (screen_width,screen_height)
# res = (1280,720)

screen =pygame.display.set_mode(res)
print(int(screen_width),int(screen_height))

IP = ''
PORT_IP = ''
ADDRESS = ''
PORT_ADD = ''
MESSAGE_REFBOX = ''
TEAM_IP = ''

CONFIG_KIPER_GRID_X = ''
CONFIG_KIPER_GRID_Y = ''
CONFIG_BACK_GRID_X = '8'
CONFIG_BACK_GRID_Y = '8'
CONFIG_STRIKER_GRID_X = '14'
CONFIG_STRIKER_GRID_Y = '8'

RESET_KIPER_GRID_X = ''
RESET_KIPER_GRID_Y = ''
RESET_BACK_GRID_X = ''
RESET_BACK_GRID_Y = ''
RESET_STRIKER_GRID_X = ''
RESET_STRIKER_GRID_Y = ''

KICKOFFKANAN = bool
KICKOFFKIRI = bool
CORNERKANAN = bool
CORNERKIRI = bool

ref=bool
udp=bool
runMenu = bool
runConf = bool
runSim = bool

CONNECT= ''
BIND = ''
conKiper = '' 
conBack = '' 
conStriker = '' 
refbox=''

kiper = bool
back = bool
striker = bool
newMsgRef=bool

cyan=bool
magenta=bool

gridKiper =bool
gridStriker = bool
gridBack = bool
wasdKiper = bool
wasdStriker = bool
wasdBack = bool

runLariTeam = bool
runLariMusuh = bool

runKickoffKanan = bool
runKickoffKiri = bool

runFreeKickTeam = bool
runFreeKickMusuh = bool

runGoalKickTeam = bool
runGoalKickMusuh = bool

runThrowInTeam = bool
runThrowInMusuh = bool

runCornerTeam = bool
runCornerMusuh = bool

runPenaltyTeam = bool
runPenaltyMusuh = bool

runKickoffKanan = bool
runKickoffKiri = bool

runCornerKanan = bool
runCornerKiri = bool

stop = bool
start = bool
dropBall = bool
park = bool
endPart = bool

diluarRadius= bool

key_pressed = {
    K_w: False,
    K_a: False,
    K_s: False,
    K_d: False,
    K_q: False,
    K_e: False,
    K_k: False,
    K_l: False,
    K_z: False,
    K_c: False,
    K_UP: False,
    K_DOWN: False,
    K_LEFT: False,
    K_RIGHT: False,
    K_1: False,
    K_2: False
}

index_A = 1
index_B = 1
index_C = 1

CONFIG_DECISION_TREE = ''
last_strategy = None
last_action = None

updateDummy = True
goalPosition = False
terimaData = False

lapanganResX= 1200
lapanganResY= 800
lapanganBawahResX= 1300
lapanganBawahResY= 900

gridRes= 50

robotResX=50
robotResY=50
headingResX=100
headingResY=100

offsetX= res[0]/6
offsetY= res[1]/20
skala = res[1]/1200

offsetResetPosX = 50*skala
offsetResetPosY = 50*skala

ball_x = None 
ball_y = None

setBall_x = 0
setBall_y = 0

musuh1_x = None
musuh1_y = None

musuh2_x = None
musuh2_y = None

musuh3_x = None
musuh3_y = None

lapangan = pygame.image.load("/home/joan/Downloads/BASESTATION - R2C - WARRIOR (coba)/assets/lapangan.png").convert_alpha()
lapangan = pygame.transform.scale(lapangan, (lapanganResX*skala,lapanganResY*skala))

lapanganBawah = pygame.image.load("/home/joan/Downloads/BASESTATION - R2C - WARRIOR (coba)/assets/lapanganBawah.png").convert_alpha()
lapanganBawah = pygame.transform.scale(lapanganBawah, (lapanganBawahResX*skala,lapanganBawahResY*skala))

kiperCyan = pygame.image.load("/home/joan/Downloads/BASESTATION - R2C - WARRIOR (coba)/assets/kiperCyan.png").convert_alpha()
kiperCyan = pygame.transform.scale(kiperCyan,(robotResX*skala,robotResY*skala))

backCyan = pygame.image.load("/home/joan/Downloads/BASESTATION - R2C - WARRIOR (coba)/assets/backCyan.png").convert_alpha()
backCyan = pygame.transform.scale(backCyan,(robotResX*skala,robotResY*skala))

strikerCyan = pygame.image.load("/home/joan/Downloads/BASESTATION - R2C - WARRIOR (coba)/assets/strikerCyan.png").convert_alpha()
strikerCyan = pygame.transform.scale(strikerCyan,(robotResX*skala,robotResY*skala))

kiperMagenta = pygame.image.load("/home/joan/Downloads/BASESTATION - R2C - WARRIOR (coba)/assets/kiperMagenta.png").convert_alpha()
kiperMagenta = pygame.transform.scale(kiperMagenta,(robotResX*skala,robotResY*skala))

backMagenta = pygame.image.load("/home/joan/Downloads/BASESTATION - R2C - WARRIOR (coba)/assets/backMagenta.png").convert_alpha()
backMagenta = pygame.transform.scale(backMagenta,(robotResX*skala,robotResY*skala))

strikerMagenta = pygame.image.load("/home/joan/Downloads/BASESTATION - R2C - WARRIOR (coba)/assets/strikerMagenta.png").convert_alpha()
strikerMagenta = pygame.transform.scale(strikerMagenta,(robotResX*skala,robotResY*skala))

headingKiper = pygame.image.load("/home/joan/Downloads/BASESTATION - R2C - WARRIOR (coba)/assets/headingKiper.png").convert_alpha()
headingKiper = pygame.transform.scale(headingKiper,(headingResX*skala,headingResY*skala))

headingBack = pygame.image.load("/home/joan/Downloads/BASESTATION - R2C - WARRIOR (coba)/assets/headingBack.png").convert_alpha()
headingBack = pygame.transform.scale(headingBack,(headingResX*skala,headingResY*skala))

headingStriker = pygame.image.load("/home/joan/Downloads/BASESTATION - R2C - WARRIOR (coba)/assets/headingStriker.png").convert_alpha()
headingStriker = pygame.transform.scale(headingStriker,(headingResX*skala,headingResY*skala))

musuhCyan = pygame.image.load("/home/joan/Downloads/BASESTATION - R2C - WARRIOR (coba)/assets/musuhCyan.png").convert_alpha()
musuhCyan = pygame.transform.scale(musuhCyan,(robotResX*skala,robotResY*skala))

musuhMagenta = pygame.image.load("/home/joan/Downloads/BASESTATION - R2C - WARRIOR (coba)/assets/musuhMagenta.png").convert_alpha()
musuhMagenta = pygame.transform.scale(musuhMagenta,(robotResX*skala,robotResY*skala))

bgMenu = pygame.image.load("/home/joan/Downloads/BASESTATION - R2C - WARRIOR (coba)/assets/R2C WARRIOR.png").convert_alpha()
bgMenu = pygame.transform.scale(bgMenu, res)

bgConf = pygame.image.load("/home/joan/Downloads/BASESTATION - R2C - WARRIOR (coba)/assets/bgConf.png").convert_alpha()
bgConf = pygame.transform.scale(bgConf, res)

bgSim = pygame.image.load("/home/joan/Downloads/bgSim.png").convert_alpha()
bgSim = pygame.transform.scale(bgSim, res)


#########################################################################################################################################

# lapangan = pygame.image.load("C:/Users/LENOVO/BASESTATION - R2C - WARRIOR (coba)/assets/lapangan.png").convert_alpha()
# lapangan = pygame.transform.scale(lapangan, (lapanganResX*skala,lapanganResY*skala))

# lapanganBawah = pygame.image.load("C:/Users/LENOVO/BASESTATION - R2C - WARRIOR (coba)/assets/lapanganBawah.png").convert_alpha()
# lapanganBawah = pygame.transform.scale(lapanganBawah, (lapanganBawahResX*skala,lapanganBawahResY*skala))

# kiperCyan = pygame.image.load("C:/Users/LENOVO/BASESTATION - R2C - WARRIOR (coba)/assets/kiperCyan.png").convert_alpha()
# kiperCyan = pygame.transform.scale(kiperCyan,(robotResX*skala,robotResY*skala))

# backCyan = pygame.image.load("C:/Users/LENOVO/BASESTATION - R2C - WARRIOR (coba)/assets/backCyan.png").convert_alpha()
# backCyan = pygame.transform.scale(backCyan,(robotResX*skala,robotResY*skala))

# strikerCyan = pygame.image.load("C:/Users/LENOVO/BASESTATION - R2C - WARRIOR (coba)/assets/strikerCyan.png").convert_alpha()
# strikerCyan = pygame.transform.scale(strikerCyan,(robotResX*skala,robotResY*skala))

# kiperMagenta = pygame.image.load("C:/Users/LENOVO/BASESTATION - R2C - WARRIOR (coba)/assets/kiperMagenta.png").convert_alpha()
# kiperMagenta = pygame.transform.scale(kiperMagenta,(robotResX*skala,robotResY*skala))

# backMagenta = pygame.image.load("C:/Users/LENOVO/BASESTATION - R2C - WARRIOR (coba)/assets/backMagenta.png").convert_alpha()
# backMagenta = pygame.transform.scale(backMagenta,(robotResX*skala,robotResY*skala))

# strikerMagenta = pygame.image.load("C:/Users/LENOVO/BASESTATION - R2C - WARRIOR (coba)/assets/strikerMagenta.png").convert_alpha()
# strikerMagenta = pygame.transform.scale(strikerMagenta,(robotResX*skala,robotResY*skala))

# headingKiper = pygame.image.load("C:/Users/LENOVO/BASESTATION - R2C - WARRIOR (coba)/assets/headingKiper.png").convert_alpha()
# headingKiper = pygame.transform.scale(headingKiper,(headingResX*skala,headingResY*skala))

# headingBack = pygame.image.load("C:/Users/LENOVO/BASESTATION - R2C - WARRIOR (coba)/assets/headingBack.png").convert_alpha()
# headingBack = pygame.transform.scale(headingBack,(headingResX*skala,headingResY*skala))

# headingStriker = pygame.image.load("C:/Users/LENOVO/BASESTATION - R2C - WARRIOR (coba)/assets/headingStriker.png").convert_alpha()
# headingStriker = pygame.transform.scale(headingStriker,(headingResX*skala,headingResY*skala))

# musuhCyan = pygame.image.load("C:/Users/LENOVO/BASESTATION - R2C - WARRIOR (coba)/assets/musuhCyan.png").convert_alpha()
# musuhCyan = pygame.transform.scale(musuhCyan,(robotResX*skala,robotResY*skala))

# musuhMagenta = pygame.image.load("C:/Users/LENOVO/BASESTATION - R2C - WARRIOR (coba)/assets/musuhMagenta.png").convert_alpha()
# musuhMagenta = pygame.transform.scale(musuhMagenta,(robotResX*skala,robotResY*skala))

# bgMenu = pygame.image.load("C:/Users/LENOVO/BASESTATION - R2C - WARRIOR (coba)/assets/bgMenu.png").convert_alpha()
# bgMenu = pygame.transform.scale(bgMenu, res)

# bgConf = pygame.image.load("C:/Users/LENOVO/BASESTATION - R2C - WARRIOR (coba)/assets/bgConf.png").convert_alpha()
# bgConf = pygame.transform.scale(bgConf, res)

# bgSim = pygame.image.load("C:/Users/LENOVO/BASESTATION - R2C - WARRIOR (coba)/assets/bgSim.png").convert_alpha()
# bgSim = pygame.transform.scale(bgSim, res)