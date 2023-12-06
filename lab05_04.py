# Pool de 4 Thread
# Numeros  aleatórios entre 1 e 100
# produz 10 tasks
# Pool de 8 threads consumidoras de task ( p/ cada nmr obtido devolve o restulado a lsista e divisores inteiros m exe=ceto 1 e ele própio )

# Printar relação das tasks e resultados.

from concurrent.futures import ThreadPoolExecutor
import random
import threading

tasks_queue = []
results_dict = {}
lock = threading.Lock()


def produz_task():
    for _ in range(10):
        sort = random.randint(1, 100)
        with lock:
            tasks_queue.append(sort)
        print(f'{threading.current_thread().name} => {sort}')


def consumir_task(task):
    divisores = [n for n in range(2, task) if task % n == 0]
    with lock:
        results_dict[(threading.current_thread().name, task)] = divisores
    print(f'{threading.current_thread().name} - Resultados {task}: {divisores}')


workers_produtores = ThreadPoolExecutor(4)

futures_produtores = workers_produtores.submit(produz_task)


workers_consumidores = ThreadPoolExecutor(8)

futures_consumidores = list(
    workers_consumidores.map(consumir_task, tasks_queue))


workers_produtores.shutdown()


workers_consumidores.shutdown()

for (produtor_name, task), divisores in results_dict.items():
    print(f'{produtor_name} - Resultados {task}: {divisores}')
