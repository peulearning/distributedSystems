import multiprocessing
import time


def imprimir_numero(num):
    for i in range(num):
        time.sleep(1)
        print(f'Número: {i}')


if __name__ == '__main__':
    # Criando Processo
    processo = multiprocessing.Process(target=imprimir_numero, args=(3,))

    # Iniciar processo
    processo.start()

    # Aguardar até que o processo termine (opcional )
    processo.join()

    print('Processo principal continuando a execução ...')
