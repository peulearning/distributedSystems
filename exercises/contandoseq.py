def contador_numero():
    contador = 0
    while contador < 5000000:
        contador += 1
    return contador


for i in range(1, contador_numero() + 1):
    print("Contagem:", i)
