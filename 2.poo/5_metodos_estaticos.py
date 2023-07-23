class Pessoas:
    possui_olho = True # Atributos de classe
    possui_boca = True #
    raca = 'Ser humano' #

    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

    def retorna_nome(self):
        return self.nome

    def logar_sistema(self):
        print(f'{self.retorna_nome} está logando no sistema!')

    @classmethod
    def andar(cls):
        cls.pernas = 2
        return None
    
    def é_adulto(idade): # Métodos estáticos
        if idade > 18: #
            return True #
        return False #
      
#p1 = Pessoas('Jean Oliveira', 21)
#p2 = Pessoas('Johan Oliveira', 12)

print(Pessoas.é_adulto(21))