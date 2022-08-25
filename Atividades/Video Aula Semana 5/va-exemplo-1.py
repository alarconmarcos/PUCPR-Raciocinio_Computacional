# Escreva um algoritmo que receba cinco números do usuário e imprima a metade de cada número.
# Mostre a soma de todas metades ao final.

soma = 0

qtde = int(input("Quantos numeros deseja informar? "))

#for c in range(5):
for c in range(qtde):

    n = float(input("Informe um valor: "))

    metade = n / 2

    print(metade)

    soma = soma + metade

print("Soma: {}".format(soma))


