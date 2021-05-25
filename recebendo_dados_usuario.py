"""
Recebendo dados do usuário
input() -> todo dado recebido via input é do tio string

Em python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- apsas simples -> 'Josielle'
- aspas duplas -> "Josielle"
- aspas simples triplas -> '''Josielle'''
"""
# aspas duplas triplas -> """Josielle """

# Entrada de dados
# print("Qual seu nome?")
# nome = input()
nome = input('Qual seu nome?')

#Processamento

#Sáida de dados
# Exemplo de print antigo 2.x
#print('Seja bem vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
#print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}')

# print("Qual sua idade?")
# idade = input()
idade = int(input('Qual sua idade?'))  #pode ser utilizado o cast direto na variável

# Exemplo de print antigo 2.x
#print('A %s tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print('A {0} tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'A {nome} tem {idade} anos e nasceu em {2021 - idade}')

# print(f'A {nome} nasceu em {2021 - int(idade)}')  # int(idade) => cast (cast é a conversão de um tipo de dado para outro)


