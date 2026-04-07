print("\n" + "=" *30)
print(f"{'Maior Valor':^30}")
print("=" *30)

lista = []
c = 0
maior = None

while c < 5:
    x = float(input(f"Informe o {c+1}º valor: "))
    lista.append(x)
    c += 1

for valor in lista:
    if maior == None or valor > maior:
        maior = valor

print(maior)