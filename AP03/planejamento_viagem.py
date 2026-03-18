print("\n" + "=" * 40)
print("Planejamento de Viagem")
print("=" * 40 + "\n")

distancia = float(input("Informe a distância (km): "))
consumo =  float(input("Informe o consumo do carro (km/l):"))
price = float(input("Informe o preço do combustível: R$"))

litros = distancia / consumo
custo = litros * price

print("\n" + "=" * 40)
print(f"{'PLANEJAMENTO DE VIAGEM':^40}")
print("=" * 40)
print(f"{'Litros necessários':<20} {'Custo estimado':20}")
print(f"{'(L)':<20} {'(R$)':20}")
print("-" * 40)
print(f"{litros:<20.2f} {custo:<20.2f}")
print("-" * 40)