import time
import threading

# Laboratório 02-03


def pizzaria(pizza, pedaco, thread_num):
    while pedaco < len(pizza):
        print(f"A THREAD Número {thread_num} está no pedaço {pedaco + 1}")
        time.sleep(3)

        pedaco += 3


pedaco_num = 128

pizza = list(range(pedaco_num))

threads = []

for i in range(3):
    thread = threading.Thread(target=pizzaria, args=(pizza, i, i + 1))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("A pizza acabou !")
