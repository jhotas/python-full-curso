cobre = float(input('Digite a quantidade de cobre: '))
prata = float(input('Digite a quantidade de prata: '))
ouro = float(input('Digite a quantidade de ouro: '))

while cobre >= 100:
    prata += 1
    cobre -= 100

while prata >= 100:
    ouro += 1
    prata -= 100

print(f'Total: {ouro}G {prata}P {cobre}C')