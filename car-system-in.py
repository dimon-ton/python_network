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


    # - บันทึกข้อมูลรถ ยี่ห้อ สี ป้ายทะเบียน บัตร
    info = {'brand':{'q':'Brand: ', 'value':None},
            'color':{'q':'Color: ', 'value':None},
            'plate':{'q':'Plate: ', 'value':None},
            'card':{'q':'Card: ', 'value':None}
            }
    
    # timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 


    # data = input('Send to Server: ')


    for k, v in info.items():
        d = input(v['q'])
        info[k]['value'] = d



    print(info)

    text = 'in|' # in| is a prefix from car system in

    for v in info.values():
        text += v['value'] + '|'


    text += timestamp


    print(text)

    writetocsv(text.split('|'))


    # connect and send

    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.connect((serverip, port))
    server.send(text.encode('utf-8'))
    data_server = server.recv(buffersize).decode('utf-8')
    print('Data from server: ', data_server)
    server.close()








'''
2-car-system-in.py
    - client-1.py
    function
        - บันทึกข้อมูลรถ ยี่ห้อ สี ป้ายทะเบียน บัตร
        - บันทึกเวลาเข้า
        - ส่งไปหา [1]
        - บันทึลงใน csv เครื่องตัวเอง

'''