import multiprocessing
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
    t = multiprocessing.Process(target=contar, args=(MAX/2,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

fim = time.time()

print(f'Tempo Gasto - 2 Processos: {fim-inicio}')

## versão com 5 threads

threads = []
inicio = time.time()
for i in range(4):
    t = multiprocessing.Process(target=contar, args=(MAX/4,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

fim = time.time()

print(f'Tempo Gasto - 4 Processos: {fim-inicio}')

