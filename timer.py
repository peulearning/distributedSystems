import threading

# Exemplo de sincronização Timer
# Apresentar dia 01/11/2023


def atravessar_rua(pedestre):
    print(f"Pessoa {pedestre} inicia travessia !")
    print(f"Pessoa {pedestre} conclui a travessia")


threads = []

for i in range(1, 4):
    t = threading.Timer(2 * i, atravessar_rua, args=(i, ))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Todas travessias CONCLUIDAS !")
