x = [{'Nome': 'Jean', 'Idade': 21}, {'Nome': 'Johan', 'Idade': 12}]

x = list(filter(lambda x: x['Idade'] <= 40, x))
print(x)