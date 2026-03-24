print("\n" + "=" * 50)
print(f"{'Monitoramento de Material Radioativo':^50}")
print("=" * 50)

t = 0
i = float(input("Informe a massa inicial em gramas: "))
mi = i

while i > 0.5:
    i /= 2
    t += 50

mf = i

print("\n" + "=" * 60)
print(f"{'Resumo Final':^60}")
print("-" * 60)
print(f"{'Massa Inicial':<20} {'Massa Final':<20} {'Tempo Total':<20}")
print(f"{'g':<20} {'g':<20} {'Seg':<20}")
print(f"{mi:<20.1f} {mf:<20.1f} {t:<20.1f}")