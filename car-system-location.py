import socket
import csv
import threading



# save to csv
def writetocsv(data):
  with open("2-car-system-in.csv", "a", newline='', encoding='utf-8') as file:
    fw = csv.writer(file)
    fw.writerow(data)
  print('csv saved')



serverip_location = '192.168.97.100'
port_location = 9500
buffsize_location = 4096

plate_dict = {}

def LocationServer():
  while True:
      server = socket.socket()
      server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

      server.bind((serverip_location, port_location))
      server.listen(1)
      print('waiting for client...')

      client, addr = server.accept()
      print('connected from: ', addr)

      data = client.recv(buffsize_location).decode('utf-8')
      print('Data from client: ', data)


      source = data.split('|')[0] # มาจากโปรแกรมฝั่งไหน
      plate = data.split('|')[1]


      if source == 'check':
          check = plate_dict[plate]

          text = 'location|'
          for c in check:
            text += c + '|'

          client.send(text.encode('utf-8'))
          client.close()
      else:
          client.close()

      


# run threading
task = threading.Thread(target=LocationServer)
task.start()


# devide data into list
def splitrow(datalist, column=7):
  result = []
  buff_list = []
  for i, t in enumerate(datalist, start=1):
    if i % column == 0:
      buff_list.append(t)
      result.append(buff_list)
      buff_list = []
    else:
      buff_list.append(t)
  return result


# address
serverip = '192.168.97.100'
port = 9000
buffersize = 4096

while True:
  q = input(
    '[1] - get multiple car information\n[2] - get single car\n[3] - Save Car Zone\n[q] - exit\n')

  if q == '1':
    text = 'location|allcar'
  elif q == '2':
    getcar = 'Enter Plate Code: '
    text = 'location|{}'.format(getcar)
  elif q == '3':
    plate = input('Enter Plate Code: ')
    getzone = input('Enter Zone Number: ')

    if len(plate_dict[plate]) == 7:
      # ยังไม่เคยกรอก ข้อมูลจะมีทั้ง 7 รายการ
      plate_dict[plate].append(getzone)
    else:
      # ถ้าเคยกรอกไปแล้ว ต้องการเปลี่ยนให้ใช้แบบนี้
      plate_dict[plate][7] = getzone


  elif q == 'q':
    break

  text = 'location|allcar'


  if q != '3':
    # connect and send

    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.connect((serverip, port))
    server.send(text.encode('utf-8'))
    data_server = server.recv(buffersize).decode('utf-8')
    print('Data from server: ', data_server)

    data_list = data_server.split('|')[1:-1]  # arrange data into data_iist
    for row in splitrow(data_list, 7):
      print(row)

      if row[4] not in plate_dict:
        plate_dict[row[4]] = row # บันทึกข้อมูลของรถเก็บไว้เป็น dict

    server.close()

    print('-------------------------------------------')




'''
3-car-system-location.py
    - client-1.py
    function
        - ดึงข้อมูลรถ ยี่ห้อ สี ป้ายทะเบียน บัตร จาก [1]
    - server.py
        - บันทึกตำแหน่งโซนของรถได้
        - ส่งข้อมูลรถไปยัง [4]

'''
