import csv


# data = list
data = ['toyota', 'red', 'a11', '111', '2022-04-12 15:13:12']
def writetocsv(data):
    with open("2-car-system-in.csv", "a", newline='', encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)
    print('csv saved')

writetocsv(data)

