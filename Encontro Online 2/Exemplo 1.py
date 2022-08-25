# Desenvolva um programa que efetue a leitura do valor total de uma venda e apresnte ao final
# o valor a vista (10% de desconto), o valor das parcelas em caso de parcelamento em 3x (sem
# juros) e a comissão do vendedor (5% sobre o valor da venda).
# Caso a comissão do vendedor ultrapasse R$ 100,00, mostre uma mensagem dizendo que a comissão
# ultrapassou o teto de comissão da empresa.

# 1) Entrada de dados
valor_total = float(input("Informe o valor total: "))

# 2) Processamento

# Calcula valor a vista
#valor_a_vista = valor_total - (valor_total * 0.1)
valor_a_vista = valor_total * 0.90

# Calcula parcelas
valor_parcelado = valor_total / 3

# Calcula comissão
valor_comissao = valor_total * 0.05

# 3) Saida de dados
print("VALOR A VISTA: R$ {:.2f}".format(valor_a_vista))
print("3 PARCELAS DE: R$ {:.2f}".format(valor_parcelado))
print("COMISSÃO: R$ {:.2f}".format(valor_comissao))

if valor_comissao > 100:
    print("Sua comissão ultrapassou os valores permitidos")
