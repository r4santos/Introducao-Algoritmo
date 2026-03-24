print("\n" + "=" * 50)
print(f"{'Soma Com Sinais Alternados':^50}")
print("=" * 50)

n = 0
x = 1
s = 0

while n <= 0:
    n = int(input("Informe o valor de N: "))

while x <= n:
    if x % 2 == 0:
        s -= 1/x
    else:
        s += 1/x
    x += 1

print (s)