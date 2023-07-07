# Receba F para feminino e M para masculino e exiba o sexo da pessoa

sexo = input('Você é (M) Masculino | (F) Feminino | (N) Prefiro não dizer: ')


if sexo == 'M' or sexo == 'm':
    print('Você é do sexo masculino!')
elif sexo == 'F' or sexo == 'f':
    print('Você é do sexo feminino!')
elif sexo == 'N' or sexo == 'n':
    print('Sexo indefinido.')
else:
    print('Valor inválido.')