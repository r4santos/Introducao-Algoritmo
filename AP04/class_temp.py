print("\n" + "=" * 60)
print(f"{'Temperatura Atual (Celsius)':^60}")
print("=" * 60)

loop = True

while loop:
    temp = float(input("Informe o valor (digite 99 para encerrar): "))

    if temp == 99:
        loop = False
    elif temp < 10:
        print("Temperatura baixa")
    elif temp <= 25:
        print("Temperatura agradável")
    else:
        print("Temperatura alta")