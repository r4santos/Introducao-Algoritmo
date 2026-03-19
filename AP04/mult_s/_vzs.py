print("\n" + "=" * 60)
print(f"{'Multiplicação sem utilizar *':^60}")
print("=" * 60)

v1 = float(input("Informe o valor 1: "))
v2 = float(input("Informe o valor 2: "))

def contar_casas_decimais(num):
    s = str(num)
    if '.' in s:
        return len(s.split('.')[1])
    return 0

# Caso zero
if v1 == 0 or v2 == 0:
    resultado = 0
else:
    # Determinar sinal do resultado
    sinal_negativo = (v1 < 0) != (v2 < 0)
    
    # Trabalhar com valores positivos
    v1_abs = abs(v1)
    v2_abs = abs(v2)
    
    # Contar casas decimais
    casas1 = contar_casas_decimais(v1_abs)
    casas2 = contar_casas_decimais(v2_abs)
    
    # Converter para inteiros
    v1_int = int(v1_abs * (10 ** casas1))
    v2_int = int(v2_abs * (10 ** casas2))
    
    # Multiplicação por adição repetida (com otimização de bit shifting)
    resultado_int = 0
    
    # Usar o menor como iterador para menos iterações
    if v2_int < v1_int:
        v1_int, v2_int = v2_int, v1_int
    
    # Multiplicação por adição repetida
    while v2_int > 0:
        resultado_int += v1_int
        v2_int -= 1
    
    # Ajustar para decimais
    casas_totais = casas1 + casas2
    resultado = resultado_int / (10 ** casas_totais)
    
    # Aplicar sinal
    if sinal_negativo:
        resultado = -resultado

print(resultado)