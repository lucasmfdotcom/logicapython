
# Laço de repetição com for usando range() com um passo de incremento
for i in range(0, 21, 2):  # Começa em 0, vai até 20, incrementando de 2 em 2
    print(i)

#---------------------------------
# Laço de repetição com for para iterar sobre uma lista e incrementar um contador
contador = 0
lista = [15, 20, 30, 40, 50, 60]
for elemento in lista:
    contador += 1  # Incrementa o contador
    print(f"Elemento {contador}: {elemento}")
