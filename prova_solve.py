import threading
import queue
import random

# Função produtor


def produtor(fila, total_produzido):
    while total_produzido[0] < 50:
        numero = random.randint(1, 100)
        fila.put(numero)
        total_produzido[0] += 1

# Função separador


def separador(fila, resultados_3, resultados_7, resultados_9, total_separado):
    while total_separado[0] < 50:
        numero = fila.get()
        if numero % 3 == 0:
            resultados_3.append(numero)
        if numero % 7 == 0:
            resultados_7.append(numero)
        if numero % 9 == 0:
            resultados_9.append(numero)
        total_separado[0] += 1

# Função principal


def main():
    fila_produzidos = queue.Queue()
    resultados_3 = []
    resultados_7 = []
    resultados_9 = []
    total_produzido = [0]
    total_separado = [0]

    # Criação das threads
    produtor_thread = threading.Thread(
        target=produtor, args=(fila_produzidos, total_produzido))
    separador_thread = threading.Thread(target=separador, args=(
        fila_produzidos, resultados_3, resultados_7, resultados_9, total_separado))

    # Inicialização das threads
    produtor_thread.start()
    separador_thread.start()

    # Aguarda até que ambas as threads terminem
    produtor_thread.join()
    separador_thread.join()

    # Imprime os resultados
    print("Separador 3:", resultados_3)
    print("Separador 7:", resultados_7)
    print("Separador 9:", resultados_9)


if __name__ == "__main__":
    main()
