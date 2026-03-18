print("\n" + "=" * 100)
print(f"{'Planejamento de abastecimento de uma frota':^100}")
print("=" * 100 + "\n")

d_media = float(input("Informe a distância média percorrida em cada entrega (km): "))
m_entregas = int(input("Número médio de entregas realizadas no dia: "))
dias_trabalhados = int(input("Número de dias de trabalho na semana: "))
consumo_m = float(input("Consumo médio do veículo em quilômetros por litro (km/l): "))
preco_comb = float(input("Preço do combustível: R$"))

dist_dia = d_media * m_entregas
dist_semana = dist_dia * dias_trabalhados
comb_nec = dist_semana * consumo_m
custo_total = comb_nec * preco_comb

print("\n" + "=" * 100)
print(f"{'PLANEJAMENTO DE ABASTECIMENTO DE UMA FROTA':^100}")
print("=" * 100)
print(f"{'Distância Diária':<20} {'Distância Semanal':<20} {'Combustível Necessário':<25} {'Custo Semanal de Combustível':<35}")
print(f"{'km':<20} {'km':<20} {'Litros':<25} {'R$':<25}")
print("-" * 100)
print(f"{dist_dia:<20.1f} {dist_semana:<20.1f} {comb_nec:<25.1f} {custo_total:<25.2f}")
print("-" * 100)