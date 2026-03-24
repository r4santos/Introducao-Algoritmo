print("\n" + "=" * 60)
print(f"{'Controle de Vendas de uma Loja':^60}")
print("=" * 60)

x = 1
t = 0
n = 1

while n != 0:
    n = float(input(f"Informe o valor da {x}ª venda: "))
    
    if n == 0:
        x -= 1
        break
    
    t += n
    x += 1

m = t / x

print("\n" + "=" * 60)
print(f"{'Resumo das Vendas':^60}")
print("-" * 60)
print(f"{'Valor Total':<15} {'Quantidade Registrada':<30} {'Valor Médio':<15}")
print(f"{'R$':<15} {'--':<30} {'R$':<15}")
print(f"{t:<15.2f} {x:<30} {m:<15.2f}")