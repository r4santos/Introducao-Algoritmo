print("\n" + "=" *50)
print(f"{'Analisador de Senha Textual':^50}")
print("=" *50)

cont = 0
letra_maiuscula = 0
letra_minuscula = 0
num = 0
caractere_especial = 0
senha_forte = False

senha = str(input("Informe sua senha: "))

for caractere in range(0, len(senha)):
    cont += 1
    if senha[caractere].isupper():
        letra_maiuscula += 1
    elif senha[caractere].islower():
        letra_minuscula += 1
    elif senha[caractere].isdigit():
        num += 1
    else:
        caractere_especial += 1

if cont > 7 and letra_maiuscula > 0 and letra_minuscula > 0 and num > 0 and caractere_especial > 0:
    senha_forte = True

print("\n" + "=" *50)
print(f"{'Resumo':^50}")
print("=" *50)
print(f"Quantidade de caracteres: {cont}")
print(f"Letras maiúsculas: {letra_maiuscula}")
print(f"Letras minúsculas: {letra_minuscula}")
print(f"Digitos: {num}")
print(f"Caracteres especiais: {caractere_especial}")
print(f"Senha forte: {senha_forte}")