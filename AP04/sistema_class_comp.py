print("\n" + "=" * 60)
print(f"{'Sistema de Classificação em uma Competição':^60}")
print("=" * 60)

score = int(input("Informe a pontuação obtida: "))
time = int(input("Informe tempo gasto na prova (min): "))

if score >= 90:
    if time < 120:
        print("Participante destaque da competição")
    else:
        print("Classificação obitda: Ouro")
elif score >= 70:
    print("Classificação obitda: Prata")
elif score >= 50:
    print("Classificação obitda: Ouro")
else:
    print("Sem medalha obtida")