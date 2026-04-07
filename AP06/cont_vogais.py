print("\n" + "=" *30)
print(f"{'Contagem Vogais':^30}")
print("=" *30)

vogal = 0

palavra = str(input("Informe a palavra: "))

for letra in palavra:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        vogal += 1

print(f"A palavra tem {vogal} vogal(is)")