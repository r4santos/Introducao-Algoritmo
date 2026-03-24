print("\n" + "=" * 50)
print(f"{'Retângulo de símbolos':^50}")
print("=" * 50)

l = int(input("Informe a largura do retângulo: "))
a = int(input("Informe a altura do retângulo: "))

while a != 0:
    print("*" * l)
    a -= 1