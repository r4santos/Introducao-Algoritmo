print("\n" + "=" * 50)
print(f"{'Somar até Valor de Parada':^50}")
print("=" * 50)

x = 1
s = 0
n = 1

while n != 0:
    n = int(input(f"Informe o {x}º número: "))
    
    if n == 0:
        x -= 1
        break
    
    s += n
    x += 1

print(f"\nA soma de todos os números informados é: {s}\nA quantidade de números informados foi: {x}")