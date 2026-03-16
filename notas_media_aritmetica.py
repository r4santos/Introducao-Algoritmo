print("Calculadora de Média Aritmética das Notas\n")

name = input("Informe o seu nome: ")
m = float(input("Informe a primeira nota: "))
n = float(input("Informe a segunda nota: "))
l = float(input("Informe a terceira nota: "))

media = (m + n + l) / 3

print(f"{name} a sua média aritmética é {media:.2f}")