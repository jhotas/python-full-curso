# Receba um número e mostre a tabuada completa dele usando o laço for

n1 = int(input('Digite um número: '))

for x in range(0, 11):
    print(f'{n1} x {x} = {n1*x}')