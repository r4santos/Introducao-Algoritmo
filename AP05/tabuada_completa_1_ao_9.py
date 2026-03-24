print("\n" + "=" * 40)
print(f"{'Tabuada Completa do 1 ao 9':^40}")
print("=" * 40)

v = 1
x = 1
y = 1

while y <= 9:
    x = 1

    print(f"\nTabuada do {v}")
    while x <= 10:
        print(f"{y} x {x} = {y*x}")
        x += 1
    
    v += 1
    y += 1