import threading

count = 0
lock = threading.Lock()
num_threads = 2


def increment_and_print():
    global count
    with lock:
        count += 1
        print(count)


threads = [threading.Thread(target=increment_and_print)
           for _ in range(num_threads)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
