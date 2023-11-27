import threading


def atravessar_rua(pedestre):
    print(f"{pedestre} INICIOU travessia !")
    print(f"{pedestre} FINALIZA travessia.")


threads = []

for i in range(1, 4):
    t = threading.Timer(2 * i, atravessar_rua, args=(i, ))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"TODAS travessias CONCLUIDAS")
