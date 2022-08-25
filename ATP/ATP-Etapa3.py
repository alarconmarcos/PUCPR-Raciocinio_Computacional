#Curso: Análise e Desenvolvimento de Sistemas
#Matéria: Raciocínio Computacional
#Professor-Tutor: Lucas Emanuel Silva E Oliveira
#Aluno: Marcos Alarcon


#importação da classe para uso do metodo strftime
from datetime import datetime

#Le a data e a hora atual
hoje = datetime.now()

#extrai o ano da data e hora armazenada na variável hoje
ano_atual = int(hoje.strftime("%Y"))

#Etapa 1
meu_nome_completo = "Marcos Alarcon"
print("Olá, Seja bem-vindo à loja Quase Tudo Utilidades, sou", meu_nome_completo, "e irei auxiliá-lo no que precisar.\n" )
print("É um prazer tê-lo em nossa loja, e para melhor lhe atender, faremos uma breve análise de crédito. \n")
print("Para isso precisarei de algumas informações:\n")

def efetua_cadastro():
    cargo = input("Qual é o seu cargo na empresa em que trabalha?: ")
    salario = float(input("Qual é o valor do seu salário?: "))
    ano_nascimento = int(input("Qual é o ano em que você nasceu?: "))
    print()
    print("Obrigado pelas informações, conferindo então:\n")
    print("Você trabalha como",cargo+", recebe um salário mensal no valor de R$ {:.2f}".format(salario)+", e nasceu no ano de ",ano_nascimento,"\n")
    
    idade = (ano_atual - ano_nascimento)
    print("Sua idade aproximada é:",idade, "anos \n")

    dados_corretos = str(input("Seus dados estão corretos? \n Digite [s] para sim e [n] para não: "))
    
    return dados_corretos, salario, ano_nascimento, idade
    
dados_corretos, salario, ano_nascimento, idade = efetua_cadastro()

while dados_corretos != 's':
    print("Ok vamos lá, insira novamente os seus dados!\n")
    efetua_cadastro()
    
    
def obter_limite():
    limite = (salario * (idade / 1000)) + 100
    print("Você poderá gastar na loja a quantia de: R$ {:.2f}".format(limite))
    
    return limite

limite = obter_limite()

def verifica_produto(limite):
    #Etapa 3
    produto = input("Informe o nome do produto que deseja adquirir: ")
    valor_produto = float(input("Informe o valor do produto que deseja adquirir: "))

    if valor_produto <= (limite * 0.60):
        print("Produto liberado!")
    elif (valor_produto > (limite * 0.60)) and (valor_produto <= (limite * 0.90)):
        print("Produto liberado liberado ao parcelar em até 2 vezes")
    elif (valor_produto > (limite * 0.90)) and (valor_produto <= limite):
        print("Produto liberado liberado ao parcelar em até 3 vezes")
    else:
        print("Produto bloqueado!")

    

qtd_letras_nome_completo = len(meu_nome_completo)

qtd_letras_nome = len(meu_nome_completo[:meu_nome_completo.index(" ")])

if valor_produto >= qtd_letras_nome and valor_produto <= idade:
    print("Parabéns, você recebeu um desconto de: R$ {:.2f}".format(qtd_letras_nome))
    print("Portanto, você pagará pelo produto:", produto,"o valor de R$ {:.2f}".format(valor_produto - qtd_letras_nome))    
