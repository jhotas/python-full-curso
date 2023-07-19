class Pessoas:
    def __init__ (self, nome, idade, cpf):
        print(f'{nome} | {idade} | {cpf}')

    def logar_sistema(self):
        print('Estou logando no sistema')
        
p1 = Pessoas('Jean Oliveira', 21, '32891387921')
p2 = Pessoas('Tayana Wilbert', 40, '98321983245')