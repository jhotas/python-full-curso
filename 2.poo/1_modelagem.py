class Pessoas:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def logar_sistema(self):
        print(f'{self.nome} está logando no sistema')

p1 = Pessoas('Jean Oliveira', 21, '4218932143')
p2 = Pessoas('Johan Oliveira', 12, '82918392143')

p1.logar_sistema()
p2.logar_sistema()