import csv
import socket
import uuid

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



car_dict = {}


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


    source = data.split('|')[0] # มาจากโปรแกรมฝั่งไหน
    
    if source == 'in':
        # บันทึกข้อมูลลงใน dict
        key = str(uuid.uuid1()).split('-')[0]
        car_dict[key] = data.split('|')

        # บันทึกลง CSV
        writetocsv(data.split('|'))
        client.send('saved'.encode('utf-8'))
        client.close()
    elif source == 'location':
        text = 'out|'
        for k,v in car_dict.items():
            text += k + '|'
            for dt in v:
                text += dt + '|'

        print('Send to location: ', text)
        client.send(text.encode('utf-8'))
        client.close()
    else:
        pass





'''
1-car-system-out.py
    - server.py
    function
    - บักทึกเวลาออก
    - คำนวณชั่วโมงจอด
    - คำนวณค่าจอด
    -  บันทึกข้อมูลที่ได้รับจาก [2]

'''