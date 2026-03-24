print("\n" + "=" * 50)
print(f"{'Trângulo Crescente de Números':^50}")
print("=" * 50)

n = int(input("Informe o valor de N: "))
x = 1
p = ""

while x <= n:
    p += str(x)
    x += 1
    print(p)