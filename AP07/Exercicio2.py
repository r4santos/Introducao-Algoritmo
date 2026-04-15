l = 0
c = 0

while l <= 0:
    l = int(input("Informe um valor positivo para Linha: "))

while c <= 0:
    c = int(input("Informe um valor positivo para Coluna: "))

for x in range(1,l+1):
    print(f"\nLinha {x}")
    for y in range(1,c+1):
        produto = x / y
        if produto % 2 == 0:
            poi = "par"
        else:
            poi = "ímpar"
        if produto <= 10:
            faixa = "pequeno"
        elif produto <= 20:
            faixa = "médio"
        else:
            faixa = "grande"
        if produto > 20:
            maior20 = "maior que 20"
        else:
            maior20 = "menor que 20"
        print(f"Linha {x} e coluna {y} -> produto = {produto} -> {poi};{faixa}; {maior20}")