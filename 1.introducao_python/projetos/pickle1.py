import pickle

class Pessoa:
    nome = 'Jean'
    idade = 21

class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoas('Johan', 12)

arq = open('arquivo.pkl', 'wb')
pickle.dump(p1, arq)

arq = open('arquivo.pkl', 'rb')
retornou = pickle.load(arq)

print(retornou.nome)