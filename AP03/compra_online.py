print("\n" + "=" * 60)
print("Compra Online")
print("=" * 40 + "\n")

p_produto = float(input("Preço do produto: R$"))
porc_imposto =  float(input("Percentual do imposto (0 a 100): "))
frete = float(input("Valor do frete: R$"))

imposto = p_produto * (porc_imposto / 100)
total = p_produto + imposto + frete

print("\n" + "=" * 40)
print(f"{'RESUMO COMPRA':^40}")
print("=" * 40)
print(f"{'Valor Imposto':<20} {'Valor Total':20}")
print(f"{'(R$)':<20} {'(R$)':20}")
print("-" * 40)
print(f"{imposto:<20.2f} {total:<20.2f}")
print("-" * 40)