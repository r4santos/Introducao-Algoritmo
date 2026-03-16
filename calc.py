div_loop = True
calc_loop = True

def press_enter(mensagem="Pressione ENTER  para continuar"):
    input(mensagem)
    return True

print("Calculadora")
print()

while calc_loop:
    print("Escolha a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")
    op = int(input("=> "))

    match op:

        case 0:
            calc_loop = False

        case 1:
            x = float(input("Informe o primeiro valor: "))
            y = float(input("Informe o segundo valor: "))
            result = x + y

            print(result)
            press_enter()

        case 2:
            x = float(input("Informe o primeiro valor: "))
            y = float(input("Informe o segundo valor: "))
            result = x - y

            print(result)
            press_enter()    
        
        case 3:
            x = float(input("Informe o primeiro valor: "))
            y = float(input("Informe o segundo valor: "))
            result = x * y

            print(result)
            press_enter()

        case 4:
            x = float(input("Informe o primeiro valor: "))
    
            while div_loop:
                y = float(input("Informe o segundo valor: "))
    
                if y == 0:
                    print("Informe um valor diferente de 0")
                else:
                    div_loop = False
    
            result = x / y
    
            print(result)
            press_enter()

        case _:
            print("Informe um valor válido")
        