print("\n" + "=" *30)
print(f"{'Prefixos Palíndromos':^30}")
print("=" *30)

palavra = str(input("Informe a palavra: "))
prefixo = ""

for letra in range(0, len(palavra)):
    e = True
    prefixo += palavra[letra]

    for x in range(0, len(prefixo)):
        if prefixo[x] != prefixo[len(prefixo) - x - 1]:
            e = False
    if e:
        print(prefixo)
