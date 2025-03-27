import modules.varGlobals as varGlobals
import threading
# from lib.kickOff import kickoffMusuh,kickoffTeam
# from lib.freekick import freeKickMusuh,freeKickTeam
# from lib.goalKick import goalKickMusuh,goalKickTeam
# from lib.throwIn import throwInMusuh, throwInTeam
# from lib.corner import cornerMusuh, cornerMusuh, cornerTeam
# from lib.penalty import penaltyMusuh, penaltyTeam
from library.stop import stop
from library.start import start
# from lib.dropBall import dropBall
from library.endPart import endPart
from library.park import park
from modules.comBasestation import startBs
import time

def playGame():
    if varGlobals.newMsgRef:
        varGlobals.BIND = 'BIND'
        print("autobind basestation")
        varGlobals.kiper = False
        varGlobals.back = False
        varGlobals.striker =False
        varGlobals.conKiper = 'KIPER DISCONNECTED' 
        varGlobals.conBack = 'BACK DISCONNECTED' 
        varGlobals.conStriker = 'STRIKER DISCONNECTED'
        varGlobals.udp=False

        time.sleep(0.30)

        varGlobals.udp=True
        varGlobals.BIND='SUCCESS'
        startBs()
        # if varGlobals.MESSAGE_REFBOX=="STOP":
        #     threading.Thread(target=stop, daemon=True).start()
            
        # elif varGlobals.MESSAGE_REFBOX=="START":
        #     threading.Thread(target=start, daemon=True).start()

        # # elif varGlobals.MESSAGE_REFBOX=="DROP BALL":
        # #     threading.Thread(target=dropBall, daemon=True).start()

        # elif varGlobals.MESSAGE_REFBOX=="PARK":
        #     #threading.Thread(target=park, daemon=True).start()
        #     print("INI PARK")

        # elif varGlobals.MESSAGE_REFBOX=="END PART":
        #     #threading.Thread(target=endPart, daemon=True).start()
        #     print("INI END PARK")

        ############################################################################

        # if varGlobals.cyan and varGlobals.MESSAGE_REFBOX=="CYAN KICKOFF":
        #     threading.Thread(target=kickoffTeam, daemon=True).start()
            
        # elif varGlobals.cyan and varGlobals.MESSAGE_REFBOX=="MAGENTA KICKOFF":
        #     threading.Thread(target=kickoffMusuh, daemon=True).start()
        
        # if varGlobals.magenta and varGlobals.MESSAGE_REFBOX=="MAGENTA KICKOFF":
        #     threading.Thread(target=kickoffTeam, daemon=True).start()
            
        # elif varGlobals.magenta and varGlobals.MESSAGE_REFBOX=="CYAN KICKOFF":
        #     threading.Thread(target=kickoffMusuh, daemon=True).start()
            
        ############################################################################
        
        # if varGlobals.cyan and varGlobals.MESSAGE_REFBOX=="CYAN FREEKICK":
        #     threading.Thread(target=freeKickTeam, daemon=True).start()
            
        # elif varGlobals.cyan and varGlobals.MESSAGE_REFBOX=="MAGENTA FREEKICK":
        #     threading.Thread(target=freeKickMusuh, daemon=True).start()
        
        # if varGlobals.magenta and varGlobals.MESSAGE_REFBOX=="MAGENTA FREEKICK":
        #     threading.Thread(target=freeKickTeam, daemon=True).start()
            
        # elif varGlobals.magenta and varGlobals.MESSAGE_REFBOX=="CYAN FREEKICK":
        #     threading.Thread(target=freeKickMusuh, daemon=True).start()
            
        # ############################################################################
        
        # if varGlobals.cyan and varGlobals.MESSAGE_REFBOX=="CYAN GOALKICK":
        #     threading.Thread(target=goalKickTeam, daemon=True).start()
            
        # elif varGlobals.cyan and varGlobals.MESSAGE_REFBOX=="MAGENTA GOALKICK":
        #     threading.Thread(target=goalKickMusuh, daemon=True).start()
        
        # if varGlobals.magenta and varGlobals.MESSAGE_REFBOX=="MAGENTA GOALKICK":
        #     threading.Thread(target=goalKickTeam, daemon=True).start()
            
        # elif varGlobals.magenta and varGlobals.MESSAGE_REFBOX=="CYAN GOALKICK":
        #     threading.Thread(target=goalKickMusuh, daemon=True).start()
            
        # ############################################################################
        
        # if varGlobals.cyan and varGlobals.MESSAGE_REFBOX=="CYAN THROW IN":
        #     threading.Thread(target=throwInTeam, daemon=True).start()
            
        # elif varGlobals.cyan and varGlobals.MESSAGE_REFBOX=="MAGENTA THROW IN":
        #     threading.Thread(target=throwInMusuh, daemon=True).start()
        
        # if varGlobals.magenta and varGlobals.MESSAGE_REFBOX=="MAGENTA THROW IN":
        #     threading.Thread(target=throwInTeam, daemon=True).start()
            
        # elif varGlobals.magenta and varGlobals.MESSAGE_REFBOX=="CYAN THROW IN":
        #     threading.Thread(target=throwInMusuh, daemon=True).start()
            
        # ############################################################################
        
        # if varGlobals.cyan and varGlobals.MESSAGE_REFBOX=="CYAN CORNER":
        #     threading.Thread(target=cornerTeam, daemon=True).start()
            
        # elif varGlobals.cyan and varGlobals.MESSAGE_REFBOX=="MAGENTA CORNER":
        #     threading.Thread(target=cornerMusuh, daemon=True).start()
        
        # if varGlobals.magenta and varGlobals.MESSAGE_REFBOX=="MAGENTA CORNER":
        #     threading.Thread(target=cornerTeam, daemon=True).start()
            
        # elif varGlobals.magenta and varGlobals.MESSAGE_REFBOX=="CYAN CORNER":
        #     threading.Thread(target=cornerMusuh, daemon=True).start()
            
        # ############################################################################
        
        # if varGlobals.cyan and varGlobals.MESSAGE_REFBOX=="CYAN PENALTY KICK":
        #     threading.Thread(target=penaltyTeam, daemon=True).start()
            
        # elif varGlobals.cyan and varGlobals.MESSAGE_REFBOX=="MAGENTA PENALTY KICK":
        #     threading.Thread(target=penaltyMusuh, daemon=True).start()
        
        # if varGlobals.magenta and varGlobals.MESSAGE_REFBOX=="MAGENTA PENALTY KICK":
        #     threading.Thread(target=penaltyTeam, daemon=True).start()
            
        # elif varGlobals.magenta and varGlobals.MESSAGE_REFBOX=="CYAN PENALTY KICK":
        #     threading.Thread(target=penaltyMusuh, daemon=True).start()
            
        ############################################################################
            
    varGlobals.newMsgRef=False