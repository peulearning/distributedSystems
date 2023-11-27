import multiprocessing
from multiprocessing import Pool, Manager


def is_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


def gerar_numeros_impares(q_tarefas):
    for i in range(100001, 1000000, 2):
        q_tarefas.put(i)
    q_tarefas.put(None)


def processar_tarefa(numero, resultados):
    if numero is not None and is_primo(numero):
        resultados.append(numero)


if __name__ == "__main__":
    manager = Manager()
    resultados = manager.list()
    q_tarefas = multiprocessing.Queue()

    # Iniciar processo para gerar números ímpares
    p_produtor = multiprocessing.Process(
        target=gerar_numeros_impares, args=(q_tarefas,))
    p_produtor.start()

    # Usar Pool para processar tarefas
    with Pool(processes=multiprocessing.cpu_count()) as pool:
        while True:
            numero = q_tarefas.get()
            if numero is None:
                break
            pool.apply_async(processar_tarefa, args=(numero, resultados))

        # Aguardar até que todas as tarefas sejam concluídas
        p_produtor.join()
        pool.close()
        pool.join()

    # Imprimir resultados
    print("Quantidade de números primos de 6 dígitos:", len(resultados))
    print('FINALIZADO')
