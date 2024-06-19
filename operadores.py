#Operador	Equivalente a
#  =	x = 1
# +=	x = x + 1
#  -=	x = x - 1
#  *=	x = x * 1
#  /=	x = x / 1
# %=	x = x % 1
# Exemplo da utilização de cada operador de atribuição mencionado acima:

#notar que sempre na primeira linha é atribuido um valor a variavel numero
#na sequencia é utilizado um operador de atribuição realizando uma operacao
#

# Operador +=

numero = 5     #Declara a variavel numero como equivalente a 5
numero += 7   #Atribui a soma do valor 7 + variavel
print(numero)  # Resultado será 12


# Operador -=

numero = 5
numero -= 3
print(numero)  # Resultado será 2, pois 5 - 3 = 2


#Operador *=

numero = 5
numero *= 2
print(numero)  # Resultado será 10


# Operador /=

numero = 5
numero /= 4
print(numero)  # Resultado será 1.25


# Operador %=:

numero = 5
numero %= 2
print(numero)  # Resultado será 1
# Obs: O operador % é chamado módulo e nada mais é que o resto da divisão. No exemplo acima: 5 dividido por 2 dá 2 de resultado e sobra 1. Por isso numero %= 2 será 1!