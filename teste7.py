from multiprocessing import JoinableQueue, Process

PROCESS = 3
MAX = 100


def add(queue: JoinableQueue, results: JoinableQueue):
    while True:
        value = queue.get()

        if value is None or value == MAX:
            queue.put(None)
            return

        queue.put(value + 1)
        results.put(value + 1)


if __name__ == '__main__':
    queue = JoinableQueue()
    queue.put(0)

    results = JoinableQueue()

    plist = []

    for i in range(PROCESS):
        process = Process(target=add, args=(queue, results))
        process.start()
        plist.append(process)

    for process in plist:
        process.join()

    size = results.qsize()

    print(f'done with {size} elements.')

    for _ in range(size):
        print(results.get())
