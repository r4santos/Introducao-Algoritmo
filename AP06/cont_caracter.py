print("\n" + "=" *30)
print(f"{'Contagem de Caractere':^30}")
print("=" *30)

aparece = 0

palavra = str(input("Informe a palavra: "))
caractere = str(input("Informe o caractere: "))

for letra in palavra:
    if letra == caractere:
        aparece += 1

if aparece == 0:
    print("O caractere não aparece na palavra")
else:
    print(f"O caractere aparece {aparece} vez(es) na palavra")