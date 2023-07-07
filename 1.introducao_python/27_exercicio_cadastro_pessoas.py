# Faça um programa que o usuário possa cadastrar n pessoas, armazenando seu
# nome, idade e altura

pessoas = []
while True:
    decisao = int(input('Digite 1 para cadastrar uma pessoa e 2 para sair: \n'))
    if decisao == 2:
        break
    
    pessoa = { 'Nome': input('Digite o nome: '), 'Idade': input('Digite a idade: '), 'Altura': input('Digite a altura: ') }
    pessoas.append(pessoa)

for pessoa in pessoas:
    print(pessoa)