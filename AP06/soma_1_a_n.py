print("\n" + "=" *30)
print(f"{'Soma de 1 até N':^30}")
print("=" *30)

total = 0

n = int(input("Informe o valor de N: "))
m = n - 1

while m < n:
    print("\nO valor de M deve ser maior que o de N:")
    m = int(input("Informe o valor para M: "))

for x in range(n, m + 1):
    total += x

print(total)