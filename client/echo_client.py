import socket

def sendCred(userName,password) :
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65432        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(f'{userName}<SEP>{password}'.encode('utf-8'))
        data = s.recv(1024)

    print('Received', repr(data))
    return data