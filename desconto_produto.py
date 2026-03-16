print("Calcular desconto de um produto\n")

p = float(input("Informe o preço do produto: "))
d = float(input("Informe a porcentagem de desconto: "))

pd = p - (p * (d/100))

print(f"O valor final do produto é R${pd}")