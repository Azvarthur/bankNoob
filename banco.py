valor = int(input("Digite um valor: "))

if valor <= 0:
    print("Digite um valor valido!")
else:
    saque = valor

    v1 = 0
    v2 = 0
    v3 = 0
    v4 = 0
    v5 = 0
    v7 = 0
    while True:
        if valor >= 100:
            while valor >= 100:
                valor = valor - 100
                v7 += 1
        if valor >= 50:
            while valor >= 50:
                valor = valor - 50
                v1 += 1
        elif valor >= 20:
            while valor >= 20:
                valor = valor - 20
                v2 += 1
        elif valor >= 10:
            while valor >= 10:
                valor = valor - 10
                v3 += 1
        elif valor >= 5:
            while valor >= 5:
                valor = valor - 5
                v4 += 1
        elif valor >= 2:
            while valor >= 2:
                valor = valor - 2
                v5 += 1
        elif valor == 0 or valor == 1:
            break

    if valor == 0:
        print(
            f"Foi sacado {saque}, sendo {v7} notasd de 100R$, {v1} notas de 50R$, {v2} notas de 20R$, {v3} notas de "
            f"10R$, {v4} notas de 5R$,"
            f"{v5} notas de 2R$!")
    else:
        print("O valor solicitado deve ser múltiplo de R$ 2, R$ 5, R$ 10, R$ 20, R$ 50 ou R$ 100 reais!")
