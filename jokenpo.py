# Entrada: escolha do usuário
escolha = input("Insira sua escolha (pedra, papel ou tesoura): ").lower()

# Número aleatório para a escolha do computador
import random
computador = random.choice(["pedra", "papel", "tesoura"])

# Verificação da vitória
if escolha == computador:
    print("Empate!")
elif (escolha == "pedra" and computador == "tesoura") or (escolha == "papel" and computador == "pedra") or (escolha == "tesoura" and computador == "papel"):
    print("Você ganhou!")
else:
    print("Computador ganhou!")