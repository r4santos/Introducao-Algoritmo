print("Calculadora de IMC\n")

name = input("Informe o seu nome: ")
weight = float(input("Informe o seu peso: "))
height = float(input("Informe a sua altura: "))

imc = weight / ( height * height)

print(f"{name} o seu IMC é {imc:.2f}")