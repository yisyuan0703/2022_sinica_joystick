import socket

HOST = "127.0.0.1" # the first three numbers should be the same as the TM Robot's IP address
PORT = 5890 # port is fixed in TM Robot

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')

while True:
    conn, addr = s.accept()
    print('connected by ' + str(addr))

    while True:
        indata = conn.recv(1024)
        if len(indata) == 0: # connection closed
            conn.close()
            print('client closed connection.\n')
            break
        print('recv: ' + indata.decode()+'\n')

        outdata = 'echo: recieved'
        conn.send(outdata.encode())