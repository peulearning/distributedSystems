import threading
import time

def contar(max):
    cont = 0
    while cont < max:
        cont += 1

MAX = 500_000_000
inicio = time.time()
contar(MAX)
fim = time.time()

print(f'Tempo Gasto - Sequencial: {fim-inicio}')

## versão com 2 threads

threads = []
inicio = time.time()
for i in range(2):
    t = threading.Thread(target=contar, args=(MAX/2,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

fim = time.time()

print(f'Tempo Gasto - 2 Threads: {fim-inicio}')

## versão com 5 threads

threads = []
inicio = time.time()
for i in range(5):
    t = threading.Thread(target=contar, args=(MAX/5,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

fim = time.time()

print(f'Tempo Gasto - 5 Threads: {fim-inicio}')

