import time

# Modo Serial


def download_de_arquivo(nome_arquivo):
    print(f'Iniciando o download de {nome_arquivo}')
    time.sleep(2)
    print(f'{nome_arquivo} acabou de ser baixo !')


def download_serial(arquivos):
    inicio = time.time()
    for arquivo in arquivos:
        download_de_arquivo(arquivo)
        fim = time.time()
        print(f"Total de tempo: {fim - inicio } seg")


if __name__ == "__main__":
    lista_arquivos = [f"Arquivo(i).txt" for i in range(1, 10)]

    print("Serial")
    download_serial(lista_arquivos)
