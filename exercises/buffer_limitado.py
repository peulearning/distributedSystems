import threading
import time

# Tamanho do buffer
tamanho_buffer = 10

# Número de pedaços de pizza
num_pedacos_pizza = 128

# Variável para acompanhar a próxima fatia disponível
proxima_fatia = 0

# Inicialização de semáforos e locks
mutex = threading.Lock()
pedacos_disponiveis = threading.Semaphore(0)
espaco_no_buffer = threading.Semaphore(tamanho_buffer)


def produzir_pizza():
    global proxima_fatia
    while True:
        # Demora aproximadamente 1 segundo para produzir uma fatia
        time.sleep(1)
        fatia = proxima_fatia
        mutex.acquire()
        if proxima_fatia < num_pedacos_pizza:
            proxima_fatia += 1
            mutex.release()
            espaco_no_buffer.acquire()  # Verifica se há espaço no buffer
            print(f"Produtor está produzindo a fatia {fatia}")
            pedacos_disponiveis.release()  # Incrementa o contador de pedaços disponíveis
        else:
            mutex.release()
            break


def consumir_pizza(id):
    while True:
        pedacos_disponiveis.acquire()  # Verifica se há pedaço disponível
        mutex.acquire()
        if proxima_fatia > 0:
            proxima_fatia -= 1
            mutex.release()
            espaco_no_buffer.release()  # Incrementa o contador de espaço no buffer
            print(f"Thread {id} está consumindo uma fatia")
            # Demora aproximadamente 3 segundos para comer uma fatia
            time.sleep(3)
        else:
            mutex.release()
            break


# Crie as threads produtoras e consumidoras
threads_produtoras = []
threads_consumidoras = []

for i in range(2):
    thread = threading.Thread(target=produzir_pizza)
    threads_produtoras.append(thread)

for i in range(3):
    thread = threading.Thread(target=consumir_pizza, args=(i,))
    threads_consumidoras.append(thread)

# Inicie as threads
for thread in threads_produtoras:
    thread.start()

for thread in threads_consumidoras:
    thread.start()

# Aguarde as threads terminarem (isso é apenas um exemplo, você pode definir uma condição de parada)
for thread in threads_produtoras:
    thread.join()

for thread in threads_consumidoras:
    thread.join()

print("Todas as threads terminaram de produzir e consumir a pizza.")
