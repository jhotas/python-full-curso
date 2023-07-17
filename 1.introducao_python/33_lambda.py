def teste():
    return lambda *idade: print(idade)

x = teste()
x('Jean', 'Johan')