import os

def Clear_Screen():
    os.system("cls")

def Header():
    Clear_Screen()
    print("=" * 60 + f"\n{'Sistema Simples de Caixa Com Validação de Produto':^60}" + "\n" + "=" * 60)

def Press_Enter(mensagem="Pressione ENTER  para continuar"):
    input(mensagem)
    return True    

loop = True
menu1 = 6
total_vendido = 0
total_vendas = 0
total_lanches = 0
total_bebidas = 0
total_sobremesas = 0

while loop:
    if menu1 == 0:
        loop = False
        break

    while menu1 > 5 or menu1 < 0:

        Header()
        print("\n1 - Registrar venda\n2 - Mostrar total vendido\n3 - Mostrar quantidade de vendas\n4 - Mostrar valor médio das vendas\n5 - Mostrar quantidade vendida por tipo de produto\n0 - Encerrar sistema")
        menu1 = int(input("=> "))

    if menu1 == 1:
        menu1 = 6
        menu_venda = 4
        qntd = 0
        venda = 0
        while menu_venda > 3 or menu_venda < 1:
            Header()
            print("-" * 60 + "\n1 - Lanche\n2 - Bebida\n3 - Sobremesa")
            menu_venda = int(input("=> "))
        
        while qntd <= 0:
            qntd = int(input("Informe a quantidade do produto vendida: "))

        if menu_venda == 1:
            total_lanches += qntd
        elif menu_venda == 2:
            total_bebidas += qntd
        elif menu_venda == 3:
            total_sobremesas += qntd

        while venda <= 0:
            venda = float(input("Informe o valor da unidade: R$"))
        
        total_vendido += venda * qntd
        total_vendas += 1

    elif menu1 == 2:
        menu1 = 6
        Header()
        print("-" * 30)
        print(f"|{'Total Vendido':^28}|")
        print(f"|{f'R${total_vendido:.2f}':^28}|")
        print("-" * 30)
        Press_Enter()

    elif menu1 == 3:
        menu1 = 6
        Header()
        print("-" * 30)
        print(f"|{'Quantidade Vendas':^28}|")
        print(f"|{total_vendas:^28}|")
        print("-" * 30)
        Press_Enter()

    elif menu1 == 4:
        menu1 = 6
        Header()
        print("-" * 30)
        print(f"|{'Valor Médio - Vendas':^28}|")
        print(f"|{f'R${media_vendas:.2f}':^28}|")
        print("-" * 30)
        Press_Enter()

    elif menu1 == 5:
        menu1 = 6
        Header()
        print("-" * 30)
        print(f"|{'Quantidade Vendas':^28}|")
        print(f"|{'Lanche':^9}{'Bebida':^9}{'Sobremesa':^10}|")
        print(f"|{total_lanches:^9}{total_bebidas:^9}{total_sobremesas:^10}|")
        print("-" * 30)
        Press_Enter()

    media_vendas = total_vendido / total_vendas

Clear_Screen()
print("=" * 120)
print(f"{'Relatório Final':^120}")
print("=" * 120 + "\n")
print(f"{'Total Vendido':^20}{'Total Vendas':^20}{'Média Vendas':^20}{'Total Lanches':^20}{'Total Bebidas':^20}{'Total Sobremesas':^20}")
print(f"{f'R${total_vendido:.2f}':^20}{total_vendas:^20}{f'R${media_vendas:.2f}':^20}{total_lanches:^20}{total_bebidas:^20}{total_sobremesas:^20}")