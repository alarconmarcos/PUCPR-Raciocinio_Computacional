#Pontifícia Universidade Católica do Paraná - PUCPR
#Curso de Análise e Desenvolvimento de Sistemas
#Matéria de Raciocínio Computacional
#Professor: Galbas Milleo Filho

#Atividade Prática (ATP): Loja em Python

from datetime import datetime

def obter_limite():

    nomeCompleto = "Fulaninho"
    print("Bem vindo à loja de", nomeCompleto)
    print ("Vamos analisar o seu crédito. Digite as informações solicitadas")
    cargo = str(input("Seu cargo na empresa: "))
    salario = float(input("Salário atual: "))
    anoNascimento = int(input("Ano de nascimento: "))
    print('As informações fornecidas foram: \nCargo: {} \nSalário: {:.2f} \nAno de Nascimento: {}'. format (cargo, salario,anoNascimento))

    diaAtual = datetime.now()
    idadeAproximada = diaAtual.year - anoNascimento
    limiteGasto = salario*(idadeAproximada/1000)+100
    print("Sua idade aproximada é de: ", idadeAproximada)
    print("Você pode gastar R$", limiteGasto)
    return limiteGasto, idadeAproximada, nomeCompleto
limiteGasto, idadeAproximada, nomeCompleto = obter_limite()


def verificar_produto(limiteGasto, idadeAproximada, nomeCompleto):
    produto = input("Nome do produto a ser cadastrado: ")
    precoProduto = float(input("Preço do produto: "))
    if precoProduto <= (limiteGasto * 0.6):
        print("Liberado")
    elif precoProduto > (limiteGasto * 0.6) and precoProduto <= (limiteGasto * 0.9):
        print("Liberado ao parcelar em até 2 vezes")
    elif precoProduto > (limiteGasto * 0.9) and precoProduto <= (limiteGasto * 1.0):
        print("Liberado ao parcelar em 3 ou mais vezes")
    else:
        print("Bloqueado")

    tamanhoNomeCompleto = len(nomeCompleto)
    primeiroNome = (nomeCompleto.split()[0]) 
    tamanhoPrimeiroNome = len(primeiroNome)
    if tamanhoNomeCompleto >= precoProduto >= idadeAproximada or tamanhoNomeCompleto <= precoProduto <= idadeAproximada:
        print("Seu primeiro nome é: ", primeiroNome)
        print("Seu primeiro nome tem ", tamanhoPrimeiroNome, " caracteres")
        print("Seu nome completo tem ", tamanhoNomeCompleto, " caracteres")
        print("Foi concedido desconto de {:.0f}%".format(tamanhoPrimeiroNome))
        percentualDesconto = tamanhoPrimeiroNome / 100
        desconto = (precoProduto - (precoProduto * percentualDesconto))
        print("O valor do produto com desconto será de R$", desconto)
    else:
        desconto = precoProduto
        print("O produto não tem desconto e será de", desconto)
    return desconto

saldo = limiteGasto
cadastroProdutos = int(input("Quantos produtos deseja cadastrar? "))

while not cadastroProdutos == 0:
    limite = []
    limite = verificar_produto(limiteGasto, idadeAproximada, nomeCompleto)
    cadastroProdutos -= 1
    saldo -= limite
    print("Seu saldo para gastar é de: ", saldo)
                         



    

