from model import Pessoa

class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoas.txt', 'w') as arq:
            arq.write(pessoa.nome + " " + str(pessoa.idade) + " " + pessoa.cpf)

    @classmethod
    def ler(cls):
        nome = 'Jean'
        idade = 21
        cpf = 3219389232
        return Pessoa(nome, idade, cpf)
    
p1 = Pessoa('Jean', 20, '321788721')
print(PessoaDal.ler().cpf)