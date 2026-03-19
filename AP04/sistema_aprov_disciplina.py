print("\n" + "=" * 60)
print(f"{'Sistema de Aprovação em Disciplina':^60}")
print("=" * 60)


age = int(input("Informe a idade: "))
print("Possui matrícula ativa? \n 1 - Sim\n 2 - Não")
mat_act = int(input("=> "))
print("Possui autorização especial? \n 1 - Sim\n 2 - Não")
auth_spc = int(input("=> "))

if auth_spc == 1:
    print("Acesso permitido")
elif age >= 18 and mat_act == 1:
    print("Acesso permitido")
else:
    print("Acesso negado")