import time
import threading

# Laboratório 02-01

# Função que simula o download de um arquivo (5 segundos)


def download_file(file_name):
    print(f"Iniciando o download de {file_name}")
    time.sleep(5)
    print(f"Download de {file_name} concluído")

# Modo Serial


def download_serial(files):
    start_time = time.time()
    for file in files:
        download_file(file)
    end_time = time.time()
    print(f"Tempo total em modo serial: {end_time - start_time} segundos")

# Modo Concorrente


def download_concurrent(files):
    start_time = time.time()
    threads = []

    for file in files:
        thread = threading.Thread(target=download_file, args=(file,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Tempo total em modo concorrente: {end_time - start_time} segundos")


if __name__ == "__main__":
    file_list = [f"file{i}.txt" for i in range(1, 11)]

    print("Modo Serial:")
    download_serial(file_list)

    print("\nModo Concorrente:")
    download_concurrent(file_list)
