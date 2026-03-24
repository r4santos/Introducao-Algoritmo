print("\n" + "=" * 50)
print(f"{'Maior e Menor Valor Encontrado':^50}")
print("=" * 50)

x = 1
maior = None
menor = None

while x <= 8:
    n = int(input(f"Informe o {x}º número: "))
    
    if maior is None:
        maior = n
    elif n > maior:
        maior = n
    
    if menor is None:
        menor = n
    elif n < menor:
        menor = n

    x += 1


print(f"\nDos números informados temos:\nMenor valor: {menor}\nMaior valor: {maior}")