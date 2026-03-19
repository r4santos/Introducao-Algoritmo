print("\n" + "=" * 40)
print(f"{'Número Dentro de um Intervalo':^40}")
print("=" * 40)

loop = True

while loop:
    num = int(input("Informe o valor (99 pra sair): "))

    if num == 99:
        loop = False
    elif num >= 10 and num <= 20:
        print("Número dentro do intervalo")
    else:
        print("Número fora do intervalo")