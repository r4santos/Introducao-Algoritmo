print("\n" + "=" * 50)
print(f"{'Soma Harmônica Simples':^50}")
print("=" * 50)

n = 0
x = 1
s = 0

while n <= 0:
    n = int(input("Informe o valor de N: "))

while x <= n:
    s += 1/x
    x += 1

print (s)