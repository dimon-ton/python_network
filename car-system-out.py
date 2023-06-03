import csv
import socket


# save to csv

def writetocsv(data):
    with open("2-car-system-out.csv", "a", newline='', encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)
    print('csv saved')



# ip address
serverip = '192.168.210.100'
port = 9000
buffersize = 4096


# 
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
    writetocsv(data.split('|'))

    # บันทึกลง CSV
    

    client.send('saved'.encode('utf-8'))
    client.close()




'''
1-car-system-out.py
    - server.py
    function
    - บักทึกเวลาออก
    - คำนวณชั่วโมงจอด
    - คำนวณค่าจอด
    -  บันทึกข้อมูลที่ได้รับจาก [2]

'''