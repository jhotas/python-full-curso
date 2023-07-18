x = [{'Nome': 'Jean', 'Idade': 21}, {'Nome': 'Johan', 'Idade': 12}]

x = list(map(lambda x: {'Nome': x['Nome'], 'Idade': 'Menor do que 18 anos'} if x['Idade'] < 18 else(x), x))
print(x)