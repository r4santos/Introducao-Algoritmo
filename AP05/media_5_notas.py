print("\n" + "=" * 30)
print(f"{'Média de 5 Notas':^30}")
print("=" * 30)

i = 1
t = 0

while i <= 5:
    n = float(input(f"Informe a {i}ª nota: "))
    t += n
    i += 1

m = t / 5

print(f"A média das 5 notas é: {m}")