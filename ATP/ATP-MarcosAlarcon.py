#Curso: Análise e Desenvolvimento de Sistemas
#Matéria: Raciocínio Computacional
#Professor-Tutor: Lucas Emanuel Silva E Oliveira
#Aluno: Marcos Alarcon


#importação de classes
from datetime import datetime
from time import sleep
from sys import stdout

#função para validar os valores digitados
def valida_float_input(pergunta):
    s = None

    while True:
        try:
            s = float(input(pergunta))
            break
        except ValueError:
            print("Erro: O valor informado dever ser um valor numérico")
            print("Por favor, digite novamente!")

    return s

#função para simples animação de verificação de cadastro
def progresso():
    toolbar_width = 50

    for i in range(toolbar_width):
        sleep(0.1) 
        stdout.write("-")
        stdout.flush()
    stdout.write("[Concluído!]")

#função cadastro do cliente
def cadastra_cliente():
    #Le a data e a hora atual
    hoje = datetime.now()

    #extrai o ano da data e hora armazenada na variável hoje
    ano_atual = int(hoje.strftime("%Y"))

    cargo = input("Qual é o seu cargo na empresa em que trabalha?: ")
    salario = float(valida_float_input("Qual é o valor do seu salário?: "))
    ano_nascimento = int(valida_float_input("Qual é o ano em que você nasceu?: "))
    print()
    print("Obrigado pelas informações, para uma simples conferência:\n")
    print("Você trabalha como",cargo+", recebe um salário mensal no valor de R$ {:.2f}".format(salario)+", e nasceu no ano de",ano_nascimento,"\n")
    
    idade = (ano_atual - ano_nascimento)
    print("Sua idade aproximada é de",idade, "anos \n")

    dados_corretos = str(input("Seus dados estão corretos? \nDigite [s] para sim e [n] para não: "))

    return dados_corretos, salario, ano_nascimento, idade
    
#função que calcula o limite do cliente
def obter_limite():
    meu_nome_completo = "Marcos Alarcon"

    #mensagens de boas vindas
    print("------------------------------------------")
    print("| Bem-vindo à loja Quase Tudo Utilidades |")
    print("------------------------------------------\n")
    print("Olá, eu sou", meu_nome_completo, "e irei auxiliá-lo no que precisar.\n" )
    print("É um prazer tê-lo em nossa loja, e para melhor lhe atender, faremos uma breve análise de crédito. \n")
    print("Para isso precisarei de algumas informações:\n")

    #invoca a função de cadastro do cliente
    dados_corretos, salario, ano_nascimento, idade = cadastra_cliente()

    #laço de repetição para invocar a função cadastro novamente caso o cliente informe os dados incorretos
    while dados_corretos != "s":
        print("\nPor favor insira novamente os seus dados!\n")
        dados_corretos, salario, ano_nascimento, idade = cadastra_cliente()
    
    
    #Animação enquanto analisa o limite do cliente
    print("Efetuando análise de cadastro, por favor aguarde!\n")
    progresso()

    limite = round(salario * (idade / 1000)) + 100
    print("\nParabéns seu cadastro foi aprovado!\nVocê poderá gastar na loja a quantia de: R$ {:.2f}".format(limite))
    return limite, meu_nome_completo, idade


def verifica_produto(limite,n_prod,nome_completo,idade):
    produto = input("Informe o nome do {0}º produto que deseja cadastrar: ".format(n_prod))
    valor_produto = float(valida_float_input("Informe o valor do {0}º produto que deseja cadastrar: ".format(n_prod)))

    cadastra=True
    qtd_letras_nome_completo = len(nome_completo)
    qtd_letras_nome = len(nome_completo.split()[0])

    if valor_produto >= qtd_letras_nome_completo and valor_produto <= idade:
        print("Parabéns, você recebeu um desconto de: R$ {:.2f}".format(qtd_letras_nome))
        print("Portanto, você pagará somente R$ {:.2f}".format(valor_produto - qtd_letras_nome)," pelo produto:", produto)
        valor_produto = valor_produto - qtd_letras_nome

    if valor_produto <= (limite * 0.60):
        print("Produto liberado!")
    elif (valor_produto > (limite * 0.60)) and (valor_produto <= (limite * 0.90)):
        print("Produto liberado ao parcelar em até 2 vezes")
    elif (valor_produto > (limite * 0.90)) and (valor_produto <= limite):
        print("Produto liberado ao parcelar em 3 vezes ou mais vezes!")
    else:
        print("Produto bloqueado!\nSeu limite não é suficiente para cadastrar este produto")
        cadastra = False

    if cadastra:
        limite_restante = limite - valor_produto
    else:
        limite_restante = limite

    if limite_restante > 0:
        print("Restam ainda um saldo total de R$ {:.2f}".format(limite_restante), "para efetuar compras na loja!")
    else:
        print("Seu saldo esgotou, não é possível cadastrar mais produtos!")
        cadastra = False

    print("\n")

    return limite_restante, cadastra

def cadastra_produto(limite, nome_completo, idade):
    qtd_produtos = int(valida_float_input("Quantos produtos deseja cadastrar?: "))

    for i in range(qtd_produtos):
        limite, cadastra = verifica_produto(limite, i+1, nome_completo, idade)
        if not cadastra:
            break
        i += 1
    return limite


limite, nome_completo, idade = obter_limite()
limite = cadastra_produto(limite, nome_completo, idade)

while limite > 0:
    print("Você finalizou suas compras e ainda restou um saldo total de R$ {:.2f}".format(limite))
    if str(input("Deseja cadastrar mais algum produto? \nDigite [s] para sim e [n] para não: ")) == "s":
        limite = cadastra_produto(limite, nome_completo, idade)
    else:
        break
print('>>>>Agradecemos pela sua preferência<<<<\n\n<<<Volte sempre!>>>')



