"""
PEP8 - Python Enhancement Proposal

São propostas de molhorias para a linguagem Python

The Zen of Python

import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica.

[1] - utilize Camel Case para nomes de classes;
ex.:
class Calculadora: (inicial maiuscula)
    pass

[2] - Utilize nomes em minusculo, separados por underline para funções ou variaveis
ex.:
def soma():
    pass


obs.: duas linhas em branco [4]
def soma_dois():
    pass

[3] - Utilize quatro espaços para identação! NÃO PODE UTILIZAR TAB
ex.:
if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
ex.:
- Separar funções e definições de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco.

[5] - Imports
ex.:
- Imports devem ser sempre feitos em linhas separadas;
import sys
import os
from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

[6] - Espaços em expressões e instruções
ex.:
funcao( algo [ 1 ], { outro: 2 } ) - errado
funcao(algo[1], {outro: 2}) - certo

[7] - Termine sempre uma instrução com uma nova linha
ex.:
import this

print('Josi')

"""
