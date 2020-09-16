import socket
from sqliteServer import checkUser

HOST = '127.0.0.1'        # '192.168.29.105'   Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

while (t:=True) :
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    break

                print(f'Recived : {data}')
                conn.sendall((s:=checkUser(r'server/users.sqlite',*data.split('<SEP>'))).encode('utf-8'))
                print(f'Sent : {s}')