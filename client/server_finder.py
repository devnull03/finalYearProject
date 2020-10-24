import  socket

ip = '.'.join(socket.gethostbyname(socket.gethostname()).split('.')[:-1]) + '.'

print(
    ip+str(i) for i in range()
)