
from abc import ABC,abstractmethod
from webbrowser import Opera


class Operacao(ABC):
        
    @abstractmethod
    def calcular(self,x,y):
        pass

class Soma(Operacao):
        
    def calcular(self, x, y):
        return x + y

class Subtracao(Operacao):        

    def calcular(self, x, y):
        return x - y

class Multiplicacao(Operacao):        

    def calcular(self, x, y):
        return x * y

class Divisao(Operacao):
       
    def calcular(self, x, y):
        return x / y
        

# Programa Principal

soma = Soma()
sub = Subtracao()
div = Divisao()
mult = Multiplicacao()

print(soma.calcular(10, 5))      # 15
print(sub.calcular(10, 5))       # 5
print(div.calcular(10, 5))       # 2.0
print(mult.calcular(10, 5))      # 50
   
  
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Gato(Animal):

    def emitir_som(self):
        print('Miado')

class Cachorro(Animal):

    def emitir_som(self):
        print('Latido')

class Cavalo(Animal):

    def emitir_som(self):
        print('Relinchado')


class Veterinario:

    def examinar(self, animal):
        animal.emitir_som()




dog = Cachorro("Rex", 3)
horse = Cavalo("Horse", 6)
cat = Gato("Tina", 1)

dog.emitir_som()          # exibe o som do cachorro
horse.emitir_som()        # exibe o som do cavalo
cat.emitir_som()          # exibe o som do gato

vet = Veterinario()
vet.examinar(dog)         # exibe o som do cachorro 
vet.examinar(horse)       # exibe o som do cavalo 
vet.examinar(cat)         # exibe o som do gato

