import threading
import time

def Driving():
    for i in range(10):
        print('driving...', i)
        time.sleep(1)


def Meeting():
    for i in range(10):
        print('meeting...', i)
        time.sleep(0.5)

t1 = time.time()
# normal
# Driving()
# Meeting()




# parallel

task1 = threading.Thread(target=Driving)
task2 = threading.Thread(target=Meeting)

task1.start()
task2.start()

task1.join()
task2.join()

t2 = time.time()
print('Period: ', t2 - t1)