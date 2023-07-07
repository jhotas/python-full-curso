print('REGISTRO NA APP:')
nome = input('Nome: ')
idade = int(input('Idade: '))
cep = (input('CEP: '))

dados = { 'Nome': nome, 'Idade': idade, 'CEP': cep } 

print(f'Seus dados: {dados}')

while True:
  resposta = (input('Digite 1 para confirmar ou 2 para alterar os dados: '))
  if resposta == '1':
      print('Dados armazenados!')
      break
  elif resposta == '2':
    altera_dado = input('Qual dado deseja alterar? (N) Nome (I) Idade (C) CEP')
    if altera_dado == 'N' or altera_dado == 'n':
       nome = input('Nome:')
       print(f'Seus dados: {dados}')
    elif altera_dado == 'I' or altera_dado == 'i':
       idade = input('Idade: ')
       print(f'Seus dados: {dados}')
    elif altera_dado == 'C' or altera_dado == 'c':
       cep = input('CEP: ')
       print(f'Seus dados: {dados}')
    else:
       print('Introduza uma opção válida.')