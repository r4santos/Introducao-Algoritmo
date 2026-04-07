print("\n" + "=" *30)
print(f"{'Moldura Numérica':^30}")
print("=" *30)

n = -1
while n < 1:
    n = int(input("Informe o valor de N:"))

for x in range(0, n):
    linha = ""
    for y in range(0, n):
        if x == 0 or x == n - 1 or y == 0 or y == n - 1:
            linha += "1"
        else: 
            linha += "0"
    print(linha)
