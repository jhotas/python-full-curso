# Not working yet
cobre = float(input('Digite a quantidade de cobre: '))
prata = float(input('Digite a quantidade de prata: '))
ouro = float(input('Digite a quantidade de ouro: '))

cobre_conv = 0
prata_conv = 0
ouro_conv = 0

if cobre > 100:
    cobre_conv = cobre / 100
    prata_final = cobre_conv

if prata > 100:
    prata_conv = prata / 100
    ouro_final = prata_conv

print(f'Total: {ouro_final}G {prata_final}P {cobre}')