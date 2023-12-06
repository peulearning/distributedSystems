import threading

num_threads = 5
lock = threading.Lock()
lista = []


def add_values(start, end):
    with lock:
        lista.extend(range(start, end))


threads = [threading.Thread(target=add_values, args=(
    i*100//num_threads + 1, (i+1)*100//num_threads))for i in range(num_threads)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f'Conteúdo da Lista: ', sorted(lista))
