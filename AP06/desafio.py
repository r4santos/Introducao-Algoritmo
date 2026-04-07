import os

def Clear_Screen():
    os.system('cls')

def Header():
    Clear_Screen()
    print("=" *80 + f"\n{'Sistema de Simulação de Investimentos com Juros Compostos':^80}" + "\n" + "=" *80)

def Press_Enter(mensagem="Pressione ENTER  para continuar"):
    input(mensagem)
    return True

# Ciclo do programa
on = True
config = False
simulacao = False
# Variáveis config da simulação
valor_investido = 0
valor_aporte = 0
taxa_juros = None
qntd_meses = 0
# Variáveis p/ executar simulação
valor_ganho = 0
valor_total = 0
soma_saldo = 0
saldo_total = 0
maior_saldo = 0
mes_maior_saldo = 0
# Variável p/ evolução mensal
saldo = 0

while on:
    Header()
    x = int(input("\n1 - Configurar simulação\n2 - Executar simulação\n3 - Mostrar relatório geral\n4 - Mostrar evolução mês a mês\n0 - Encerrar sistema\n=> "))
    match x:
        case 1:
            Header()
            while valor_investido <= 0:
                valor_investido = float(input("Informe o valor investido: R$"))
            while valor_aporte <= 0:
                valor_aporte = float(input("Informe o valor do aporte mensal: R$"))
            while taxa_juros is None:
                taxa_juros = float(input(f"Informe a taxa de juros (em porcentagem): "))
            while qntd_meses < 1:
                qntd_meses = int(input("Informe a quantidade de meses: "))

            config =  True
            Press_Enter()
        case 2:
            if config:
                saldo_total = valor_investido
                maior_saldo = saldo_total
                mes_maior_saldo = 0

                for mes in range(0, qntd_meses):
                    saldo_total = (saldo_total + valor_aporte) * (1 + (taxa_juros / 100))
                    soma_saldo += saldo_total
                    if saldo_total > maior_saldo:
                        maior_saldo = saldo_total
                        mes_maior_saldo = mes + 1

                simulacao = True
                saldo_medio = soma_saldo / qntd_meses
                total_investido = valor_investido + valor_aporte * qntd_meses
                lucro_total = saldo_total - total_investido
                print("Simulação executada com sucesso")
            else:
                print("Deve-se realizar a configuração da simulação")

            Press_Enter()
        case 3:
            Header()
            if simulacao:
                print("\n" + "=" *80)
                print(f"{'Relatório Geral':^80}")
                print("=" *80)
                print(f"{'Valor Inicial':^15}{'Aporte Mensal':^15}{'Taxa de Juros':^15}{'Qntd Meses':^15}{'Total Investido':^15}")
                print(f"{f'R${valor_investido:.2f}':<15}{f'R${valor_aporte:.2f}':<15}{f'{taxa_juros}%':<15}{qntd_meses:<15}{f'R${total_investido:.2f}':<15}")
                print(f"{'Saldo Final':^15}{'Lucro Total':^15}{'Saldo Médio':^15}{'Maior Saldo':^15}{'Mês Maior Saldo':^15}")
                print(f"{f'R${saldo_total:.2f}':<15}{f'R${lucro_total:.2f}':<15}{f'R${saldo_medio:.2f}':<15}{f'R${maior_saldo:.2f}':<15}{mes_maior_saldo:<15}")
            else:
                print("Deve-se realizar a simulação antes de gerar o relatório")
            Press_Enter()
        case 4:
            Header()
            saldo = valor_investido
            for mes in range(0, qntd_meses):
                saldo = (saldo + valor_aporte) * (1 + (taxa_juros / 100))
                print(f"Mês {mes+1}: R${saldo:.2f}")
            Press_Enter()
        case 0:
            on = False
        case _:
            print("Informe um valor válido")

if simulacao:
    Header()
    print("\n" + "=" * 60 + f"\n{'Resumo Final':^60}" + "\n" + "=" * 60)
    print(f"{'Total Investido':^20}{'Saldo Final':^20}{'Lucro Total':^20}")
    print(f"{f'R${total_investido:.2f}':<20}{f'R${saldo_total:.2f}':<20}{f'R${lucro_total:.2f}':<20}")

Press_Enter()