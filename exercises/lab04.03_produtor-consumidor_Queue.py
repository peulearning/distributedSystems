import multiprocessing
import random
import time

def produtor(q):
    for i in range(10):
        v = i+1
        print(f'Valor Produzido: {v}')
        q.put(v)
        time.sleep(1)
    q.put(None)

def consumidor(q,id):
    while True:
        v = q.get()
        if v == None:
            q.put(None)
            return
        print(f'Consumidor {id} coletou: {v}')
        time.sleep(20)
        r = v ** 0.5
        print(f'Consumidor {id} processou item: {v} => result: {r:.3}')
        # r = v ** 100

q = multiprocessing.Queue(maxsize=4)
processos = []

p_produtor = multiprocessing.Process(target=produtor, args=(q,))
p_produtor.start()
processos.append(p_produtor)

for i in range(3):
    p_consumidor = multiprocessing.Process(target=consumidor, args=(q,i+1))
    p_consumidor.start()
    processos.append(p_consumidor)

for p in processos:
    p.join()

print('FINALIZADO')

