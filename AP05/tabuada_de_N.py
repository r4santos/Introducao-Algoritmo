print("\n" + "=" * 30)
print(f"{'Tabuada de N':^30}")
print("=" * 30)

i = 1
n = 0

while n < 1:
    n = int(input("Informe o valor de N: "))

while i <= 10:
    r = n * i
    print(f"{n} x {i} = {r}")
    i += 1