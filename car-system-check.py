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
serverip = '172.24.16.1'
port = 9500
buffersize = 4096

while True:

    text = 'check|'

    q = input('Enter Plate Number: ')
    text += q

    # connect and send

    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.connect((serverip, port))
    server.send(text.encode('utf-8'))
    data_server = server.recv(buffersize).decode('utf-8')
    print('Data from server: ', data_server)

    data_list = data_server.split('|')
    print('Your Car Zone: ', data_list[-2])

    server.close()
    print('---------------------------------')

'''
    4-car-system-check.py
    - client-3.py
    function
        - ดึงข้อมูลรถ ยี่ห้อ สี ป้ายทะเบียน บัตร จาก [3]
        - ดึงข้อมูลตำแหน่งรถจาก  [3]
'''




