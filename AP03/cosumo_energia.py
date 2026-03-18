print("\n" + "=" * 40)
print("Consumo de Energia")
print("=" * 60 + "\n")

potencia = int(input("Potência do aparelho em Watts: "))
horas_u = int(input("Horas de uso por dia: "))
dias_u = int(input("Dias de uso no mês: "))
preco = float(input("Preço da energia: R$"))

consumo_d = (potencia * horas_u) / 1000
consumo_m = consumo_d * dias_u
custo = consumo_m * preco

print("\n" + "="*60)
print(f"{'RELATÓRIO DE CONSUMO DE ENERGIA':^60}")
print("="*60)
print(f"{'Consumo diário':<20} {'Consumo mensal':<20} {'Custo mensal':<20}")
print(f"{'(kWh)':<20} {'(kWh)':<20} {'(R$)':<20}")
print("-"*60)
print(f"{consumo_d:<20.2f} {consumo_m:<20.2f} {custo:<20.2f}")
print("="*60)