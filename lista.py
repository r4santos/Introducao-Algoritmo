import math

print("\n" + "=" * 50)
print(f"{'Maior e Menor Valor Encontrado':^50}")
print("=" * 50)

x = 1
a = []

while x <= 8:
    n = int(input(f"Informe o {x}º número: "))
    
    a.append(n)

    x += 1

menor = min(a)
maior = max(a)

print(f"\nDos números informados temos:\nMenor valor: {menor}\nMaior valor: {maior}")