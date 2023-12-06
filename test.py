import threading

# Lista compartilhada entre as threads
shared_list = []
lock = threading.Lock()

# Função que adiciona valores à lista em ordem crescente


def add_values(start, end):
    with lock:
        shared_list.extend(range(start, end))


# Definindo o número de threads desejado
num_threads = 5

# Criando as threads e iniciando
threads = [threading.Thread(target=add_values, args=(
    i*100//num_threads + 1, (i+1)*100//num_threads)) for i in range(num_threads)]
for thread in threads:
    thread.start()

# Aguardando o término de todas as threads
for thread in threads:
    thread.join()

# Imprimindo o conteúdo da lista ordenada
print("Conteúdo da Lista:", sorted(shared_list))
