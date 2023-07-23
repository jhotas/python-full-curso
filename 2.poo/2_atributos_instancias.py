class Pessoas:
    def __init__ (self, nome, idade):
        self.nome = nome # Atributos de instância
        self.idade = idade #

    def retorna_nome(self):
        return self.nome

    def logar_sistema(self):
        print(f'{self.retorna_nome} está logando no sistema!')
        
p1 = Pessoas('Jean Oliveira', 21)
p1.logar_sistema()