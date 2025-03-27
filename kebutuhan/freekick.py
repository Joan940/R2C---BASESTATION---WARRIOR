import modules.varGlobals as varGlobals
import time
# from lib.pathFinding import calculateRadius
from lib.playGame import playGame 
import modules.dataRobot as dataRobot
from lib.skils import lariBiasa,lihatBolaGeser,tendangKencang,pindahAwalKiper,ballPredictKiper,sendGrid ,tendangKencang,kejarBolaPelan, umpanTeman, lihatBolaDiam, kejarBolaCepat, changePos, tendangGiring

def reset():
    varGlobals.runLariTeam = False
    varGlobals.runLariMusuh = False

    varGlobals.runKickoffTeam = False
    varGlobals.runKickoffMusuh = False

    varGlobals.runFreeKickTeam = False
    varGlobals.runFreeKickMusuh = False

    varGlobals.runGoalKickTeam = False
    varGlobals.runGoalKickMusuh = False

    varGlobals.runThrowInTeam = False
    varGlobals.runThrowInMusuh = False

    varGlobals.runCornerTeam = False
    varGlobals.runCornerMusuh = False

    varGlobals.runPenaltyTeam = False
    varGlobals.runPenaltyMusuh = False

    varGlobals.stop = False
    varGlobals.start = False
    varGlobals.dropBall = False
    varGlobals.park = False
    varGlobals.endPart = False

def setPosition(setBall_x, setBall_y):
    position = {}
    if (setBall_x, setBall_y) in [(500, 234), (500, 414), (500, 594)]:
        position = {
            (500, 234): {
                1: {'x': 3 * 50, 'y': 1 * 50},
                2: {'x': 8 * 50, 'y': 4 * 50}
            },
            (500, 414): {
                1: {'x': 3 * 50, 'y': 2 * 50},
                2: {'x': 12 * 50, 'y': 4 * 50}
            },
            (500, 594): {
                1: {'x': 7 * 50, 'y': 4 * 50},
                2: {'x': 15 * 50, 'y': 4 * 50}
            }
        }
    elif (setBall_x, setBall_y) in [(860, 234), (860, 594)]:
        position = {
            (860, 234): {
                1: {'x': 3 * 50, 'y': 10 * 50},
                2: {'x': 9 * 50, 'y': 9 * 50}
            },
            (860, 594): {
                1: {'x': 10 * 50, 'y': 10 * 50},
                2: {'x': 9 * 50, 'y': 9 * 50}
            }
        }
    elif (setBall_x, setBall_y) in [(1220, 234), (1220, 414), (1220, 594)]:
        position = {
            (1220, 234): {
                1: {'x': 2 * 50, 'y': 900},
                2: {'x': 8 * 50, 'y': 10 * 50}
            },
            (1220, 414): {
                1: {'x': 7 * 50, 'y': 900},
                2: {'x': 8 * 50, 'y': 10 * 50}
            },
            (1220, 594): {
                1: {'x': 11 * 50, 'y': 900},
                2: {'x': 8 * 50, 'y': 10 * 50}
            }
        }
    return position

def pergerakan(position):
    for robot_id, pos in position.items():
        changePos(robot_id, pos['x'], pos['y'], 0)

def tungguPosisi(position):
    waktuMulai = time.time()
    while time.time() - waktuMulai < 5:
        diPosisi = True
        for robot_id, pos in position.items():
            if dataRobot.xpos[robot_id]//50 != pos['x']//50 or dataRobot.ypos[robot_id]//50 != pos['y']//50:
                diPosisi = False
                tungguPosisi(position)
                time.sleep(0.015)
                break
        if diPosisi:
            print("Sudah Di Posisi")
            return

def strategi(position):
    if varGlobals.striker and varGlobals.back:
        ballPredictKiper()
        lihatBolaDiam(1)
        kejarBolaCepat(1)
        tendangGiring(1)
        kejarBolaCepat(1)
        tendangKencang(1)
        while not varGlobals.stop:
            if varGlobals.stop == True:
                break
            else:
                if varGlobals.ball_x < 860 and dataRobot.catch_ball[2] == 0:
                    kejarBolaCepat(2)
                    lihatBolaDiam(1)
                    umpanTeman(2)
                    kejarBolaCepat(1)
                    tendangKencang(1)
                elif varGlobals.ball_x > 860:
                    lihatBolaGeser(2)
                    lihatBolaDiam(1)
                    kejarBolaCepat(1)
                    tendangKencang(1)
                elif varGlobals.ball_x < 860 and dataRobot.catch_ball[2] == 1:
                    lihatBolaDiam(1)
                    umpanTeman(2)
                    kejarBolaCepat(1)
                    tendangKencang(1)
    
    elif varGlobals.striker and not varGlobals.back:
        kejarBolaPelan(2)
        tendangGiring(2)
        kejarBolaCepat(2)
        tendangKencang(2)
    elif not varGlobals.striker and varGlobals.back:
        kejarBolaPelan(1)
        tendangGiring(1)
        kejarBolaCepat(1)
        tendangKencang(1)

def freeKickHandler(isTeamFreeKick):
    reset()
    varGlobals.runFreeKickTeam = isTeamFreeKick
    varGlobals.runFreeKickMusuh = not isTeamFreeKick
    
    while (varGlobals.runFreeKickTeam or varGlobals.runFreeKickMusuh) and not varGlobals.stop:
        print("Mulai Free Kick")
        pindahAwalKiper()
        ballPredictKiper()

        positions = setPosition(varGlobals.setBall_x, varGlobals.setBall_y)
        pergerakan(positions)
        tungguPosisi(positions)

        #Freekick Musuh
        if varGlobals.runFreeKickMusuh:
            if (positions) in [(500, 234), (500, 414), (500, 594)]:
                position = {
                    (500, 234): {
                        1: {'x': 3 * 50, 'y': 1 * 50},
                        2: {'x': 8 * 50, 'y': 4 * 50}
                    },
                    (500, 414): {
                        1: {'x': 3 * 50, 'y': 2 * 50},
                        2: {'x': 12 * 50, 'y': 4 * 50}
                    },
                    (500, 594): {
                        1: {'x': 7 * 50, 'y': 4 * 50},
                        2: {'x': 15 * 50, 'y': 4 * 50}
                    }
                }
            elif (positions) in [(860, 234), (860, 594)]:
                position = {
                    (860, 234): {
                        1: {'x': 3 * 50, 'y': 10 * 50},
                        2: {'x': 9 * 50, 'y': 9 * 50}
                    },
                    (860, 594): {
                        1: {'x': 10 * 50, 'y': 10 * 50},
                        2: {'x': 9 * 50, 'y': 9 * 50}
                    }
                }
            elif (positions) in [(1220, 234), (1220, 414), (1220, 594)]:
                position = {
                    (1220, 234): {
                        1: {'x': 3 * 50, 'y': 13 * 50},
                        2: {'x': 8 * 50, 'y': 10 * 50}
                    },
                    (1220, 414): {
                        1: {'x': 7 * 50, 'y': 13 * 50},
                        2: {'x': 8 * 50, 'y': 10 * 50}
                    },
                    (1220, 594): {
                        1: {'x': 11 * 50, 'y': 13 * 50},
                        2: {'x': 8 * 50, 'y': 10 * 50}
                    }
                }
            pergerakan(positions)
            tungguPosisi(positions)

        if varGlobals.start and not varGlobals.stop:
            strategi(positions)
        time.sleep(0.25)

def freeKickTeam():
    freeKickHandler(True)

def freeKickMusuh():
    freeKickHandler(False)