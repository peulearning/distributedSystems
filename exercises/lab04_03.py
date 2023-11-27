import multiprocessing
import time
import math


def produtor(queue):
    for i in range(1, 11):
        time.sleep(1)  # Produção
        queue.put(i)
    queue.put(None)  # Finaliza


def consumidor(queue):
    while True:
        valor = queue.get()
        if valor is None:
            break

        time.sleep(10)

        raiz_quadrada = math.sqrt(valor)
        print(
            f"Consumidor - {multiprocessing.current_process().name}: Valor={valor},Raiz Quadrada={raiz_quadrada}")

    queue = multiprocessing.Queue(maxsize=4)

    produtor_process = multiprocessing.Process(target=produtor, args=(queue,))
    produtor_process.start()

    consumidores = []

    for i in range(3):
        consumidor_process = multiprocessing.Process(
            target=consumidor, args=(queue,))
        consumidores.append(consumidor_process)
        consumidor_process.start()

    produtor_process.join()

    for consumidor_process in consumidores:
        consumidor_process.join()

    print("FINISH")
