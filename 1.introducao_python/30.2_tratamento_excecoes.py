# Capturando a exceção que é devolvida
try:
    x = int(input('Digite um número: '))
    print(5/x)
except Exception as a:
    print(a)