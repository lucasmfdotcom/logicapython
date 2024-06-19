#Criação de listas simples em python:

alunos = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
print(type(teste)) # a funcao type() em python mostra o tipo da variavel alunos ‘list’
print(len(alunos)) # a função len() apresenta o comprimento do parametro passado '5'
print(alunos[4]) # Luana - Notar que a lista inicia sempre com indice do 0

#--------------------------------------

#Listas em python aceita valores diferentes com tipos diferentes

aluno = ['Murilo', 19, 1.79] # Nome, idade e altura

print(type(aluno)) # type 'list'
print(aluno) # ['Murilo', 19, 1.79]

#--------------------------------------

#Alterar fatores de uma lista:
programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
print(programadores) # imprime o conteudo da lista "programadores"

programadores[1] = 'Carolina' #edita o item 1 da lista para 'Carolina'
print(programadores) # ['Victor', 'Carolina', 'Samuel', 'Caio', 'Luana']

#--------------------------------------

#Inserir um elemento ao fim da lista

programadores.append('Renato')
print(programadores) # ['Victor', 'Carolina', 'Samuel', 'Caio', 'Luana', 'Renato']

#Inserir elemento indicando dois parametros posicao + elemento:

programadores = ['Victor', 'Carolina', 'Samuel', 'Caio', 'Luana']
programadores.insert(1, 'Rafael')
print(programadores) # Resultado ['Victor', 'Rafael', 'Juliana', 'Samuel', 'Caio', 'Luana']

#--------------------------------------

#Remover item específico da lista pelo valor
programadores.remove('Victor')
print(programadores) # 

# Remover item especifico da lista pelo indice
programadores.pop(0)




