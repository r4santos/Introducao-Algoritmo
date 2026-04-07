print("\n" + "=" *50)
print(f"{'Contador de Blocos de Palavras':^50}")
print("=" *50)

total_palavras = 0
verif = 0

texto = str(input("Informe o texto: "))

for caractere in range(0, len(texto)):
    if verif > 0 and verif < 2:
        total_palavras += 1

    if texto[caractere] != " ":
        verif += 1
    else:
        verif = 0

print(f"Quantidade de palavras: {total_palavras}")