import threading

# Variável compartilhada entre as threads
count = 0
lock = threading.Lock()

# Função que incrementa o contador e imprime


def increment_and_print():
    global count
    with lock:
        count += 1
        print(count)


# Criando as threads
num_threads = 100  # Defina o número desejado de threads
threads = [threading.Thread(target=increment_and_print)
           for _ in range(num_threads)]

# Iniciando as threads
for thread in threads:
    thread.start()

# Aguardando o término de todas as threads
for thread in threads:
    thread.join()
