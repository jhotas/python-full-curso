def soma_numeros(**kwargs):
    x = kwargs.get('test6')
    if x:
        print('Foi passado')
        print(x)
    else:
        print('Não foi passado')

soma_numeros(test1 = 1, test2 = 2, test3 = 3)