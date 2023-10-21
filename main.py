"""
Esse é o motivo de DataClasses em Python serem incríveis
"""
class Pessoa:
    def __init__(self, nome, skill, idade, level):
        self.nome = nome
        self.skill = skill
        self.idade = idade

    def __str__(self) -> str:
        return f"Essa é minha classe Pessoa: {self.nome},{self.skill},{self.idade}"
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, self.__class__):
            return (self.nome == __value.nome) and (self.skill == __value.skill) and (self.idade == __value.idade)
        return False

p1 = Pessoa(nome="Luciano", skill="Engenharia", idade=35, level=50)
p2 = Pessoa(nome="Riviane", skill="Machine Learning", idade=22, level=60)
p3 = Pessoa(nome="Teo", skill="Machine Learning", idade=30, level=99)
p4 = Pessoa(nome="Teo", skill="Machine Learning", idade=30, level=98)

print(p3)
print(p4)
print(p1 == p3) # False
print(p3 == p4) # True