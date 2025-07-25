from time import sleep
import modules.varGlobals as varGlobals
import socket

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

def send_robot(data):
    sendrobot=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sendrobot.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 3)
    if varGlobals.udp:
        sendrobot.sendto(data, (varGlobals.ADDRESS, int(varGlobals.PORT_ADD)))
        #print(len(data),data)
    else:
        sendrobot.close()