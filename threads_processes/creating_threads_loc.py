import time as tim
from threading import Thread


def do_work():
    print("Starting work")
    i = 0 
    for _ in range(2000000): 
        i+=1
    print("Finished work")
    

for _ in range(5):
    t = Thread(target=do_work, args=())
    t.start