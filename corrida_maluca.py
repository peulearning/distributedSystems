import os
import random
import threading
import time

def run(id, posicoes):
    global fim
    while not fim:
        posicoes[id-1] += 1
        time.sleep(random.random())

fim = 0
threads = []
posicoes = [0 for i in range (5)]

for i in range(5):
    t = threading.Thread(target=run, args=(i+1,posicoes))
    t.start()

while max(posicoes)<78:
    time.sleep(0.1)
    os.system('clear')
    for n in posicoes:
        print('*'*n)

id = posicoes.index(max(posicoes))
empate = posicoes.count(max(posicoes))

fim = 1

for t in threads:
    t.join()

if empate > 1:
    print(f'HOUVE EMPATE')
else:
    print(f'THREAD {id+1} VENCEDOR')
