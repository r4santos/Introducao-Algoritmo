print("\n" + "=" * 60)
print(f"{'Controle de Acesso ao Laboratório':^60}")
print("=" * 60)


average = int(input("Informe a idade: "))
frequency = float(input("Percentual de frequência: "))

if frequency < 75:
    print("Reprovado por falta")
elif average >= 60:
    print("Aprovado")
elif average >= 40:
    print("Recuperação")
elif average < 40:
    print("Reprovado por nota")