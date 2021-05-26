"""
Tipo Float

Tipo real, decimal
Casa decimais

OBS.: os separadores de casas decimais na progração é o ponto e não a vírgula
"""

#Errado do ponto de vista do float, mas gera uma tupla
valor = 1, 44
print(valor)

#Correto do ponto de vista Float
valor = 1.44
print(valor)
print(type(valor))

#é possível fazer duplo atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

#Podemos converter um Float para um int e vice versa
"""
OBS.: Ao converter Float para inteiros, nós perdemos precisão
"""
res = int(valor)
print(res)
print(type(res))

#Podemos trabalhar com números complexos
# exemplo: 1j, 5j
variavel = 5j