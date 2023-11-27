import multiprocessing
from queue import Queue


def is_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True


def task_generator(queue):
    for num in range(100001, 1000000, 2):
        queue.put(num)


def worker(queue_in, result_counter):
    while True:
        try:
            num = queue_in.get_nowait()
        except queue.Empty:
            break
        if is_primo(num):
            result_counter.value += 1


if __name__ == '__main__':
    task_queue = Queue()
    result_counter = multiprocessing.Value('i', 0)

    task_process = multiprocessing.Process(
        target=task_generator, args=(task_queue,))
    task_process.start()
    task_process.join()

    num_processes = multiprocessing.cpu_count()
    processes = []

    for _ in range(num_processes):
        process = multiprocessing.Process(
            target=worker, args=(task_queue, result_counter))
        processes.append(process)
        process.start()

        for process in processes:
            process.join()

        print(f"Total de números primos de 6 dígitos: {result_counter.value}")
