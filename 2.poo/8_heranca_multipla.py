class Animal: #
    def andar(self):
        print('Estou andando')

    def correr(self):
        print('Estou correndo')

    def pular(self):
        print('Estou pulando')

class Felino(Animal): # 
    def felino(self):
        print('Eu sou um felino')

class Gato(Felino): #
    def miar(self):
        print('Estou miando')

class Cachorro(Animal):
    def latir(self):
        print('Estou latindo')

gato = Gato()
gato.felino()