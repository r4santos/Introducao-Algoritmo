# Programa simples com entrada e saída
print("=== Calculadora de Idade ===")
print()

# Entrada de dados
nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite o ano que você nasceu: "))

# Processamento
ano_atual = 2026
idade = ano_atual - ano_nascimento

# Saída
print()
print(f"Olá, {nome}!")
print(f"Você tem {idade} anos em {ano_atual}.")