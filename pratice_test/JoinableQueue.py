from multiprocessing import JoinableQueue, Process, cpu_count


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def task_generator(queue):
    for num in range(100001, 1000000, 2):
        queue.put(num)
    # Adiciona marcadores de término para cada processo de trabalho
    for _ in range(num_processes):
        queue.put(None)


def worker(queue_in, queue_out):
    while True:
        num = queue_in.get()
        if num is None:
            break
        if is_prime(num):
            queue_out.put(num)
        queue_in.task_done()


tasks_queue = JoinableQueue()
results_queue = JoinableQueue()

num_processes = cpu_count()

# Inicia o processo de geração de tarefas em paralelo com os processos de trabalho
task_process = Process(target=task_generator, args=(tasks_queue,))
task_process.start()

processes = [Process(target=worker, args=(tasks_queue, results_queue))
             for _ in range(num_processes)]

# Inicia os processos de trabalho
for process in processes:
    process.start()

# Espera até que todas as tarefas tenham sido concluídas
tasks_queue.join()

# Espera até que todos os processos de trabalho tenham terminado
for process in processes:
    tasks_queue.put(None)
for process in processes:
    process.join()

print("Números primos de 6 dígitos:")
while not results_queue.empty():
    print(results_queue.get())
