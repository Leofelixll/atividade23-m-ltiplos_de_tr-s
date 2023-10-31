# Exercício Python 23: Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

soma = 0
for num in range(0, 500, 3):
    if num % 3 == 0:
        soma += num
print('A soma todos os múltiplos de três em um intervalo de 1 até 500:', soma)
