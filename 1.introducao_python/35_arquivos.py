arquivo = open('pessoas.txt', 'a')
i = 0
while True:
    if i > 2:
        break
    arquivo.write(input('Digite o nome da pessoa: ') + ' ' + input('Digite a idade da pessoa: ') + '\n')
    i += 1