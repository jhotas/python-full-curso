# Receba 4 notas de um aluno e exiba se ele foi aprovado (nota maior ou igual a 6),
# se ele ficou de recuperação ( nota maior ou igual a 4) ou se ele foi reprovado
# (nota menor do que 4)

nota1 = float(input('Digite a 1a nota do aluno: \n'))
nota2 = float(input('Digite a 2a nota do aluno: \n'))
nota3 = float(input('Digite a 3a nota do aluno: \n'))
nota4 = float(input('Digite a 4a nota do aluno: \n'))

media = (nota1 + nota2 + nota3+ nota4) / 4

if media >= 6:
    print(f'A media do aluno foi {media}, o aluno foi aprovado! :)')
elif media >= 4:
    print(f'A media do aluno foi {media}, o aluno ficou de recuperação. :/')
else:
    print(f'A media do aluno foi {media}, o aluno foi reprovado. :(')