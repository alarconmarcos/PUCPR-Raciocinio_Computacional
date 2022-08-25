#importa o metodo strftime
from datetime import datetime

#Le a data e a hora atual
hoje = datetime.now()

#extrai o ano da data e hora armazenada na variável hoje
ano_atual = int(hoje.strftime("%Y"))

meu_nome = "Marcos Alarcon"
print("Bem vindo à loja do " + meu_nome)

print("Farei agora uma análise de crédito para você.")
print()
print("Para isso precisarei de algumas informações:")
print()
cargo = input("Qual é o seu cargo na empresa em que trabalha?: ")
salario = float(input("Qual é o valor do seu salário?: "))
ano_nascimento = int(input("Qual é o ano em que você nasceu?: "))
print()
print("Obrigado pelas informações, conferindo então:")
print()
print("Você trabalha como",cargo+", recebe um salário mensal no valor de R$ {:.2f}".format(salario)+", e nasceu no ano de ",ano_nascimento)
print()
idade = (ano_atual - ano_nascimento)
print("Sua idade aproximada é:",idade, "anos")
print()
print("Você poderá gastar na loja a quantia de: R$ {:.2f}".format((salario * (idade / 1000)) + 100))
