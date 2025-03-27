import socket
import keyboard
import time

TARGET_IP = "172.11.12.33"
TARGET_PORT = 8081

command_mapping = {
    'w': 100,
    'a': 101,
    's': 102,
    'd': 103
}

# command_mapping = {
#     'w': 'maju',
#     'a': 'kiri',
#     's': 'mundur',
#     'd': 'kanan',
# }

def send_command(command):
    if command in command_mapping:
        value = command_mapping[command]
        message = str(value).encode()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_IP)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)
        sock.sendto(message, (TARGET_IP, TARGET_PORT))
        sock.close()
        print(f"{value}")
    else:
        print(f"Perintah tidak dikenal: {command}")

if __name__ == "__main__":
    print("Tekan tombol 'w', 'a', 's', 'd' untuk mengirim perintah, dan 'esc' untuk keluar.")
    
    while True:
        try:
            for key in command_mapping.keys():
                if keyboard.is_pressed(key):
                    send_command(key)
                        
            if keyboard.is_pressed('esc'):
                print("Program dihentikan.")
                break
    
            time.sleep(0.25)

        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            break

