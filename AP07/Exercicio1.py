def classificar_multiplo(valor):
    if valor % 3 == 0 and valor % 5 == 0:
        return "múltiplo de ambos (3 e 5)"
    if valor % 3 == 0:
        return "múltiplo de 3"
    if valor % 5 == 0:
        return "múltiplo de 5"
    return "nenhum dos dois"


a = int(input("Informe o valor inteiro de A: "))
b = int(input("Informe o valor inteiro de B: "))

if a > b:
    a, b = b, a

for i in range(a, b + 1):
    print(f"\nNúmero i = {i}")
    print(f"Valores de 1 até {i}:")

    for valor in range(1, i + 1):
        classificacao = classificar_multiplo(valor)
        print(f"{valor}: {classificacao}")