print("\n" + "=" * 60)
print("Boletim Simplificado")
print("=" * 60 + "\n")

n1 = float(input("Informe a nota 1: "))
n2 = float(input("Informe a nota 2: "))
n3 = float(input("Informe a nota 3: "))

total = n1+n2+n3
faltam = 30 - total
media = total / 3

print("\n" + "=" * 60)
print(f"{'BOLETIM SIMPLIFICADO':^60}")
print("=" * 60)
print(f"{'Soma das notas':<20} {'Média':<10} {'Pontos para média máxima':<30}")
print("-" * 60)
print(f"{total:<20.1f} {media:<10.1f} {faltam:<30.1f}")
print("-" * 60)