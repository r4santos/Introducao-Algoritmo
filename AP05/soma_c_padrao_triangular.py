print("\n" + "=" * 50)
print(f"{'Soma Com Padrão Triangular':^50}")
print("=" * 50)

n = 0
x = 1
s = 0

while n <= 0:
    n = int(input("Informe o valor de N: "))

while x <= n:
    t = (x*(x+1)) / 2
    s += x/t
    x += 1

print (s)