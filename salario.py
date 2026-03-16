print("Calcular salário")
print()

name = input("Informe o nome do funcionário: ")
salary = float(input("Informe o salário: "))
porcent = float(input("Informe o perncentual de bônus: "))

x = salary + (salary * (porcent/100))

print(f"O funcionário {name} \n Deve receber: R${x:.2f}")