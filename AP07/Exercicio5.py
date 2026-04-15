mesas = 0
produto1 = 0
produto2 = 0
produto3 = 0
total_mesas = 0

while mesas < 1:
    mesas = int(input("Mesas atendidas: "))

for mesa in range(0, mesas):
    qntd_pedidos = 0
    invalido = 0
    total_mesa = 0
    
    qntd_pedidos = int(input("Pedidos feitos: "))
    
    if qntd_pedidos > 0:
        for pedido in range(0, qntd_pedidos):
            cod_produto = int(input("Código do produto: "))
            if cod_produto < 0 or cod_produto > 3:
                print("Código inválido e pedido ignorado!")
                invalido += 1
            else:
                if cod_produto == 1:
                    total_mesa += 18
                    produto1 += 1
                elif cod_produto == 2:
                    total_mesa += 6
                    produto2 += 1
                else:
                    total_mesa += 9
                    produto3 += 1
        print(f"Total da mesa: R${total_mesa:.2f}\nItens válidos: {qntd_pedidos - invalido}")

    total_mesas += total_mesa

print(f"Faturamento total: R${total_mesas:.2f}\nQuantidade vendida de cada produto:\nProduto 1: {produto1}\nProduto 2: {produto2}\nProduto 3: {produto3}")