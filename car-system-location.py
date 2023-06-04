from datetime import datetime
import socket
import csv


# save to csv

def writetocsv(data):
    with open("2-car-system-in.csv", "a", newline='', encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)
    print('csv saved')


# address
serverip = '192.168.210.100'
port = 9000
buffersize = 4096

while True:
    q = input('[1] - get multiple car information\n[2] - get single car\n[q] - exit')

    if q == '1':
        text = 'location|allcar'
    elif q == '2':
        getcar = 'Enter Plate Code: '
        text = 'location|{}'.format(getcar)
    elif q == 'q':
        break

    text = 'location|allcar'

    # connect and send

    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.connect((serverip, port))
    server.send(text.encode('utf-8'))
    data_server = server.recv(buffersize).decode('utf-8')
    print('Data from server: ', data_server)
    server.close()








'''
3-car-system-location.py
    - client-1.py
    function
        - ดึงข้อมูลรถ ยี่ห้อ สี ป้ายทะเบียน บัตร จาก [1]
    - server.py
        - บันทึกตำแหน่งโซนของรถได้
        - ส่งข้อมูลรถไปยัง [4]

'''