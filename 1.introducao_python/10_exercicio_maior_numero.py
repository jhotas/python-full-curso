# Receba 3 numeros inteiros e exiba o maior deles

num1 = int(input('Digite o 1º numero: '))
num2 = int(input('Digite o 2º numero: '))
num3 = int(input('Digite o 3º numero: '))

print(f'\nNúmeros digitados: {num1} {num2} {num3}')

if num1 > num2 and num1 > num3:
    print(f'O maior número é o {num1}')
elif num2 > num1 and num2 > num3:
    print(f'O maior número é o {num2}')
else:
    print(f'O maior número é o {num3}')