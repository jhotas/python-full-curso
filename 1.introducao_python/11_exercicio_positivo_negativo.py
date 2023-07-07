# Receba um número e exiba se ele é positivo ou negativo

num = float(input('Digite um número: '))

if num > 0:
    print('\nO número que digitou é positivo!')
elif num < 0:
    print('\nO número que digitou é negativo!')
else:
    print('\nO número 0 é par... não, é impar... par? impar? Nunca saberemos, auto-destruição em 3...2...1...')