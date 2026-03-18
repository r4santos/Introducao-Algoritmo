print("\n" + "=" * 120)
print(f"{'Estimativa de tempo para leitura de um livro':^120}")
print("=" * 120 + "\n")

total_paginas = int(input("Número total de páginas: "))
media_palavras_pg = int(input("Número médio de palavras por página: "))
velocidade_leitura_palavras_min = int(input("Velocidade média de leitura em palavras por minuto: "))
qnt_disp_leitura_dia = int(input("Quantidade de minutos disponíveis para leitura por dia: "))

total_palavras = total_paginas * media_palavras_pg
tempo_total_leitura_min = total_palavras / velocidade_leitura_palavras_min
tempo_total_leitura_hr = tempo_total_leitura_min / 60
dias_estimados_fim = tempo_total_leitura_min / qnt_disp_leitura_dia

print("\n" + "=" * 120)
print(f"{'PLANEJAMENTO DE LEITURA':^120}")
print("=" * 120)
print(f"{'Total de Palavras no Livro':<30} {'Tempo Total de Leitura':<25} {'Tempo Total de Leitura':<25} {'Dias estimados para terminar o livro':<40}")
print(f"{'-':<30} {'Minutos':<25} {'Horas':<25} {'--':<40}")
print("-" * 120)
print(f"{total_palavras:<30} {tempo_total_leitura_min:<25.1f} {tempo_total_leitura_hr:<25.1f} {dias_estimados_fim:<40.0f}")
print("-" * 120)