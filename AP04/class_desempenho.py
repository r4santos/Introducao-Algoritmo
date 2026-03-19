print("\n" + "=" * 60)
print(f"{'Classificação de Desempenho':^60}")
print("=" * 60)

loop = True

while loop:
    note = float(input("Informe a nota final (111 para sair): "))

    if note == 111:
        loop = False
    elif note < 50:
        print("Insuficiente")
    elif note < 70:
        print("Regular")
    elif note < 90:
        print("Bom")
    elif note <= 100:
        print("Excelente")