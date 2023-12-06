import threading

num_threads = 3
lista_alimentada = []
lock = threading.Lock()


def add_value(start, end):
    with lock:
        lista_alimentada.extend(range(start, end))


threads = [threading.Thread(target=add_value, args=(
    i*100//num_threads + 1, (i+1)*100//num_threads))for i in range(num_threads)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("Contéudod da Lista :", sorted(lista_alimentada))
