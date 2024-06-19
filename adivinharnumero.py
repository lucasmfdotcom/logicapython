
# Número secreto
numero_secreto = 42

# Variável para armazenar a tentativa do usuário
tentativa = None

# Loop para repetir a tentativa
while tentativa != numero_secreto:
    # Entrada: tentativa do usuário
    tentativa = int(input("Insira um número entre 1 e 100: "))

    # Verificação se a tentativa é correta
    if tentativa < numero_secreto:
        print("Tente um número maior!")
    elif tentativa > numero_secreto:
        print("Tente um número menor!")
    else:
        print("Parabéns, você acertou!")
        break