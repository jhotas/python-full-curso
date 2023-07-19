class Pessoas:
    possui_olho = True
    possui_boca = True
    raca = 'Ser humano'

    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

    def retorna_nome(self):
        return self.nome

    def logar_sistema(self):
        print(f'{self.retorna_nome} está logando no sistema!')
        
p1 = Pessoas('Jean Oliveira', 21)
p2 = Pessoas('Johan Oliveira', 12)

Pessoas.possui_boca = False

print(p1.possui_boca)
print(p2.possui_boca)