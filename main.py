from dataclasses import dataclass

"""
Esse é o motivo de DataClasses em Python serem incríveis
"""

@dataclass
class Pessoa:
    nome: str
    skill: str
    idade: int
    level:int

p1 = Pessoa(nome="Luciano", skill="Engenheiro de dados", idade=35, level=30)
p2 = Pessoa(nome="Riviane", skill="Machine Learning", idade=22, level = 40)
p3 = Pessoa(nome="Teo", skill="Machine Learning", idade=28, level = 99)
p4 = Pessoa(nome="Teo", skill="Machine Learning", idade=28, level = 99)

print(p1) # Pessoa(nome="Luciano", skill="Engenheiro de dados", idade=35)
print(p2) # Pessoa(nome="Riviane", skill="Machine Learning", idade=22)
print(p2 == p3) # False
print(p3 == p4) # True