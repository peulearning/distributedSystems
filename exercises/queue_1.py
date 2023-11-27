import multiprocessing
import time

def ping(q, parou):
    while not parou.is_set():
        time.sleep(1)
        r = q.get()
        if r == 'PONG':
            print(r)
            q.put('PING')

def pong(q, parou):
    while not parou.is_set():
        time.sleep(1)
        r = q.get()
        if r == 'PING':
            print(r)
            q.put('PONG')

q = multiprocessing.Queue()
parou = multiprocessing.Event()

p_ping = multiprocessing.Process(target=ping,args=(q,parou))
p_pong1 = multiprocessing.Process(target=pong,args=(q,parou))
p_pong2 = multiprocessing.Process(target=pong,args=(q,parou))
p_ping.start()
p_pong1.start()
p_pong2.start()

q.put('PING')

stop = input()
parou.set()
