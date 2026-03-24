print("\n" + "=" * 60)
print(f"{'Monitoramento de Temperaturas de uma Máquina':^60}")
print("=" * 60)

x = 0
t = 0
n = 1
a = 0
maior = None
menor = None

while n != -1:
    n = float(input(f"Informe o valor da {x+1}ª temperatura: "))
    
    if n == -1:
        break
    
    if n > 80:
        a += 1

    if maior is None:
        maior = n
    elif n > maior:
        maior = n

    if menor is None:
        menor = n
    elif n < menor:
        menor = n

    t += n
    x += 1

m = t / x

print("\n" + "=" * 60)
print(f"{'Resumo das Temperaturas':^60}")
print("-" * 60)
print(f"{'Registradas':<12}{'Maior':>10}{'Menor':>10}{'Média':>10}{'Acima de 80 graus':>18}")
print(f"{'--':<12}{'(Celsius)':^30}{'--':>18}")
print(f"{x:<12}{maior:>10.1f}{menor:>10.1f}{m:>10.1f}{a:>18}")