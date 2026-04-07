print("\n" + "=" *30)
print(f"{'Palindrom':^30}")
print("=" *30)

e = True
palavra = str(input("Informe uma palavra: "))

for letra in range(0, len(palavra)):
    if palavra[letra] != palavra[len(palavra) - letra - 1]:
        e = False

if e:
    print("É palíndromo")
else:
    print("Não é palíndromo")