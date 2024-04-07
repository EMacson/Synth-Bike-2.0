# server program from recieving messages from the pico
# and producing sound
# https://www.youtube.com/watch?v=xwxt32ollv0&list=PL_yUKG0GRuliyrzaGyrOl5DRHycCbGsRG was used as a tutorial for scamp
# https://www.youtube.com/watch?v=3QiPPX-KeSc and
# https://thepihut.com/blogs/raspberry-pi-tutorials/wireless-communication-between-two-raspberry-pi-pico-w-boards
# were used for socket programming

import socket
from scamp import *

# socket defintions
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

# button strings
C_str = "60"
D_str = "62"
E_str = "64"
F_str = "66"
G_str = "68"
A_str = "70"
B_str = "72"
K_str = "74"

C = 60
D = 62
E = 64
F = 66
G = 68
A = 70
B = 72
K = 74

# using clarinet as it sounded the best
s = Session()
clarinet = s.new_part("clarinet")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT).strip()
        if msg_length: 
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"[{addr}] {msg}")
                break

            # deliminate msg and play chord
            delim = msg.split("-")
            volume = float(delim[1])
            chord = [int(delim) for delim in delim[2:-1]]
            print(f"[{addr}] {chord}")

            clarinet.play_chord(chord, volume, 1)

    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        handle_client(conn, addr)

print("[STARTING] server is starting...")
start()