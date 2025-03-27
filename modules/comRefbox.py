# import modules.varGlobals as varGlobals
# import socket
# import threading
# import json
# from modules.comBasestation import send_robot

# prestart = None
        
# #############################################################################################
# #                                   KONEKSI KE REFBOX                                       #
# #############################################################################################
# def connect_refbox():
#     #MEMBUAT SOCKET
#     varGlobals.refbox=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     varGlobals.refbox.connect((varGlobals.IP,int(varGlobals.PORT_IP)))
#     con=varGlobals.refbox.recv(1024).decode().replace("\n","").replace("\x00","")

#     #PROTEKSI UNTUK MENGHUBUNGKAN KE REFBOX
#     print(len(con))
#     if len(con)==1:
#         if con =="W":
#             print("WELCOME")
#             varGlobals.MESSAGE_REFBOX='WELCOME'
#             varGlobals.CONNECT='CONNECTED'
#             varGlobals.ref=True
#             threading.Thread(target=recRef, daemon=True).start()

#     else:
#         try:
#             command = json.loads(con)
#             #PROTEKSI UNTUK MENGHUBUNGKAN KE REFBOX
#             if command["command"]=="WELCOME":
#                 print("WELCOME")
#                 varGlobals.TEAM_IP = command["targetTeam"]
#                 print(f"TargetTeam: {varGlobals.TEAM_IP}")
#                 varGlobals.MESSAGE_REFBOX='WELCOME'
#                 varGlobals.CONNECT='CONNECTED'
#                 varGlobals.ref=True
#                 threading.Thread(target=recRefJSON, daemon=True).start()
        
#         except json.JSONDecodeError:
#             print("Invalid JSON")


# #############################################################################################
# #                            MENERIMA DATA TCP DARI REFBOX                                  #
# #############################################################################################
# def recRef():
#     data=bytearray(2)

#     #LOOPING
#     while varGlobals.ref:
#         #TERIMA DATA DARI REFBOX
#         comMsg=varGlobals.refbox.recv(1024).decode()
#         varGlobals.newMsgRef=True

#         #PERINTAH UTAMA REFBOX
#         if comMsg == "S":
#             varGlobals.MESSAGE_REFBOX='STOP'
#         elif comMsg == 's':
#             varGlobals.MESSAGE_REFBOX='START'
#         elif comMsg == 'N':
#             varGlobals.MESSAGE_REFBOX='DROP BALL'
#         elif comMsg == 'e':
#             varGlobals.MESSAGE_REFBOX='END GAME'
#         elif comMsg == 'L':
#             varGlobals.MESSAGE_REFBOX='PARK'
#         elif comMsg == 'Z':
#             varGlobals.MESSAGE_REFBOX ='GAME RESET'
#             varGlobals.refbox.close()

#         #PERINTAH UNTUK CYAN
#         elif comMsg == 'K':
#             varGlobals.MESSAGE_REFBOX='CYAN KICKOFF'
#         elif comMsg == 'F':
#             varGlobals.MESSAGE_REFBOX='CYAN FREEKICK'
#         elif comMsg == 'G':
#             varGlobals.MESSAGE_REFBOX='CYAN GOALKICK'
#         elif comMsg == 'T':
#             varGlobals.MESSAGE_REFBOX='CYAN THROW IN'
#         elif comMsg == 'C':
#             varGlobals.MESSAGE_REFBOX='CYAN CORNER'
#         elif comMsg == 'P':
#             varGlobals.MESSAGE_REFBOX='CYAN PENALTY KICK'
#         elif comMsg == 'A':
#             varGlobals.MESSAGE_REFBOX='CYAN GOAL+'
#         elif comMsg == 'D':
#             varGlobals.MESSAGE_REFBOX='CYAN GOAL-'

#         #PERINTAH UNTUK MAGENTA
#         elif comMsg == 'k':
#             varGlobals.MESSAGE_REFBOX='MAGENTA KICKOFF'
#         elif comMsg == 'f':
#             varGlobals.MESSAGE_REFBOX='MAGENTA FREEKICK'
#         elif comMsg == 'g':
#             varGlobals.MESSAGE_REFBOX='MAGENTA GOALKICK'
#         elif comMsg == 't':
#             varGlobals.MESSAGE_REFBOX='MAGENTA THROW IN'
#         elif comMsg == 'c':
#             varGlobals.MESSAGE_REFBOX='MAGENTA CORNER'
#         elif comMsg == 'p':
#             varGlobals.MESSAGE_REFBOX='MAGENTA PENALTY KICK'
#         elif comMsg == 'a':
#             varGlobals.MESSAGE_REFBOX='MAGENTA GOAL+'
#         elif comMsg == 'd':
#             varGlobals.MESSAGE_REFBOX='MAGENTA GOAL-'
#         elif comMsg == 'h':
#             varGlobals.MESSAGE_REFBOX='HALFTIME'
#         else:
#             varGlobals.MESSAGE_REFBOX='empty'


# #############################################################################################
# #                            MENERIMA DATA JSON TCP DARI REFBOX                             #
# #############################################################################################
# def recRefJSON():
#     #LOOPING
#     while varGlobals.ref:
#         #TERIMA DATA DARI REFBOX
#         comMsg=varGlobals.refbox.recv(1024).decode().replace("\n","").replace("\x00","")

#         if comMsg:
#             varGlobals.newMsgRef=True
#             try:
#                 print(f"dataTerimaCONNECT: {comMsg}")
#                 command = json.loads(comMsg)
#                 #PERINTAH UTAMA REFBOX
#                 if command["command"]=="STOP":
#                     varGlobals.MESSAGE_REFBOX='STOP'
#                 elif command["command"]=="START":
#                     varGlobals.MESSAGE_REFBOX='START'
#                 elif command["command"]=="DROP_BALL":
#                     varGlobals.MESSAGE_REFBOX='DROP BALL'
#                 elif command["command"]=="END_GAME":
#                     varGlobals.MESSAGE_REFBOX='END GAME'
#                 elif command["command"]=="PARK":
#                     varGlobals.MESSAGE_REFBOX='PARK'
#                 elif command["command"]=="RESET":
#                     varGlobals.MESSAGE_REFBOX ='GAME RESET'
#                     varGlobals.refbox.close()

#                 #PERINTAH UNTUK CYAN
#                 elif command["command"]=="KICKOFF":
#                     if varGlobals.cyan and command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='CYAN KICKOFF'
#                     elif varGlobals.cyan and not command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='MAGENTA KICKOFF'

#                     if varGlobals.magenta and command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='MAGENTA KICKOFF'
#                     elif varGlobals.magenta and not command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='CYAN KICKOFF'

#                 elif command["command"]=="FREEKICK":
#                     if varGlobals.cyan and command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='CYAN FREEKICK'
#                     elif varGlobals.cyan and not command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='MAGENTA FREEKICK'

#                     if varGlobals.magenta and command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='MAGENTA FREEKICK'
#                     elif varGlobals.magenta and not command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='CYAN FREEKICK'

#                 elif command["command"]=="GOALKICK":
#                     if varGlobals.cyan and command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='CYAN GOALKICK'
#                     elif varGlobals.cyan and not command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='MAGENTA GOALKICK'

#                     if varGlobals.magenta and command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='MAGENTA GOALKICK'
#                     elif varGlobals.magenta and not command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='CYAN GOALKICK'

#                 elif command["command"]=="THROWIN":
#                     if varGlobals.cyan and command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='CYAN THROW IN'
#                     elif varGlobals.cyan and not command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='MAGENTA THROW IN'

#                     if varGlobals.magenta and command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='MAGENTA THROW IN'
#                     elif varGlobals.magenta and not command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='CYAN THROW IN'
                    
#                 elif command["command"]=="CORNER":
#                     if varGlobals.cyan and command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='CYAN CORNER'
#                     elif varGlobals.cyan and not command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='MAGENTA CORNER'

#                     if varGlobals.magenta and command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='MAGENTA CORNER'
#                     elif varGlobals.magenta and not command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='CYAN CORNER'

#                 elif command["command"]=="PENALTY":
#                     if varGlobals.cyan and command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='CYAN PENALTY KICK'
#                     elif varGlobals.cyan and not command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='MAGENTA PENALTY KICK'

#                     if varGlobals.magenta and command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='MAGENTA PENALTY KICK'
#                     elif varGlobals.magenta and not command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='CYAN PENALTY KICK'

#                 elif command["command"]=="GOAL":
#                     if varGlobals.cyan and command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='CYAN GOAL+'
#                     elif varGlobals.cyan and not command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='MAGENTA GOAL+'

#                     if varGlobals.magenta and command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='MAGENTA GOAL+'
#                     elif varGlobals.magenta and not command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='CYAN GOAL+'

#                 elif command["command"]=="SUBGOAL":
#                     if varGlobals.cyan and command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='CYAN GOAL-'
#                     elif varGlobals.cyan and not command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='MAGENTA GOAL-'

#                     if varGlobals.magenta and command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='MAGENTA GOAL-'
#                     elif varGlobals.magenta and not command["targetTeam"]==varGlobals.TEAM_IP:
#                         varGlobals.MESSAGE_REFBOX='CYAN GOAL-'


#                 elif comMsg == 'h':
#                     varGlobals.MESSAGE_REFBOX='HALFTIME'
#                 else:
#                     varGlobals.MESSAGE_REFBOX='empty'

#             except json.JSONDecodeError:
#                 print("Invalid JSON")