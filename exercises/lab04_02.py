import threading
import time


def imprimir_numero(num):
    for i in range(num):
        time.sleep(1)
        print(f'Número: {i}')


if __name__ == '__main__':
    # Criar uma Thread
    thread = threading.Thread(target=imprimir_numero, args=(3,))

    thread.start()

    thread.join()

    print('Thread principal continuando execução... ')
