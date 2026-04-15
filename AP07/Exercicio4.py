turmas = 0

while turmas < 1:
    turmas = int(input("Número de turmas: "))

for turma in range(0, turmas):
    alunos = 0
    total_medias = 0
    aprovados = 0
    reprovados = 0
    recuperacao = 0
    while alunos < 1:
        alunos = int(input("Número de alunos: "))
    
    for aluno in range(0, alunos):
        n1 = -1
        n2 = -1
        while n1 < 0 or n1 > 10:
            n1 = float(input("Nota 1: "))
        while n2 < 0 or n2 > 10:
            n2 = float(input("Nota 2: "))
        media = (n1 + n2) / 2
        total_medias += media
        if media >= 7:
            print("Aprovado")
            aprovados += 1
        elif media >= 5:
            print("Recuperação")
            recuperacao += 1
        else:
            print("Reprovado")
            reprovados += 1

    media_geral = total_medias / alunos
    print(f"Média geral: {media_geral}\nAprovados: {aprovados}\nRecuperação: {recuperacao}\nReprovados: {reprovados}")