def cadastro():

    print("Bem-vindo ao seu Planejador de viajens\n")
    print("Vamos preencher seu cadastro? \n")

    nome = input("Qual seu nome? ")
    teto = float(input("Qual valor máximo que deseja gastar na viagem? "))
    qtde = int(input("Quantas paradas sua viagem terá? "))

    return qtde, teto

def verificaDestino(destinos, totaldias, contParadas):

    if destino in destinos:
        dias = int(input("Quantos dias prentende ficar em {}?".format(destino)))

        totaldias = totaldias + dias
        contParadas = contParadas + 1
    else:
        print("Cidade {} não consta na lista de destinos permitidos!".format(destino))

    return totaldias, contParadas

def calculaGastoDiario(teto, totaldias):

    print("\nVocê poderá gastar em média R$ {0:.2f} por dia".format(teto/totaldias))




# Define a lista de destinos possiveis
destinos = ['Paris', 'Roma', 'Londres', 'Lisboa', 'Madrid']

# Chamada a função de cadastro
qtde, teto = cadastro()

print("\nAgora vamos incluir seus destinos? ")
totaldias = 0
contParadas = 0
while contParadas < qtde:

    print("\n=== Destino {} ===".format(contParadas + 1))
    destino = input("Informe a cidade de destino: ")

    # Chamada a função de verificação de destino
    totaldias, contParadas = verificaDestino(destinos, totaldias, contParadas)

# Chamada a função de calculo de gasto
calculaGastoDiario(teto, totaldias)

