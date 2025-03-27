import modules.varGlobals as varGlobals
import time
import modules.dataRobot as dataRobot

def start():
    varGlobals.stop = False
    varGlobals.start = True
    
    prestart = False

    while varGlobals.start:
        #print("ini Start")
        if not prestart:
            for i in range(5):
                print("send prestart Start")
            prestart=True
        time.sleep(0.50)