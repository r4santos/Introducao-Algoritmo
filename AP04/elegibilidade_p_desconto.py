print("\n" + "=" * 60)
print(f"{'Elegibilidade p/ Desconto':^60}")
print("=" * 60)

age = int(input("Informe a idade do cliente: "))
value = float(input("Valor da compra: R$"))

if age >= 60 or value > 200:
    print("Cliente elegível para desconto")
else:
    print("Cliente sem desconto")