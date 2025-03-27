# from modules.comBasestation import send_robot
# import modules.varGlobals as varGlobals
# import modules.dataRobot as dataRobot
# import time
# # from lib.goalPosition import drawGoalPositionRandom

# def kejarBolaPelan(id):
#     data=bytearray(3)
#     print("Kejar bola pelan")
#     while dataRobot.catch_ball[id]==0 and not varGlobals.stop:
#         print("wait catch ball pelan")
#         data[0]=int(id)
#         data[1]=int(254)
#         data[2]=int(1)
#         if varGlobals.stop==True:
#             break
#         else:
#             send_robot(data)
#             time.sleep(0.25)

# def tendangGawang(id):
#     data=bytearray(3)
#     while dataRobot.catch_ball[id]==1 and not varGlobals.stop:
#         print("Belum tendang gawang")
#         data[0]=int(id)
#         data[1]=int(254)
#         data[2]=int(2)
#         if varGlobals.stop==True:
#             break
#         else:
#             send_robot(data)
#             time.sleep(0.25)

# def umpanTeman(id):
#     data=bytearray(3)
#     while dataRobot.catch_ball[id]==1 and not varGlobals.stop:
#         print("Masih pegang bola umpan teman", id)
#         data[0]=int(id)
#         data[1]=int(254)
#         data[2]=int(3)
#         if varGlobals.stop==True:
#             break
#         else:
#             send_robot(data)
#             time.sleep(0.25)

# def lihatBolaDiam(id):
#     data=bytearray(3)
#     print("lihat bola diam")
#     data[0]=int(id)
#     data[1]=int(254)
#     data[2]=int(4)
#     send_robot(data)
#     time.sleep(0.25)

# def lihatBolaGeser(id):
#     data=bytearray(3)
#     print("lihat bola geser")
#     data[0]=int(id)
#     data[1]=int(254)
#     data[2]=int(5)
#     if dataRobot.catch_ball[id]==1:
#         if id==1:
#             lihatBolaDiam(2)
#             changePos(2,(dataRobot.xpos[1]//50)-1,(dataRobot.ypos[1]//50)-1)
#             time.sleep(3)
#         elif id==2:
#             lihatBolaDiam(1)
#             changePos(2,(dataRobot.xpos[2]//50)-1,(dataRobot.ypos[2]//50)-1)
#             time.sleep(3)
#         umpanTeman(id)
#     else:
#         send_robot(data)
#     time.sleep(0.25)

# def kejarBolaCepat(id):
#     data=bytearray(3)
#     print("wait kejar bola cepat", id)
#     while dataRobot.catch_ball[id]==0 and not varGlobals.stop:
#         data[0]=int(id)
#         data[1]=int(254)
#         data[2]=int(6)
#         if varGlobals.stop==True:
#             break
#         elif id==1 and dataRobot.catch_ball[2]==1:
#             lihatBolaDiam(1)
#             break
#         else:
#             send_robot(data)
#             print("wait catch ball cepat", id)
#             time.sleep(0.25)

# #################################
# #           Coba Lari           #
# #################################
# def lariBiasa(id):
#     data = bytearray(3)
#     print("Lari biasa", id)
#     while not varGlobals.stop:
#         data[0] = int(id)
#         data[1] = int(254)
#         data[2] = int(11)  
#         if varGlobals.stop:
#             break
#         else:
#             send_robot(data)
#             time.sleep(0.25)

# def tendangGiring(id):
#     print("Tendang Giring")
#     data = bytearray(3)
#     if(dataRobot.xpos[id]>=50 and dataRobot.xpos[id] <=400 and dataRobot.ypos[id] >= 650):
#         while not (dataRobot.kompas_value[id] >=130 and dataRobot.kompas_value[id] <= 140 and not varGlobals.stop):
#             if varGlobals.stop==True:
#                 break
#             else:
#                 changePos(id,dataRobot.xpos[id],dataRobot.ypos[id],135)
#                 print("wait angle 135")
#                 time.sleep(0.25)

#     elif(dataRobot.xpos[id]>=400 and dataRobot.xpos[id]<=800 and dataRobot.ypos[id] >= 650):
#         while not (dataRobot.kompas_value[id] >=220 and dataRobot.kompas_value[id] <= 230 and not varGlobals.stop):
#             if varGlobals.stop==True:
#                 break
#             else:
#                 changePos(id,dataRobot.xpos[id],dataRobot.ypos[id],225)
#                 print("wait angle 225")
#                 time.sleep(0.25)
#     elif(dataRobot.xpos[id]>=50 and dataRobot.xpos[id] <=800 and dataRobot.ypos[id] <= 650):
#         while not (dataRobot.kompas_value[id] >=350 and dataRobot.kompas_value[id] <= 10 and not varGlobals.stop):
#             if varGlobals.stop==True:
#                 break
#             else:
#                 changePos(id,dataRobot.xpos[id],dataRobot.ypos[id],0)
#                 print("wait angle 0")
#                 time.sleep(0.25)
#     else:
#         print("wait angle 0")
#         changePos(id,dataRobot.xpos[id],dataRobot.ypos[id],0)
#         time.sleep(2)

#     while dataRobot.catch_ball[id]==1 and not varGlobals.stop:
#         print("Belum Tendang Giring")
#         data[0] = int(id)
#         data[1] = int(254)
#         data[2] = int(7)
#         if varGlobals.stop==True:
#             break
#         else:
#             send_robot(data)
#             time.sleep(0.25)

# def pindahAwalKiper(): 
#     data = bytearray(3)
#     data[0] = int(0)
#     data[1] = int(254)
#     data[2] = int(8)
#     send_robot(data)
#     time.sleep(0.25)

# def ballPredictKiper():
#     data = bytearray(3)
#     print()
#     data[0] = int(0)
#     data[1] = int(254)
#     data[2] = int(9)
#     send_robot(data)
#     time.sleep(0.25)

# def tendangKencang(id):
#     data=bytearray(3)
#     if(dataRobot.xpos[id]>=50 and dataRobot.xpos[id] <=400 and dataRobot.ypos[id] <= 650):
#             changePos(id,dataRobot.xpos[id],dataRobot.ypos[id],35)
#             print("wait angle 35")
#             time.sleep(1)

#     elif(dataRobot.xpos[id]>=400 and dataRobot.xpos[id]<=800 and dataRobot.ypos[id] <= 650):
#         while not (dataRobot.kompas_value[id] >=335 and dataRobot.kompas_value[id] <= 345 and not varGlobals.stop):
#             if varGlobals.stop==True:
#                 break
#             else:
#                 changePos(id,dataRobot.xpos[id],dataRobot.ypos[id],340)
#                 print("wait angle 340")
#                 time.sleep(1)

#     else:
#         tendangGawang(id)

#     while dataRobot.catch_ball[id]==1 and not varGlobals.stop:
#         print("Belum Tendang Kencang")
#         data[0]=int(id)
#         data[1]=int(254)
#         data[2]=int(10)
#         if varGlobals.stop==True:
#             break
#         else:
#             send_robot(data)
#             time.sleep(0.25)

# def changePos(id,x,y,angle):
#     data=bytearray(6)
#     data[0]=int(id)
#     data[1]=int(255)
#     if angle >=0 and angle <180:
#         data[2]=int(0)
#         data[3]=int(angle)
#     elif angle >=180 and angle <=360:
#         data[2]=int(1)
#         data[3]=int(360-int(angle))
#     data[4] = int(x) // varGlobals.gridRes
#     data[5] = int(y) // varGlobals.gridRes
#     send_robot(data)
#     time.sleep(0.25)

# def resetGrid(id,x,y):
#     data=bytearray(4)
#     data[0]=int(id)
#     data[1]=int(253)
#     data[2]=int(x)
#     data[3]=int(y)
#     send_robot(data)
#     time.sleep(0.25)

# def sendGrid():
#     data = bytearray(6)
#     for i in range (2):
#             data[0]=1
#             data[1]=255
#             data[2]=0
#             data[3]=0 
#             data[4]=int(varGlobals.CONFIG_BACK_GRID_X)
#             data[5]=int(varGlobals.CONFIG_BACK_GRID_Y)
#             send_robot(data)
#             time.sleep(0.25)
#     for i in range (2):
#             data[0]=2
#             data[1]=255
#             data[2]=0
#             data[3]=0 
#             data[4]=int(varGlobals.CONFIG_STRIKER_GRID_X)
#             data[5]=int(varGlobals.CONFIG_STRIKER_GRID_Y)
#             send_robot(data)
#             time.sleep(0.25)


######################################################################################################################################################