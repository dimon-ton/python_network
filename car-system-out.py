import csv
import socket
import uuid
import threading

# save to csv
def writetocsv(data):
    with open("2-car-system-out.csv", "a", newline='', encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)
    print('csv saved')



# ip address
serverip = '172.24.16.1'
port = 9000
buffersize = 4096



car_dict = {}

def OutServer():
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

task = threading.Thread(target=OutServer)
task.start()

while True:
    if len(car_dict) == 0:
        print('Not Found Car')
        q = input('Enter to Continue: ')
        print('--------------------------------------')
    else:
        print()
        print('-------------select car out---------------')

        car_number = {}
        car_plate = {}

        for i, c in enumerate(car_dict.items(), start=1):
            print('[{}]'.format(i), c)

            # add key to c[1]
            if c[1][0] != c[0]:
                c[1].insert(0, c[0])

            car_number[str(i)] = c[1] # only value
            car_plate[c[1][4]] = c[1]


        print('[P] - for enter plate number')   
        print('[R] - Refresh Data')
        print('-------------------------------')

        q = input('Select Car: ')
        
        if q == 'R' or q == 'r':
            continue

        if q == 'P' or q == 'p':
            p = input('Enter Plate Number: ')
            print(car_plate[p])
        else:
            print(car_number[q])

        print('-----------------------------------------')



'''
1-car-system-out.py
    - server.py
    function
    - บักทึกเวลาออก
    - คำนวณชั่วโมงจอด
    - คำนวณค่าจอด
    -  บันทึกข้อมูลที่ได้รับจาก [2]

'''