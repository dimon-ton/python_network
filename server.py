import socket

serverip = '192.168.210.100'
port = 9000
buffersize = 4096



while True:
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((serverip, port))
    server.listen(1)
    print('waiting for client...')

    client, addr = server.accept()
    print('connected from: ', addr)

    data = client.recv(buffersize).decode('utf-8')
    print('Data from client: ', data)
    client.send('recieved your message: '.encode('utf-8'))
    client.close()

