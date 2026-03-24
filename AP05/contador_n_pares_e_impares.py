print("\n" + "=" * 50)
print(f"{'Contador de Números Pares e Ímpares':^50}")
print("=" * 50)

x = 1
p = 0
i = 0

while x <= 10:
    n = float(input(f"Informe o {x}º número: "))
    
    if n % 2 == 0:
        p += 1
    else:
        i += 1

    x += 1


print(f"\nForam inseridos:\n{p} números pares\n{i} números ímpares")