# import socket

# # Alamat dan port lokal untuk bind
# LOCAL_IP = "0.0.0.0"
# LOCAL_PORT = 8081

# # Pemetaan nilai numerik ke perintah
# value_mapping = {
  
# }

# def receive_commands():
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     sock.bind((LOCAL_IP, LOCAL_PORT))
    
#     print(f"Mendengarkan di {LOCAL_IP}:{LOCAL_PORT}")
#     while True:
#         try:
#             data, addr = sock.recvfrom(1024)
#             value = data.decode()
#             command = value_mapping.get(value, 'Joan')
#             print(f"Dari {command} : {value}, alamat : {addr}")
#         except Exception as e:
#             print(f"Terjadi kesalahan: {e}")

# if __name__ == "__main__":
#     receive_commands()

