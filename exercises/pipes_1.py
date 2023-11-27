import multiprocessing
import time


def ping(conn, parou):
    while not parou.is_set():
        time.sleep(1)
        r = conn.recv()
        if r == 'PONG':
            print(r)
            conn.send('PING')


def pong(conn, parou):
    while not parou.is_set():
        time.sleep(1)
        r = conn.recv()
        if r == 'PING':
            print(r)
            conn.send('PONG')


c1, c2 = multiprocessing.Pipe()
parou = multiprocessing.Event()

p_ping = multiprocessing.Process(target=ping, args=(c1, parou))
p_pong = multiprocessing.Process(target=pong, args=(c2, parou))
p_ping.start()
p_pong.start()

c1.send('PING')

stop = input()
parou.set()
