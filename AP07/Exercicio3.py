n = 0
ultimo = 1

while n <= 0:
    n = int(input("Valor inteiro positivo de N: "))

for linha in range(0, n):
    lista = ""
    soma = 0
    maior = 0
    mult3 = 0
    for numLinha in range(0, linha+1):
        lista += str(ultimo) + " "
        soma += ultimo
        if ultimo > maior:
            maior = ultimo
        if ultimo % 3 == 0:
            mult3 += 1
        ultimo += 1

    print(f"{lista} | soma = {soma} | maior {maior} | múltiplos de 3 = {mult3}")