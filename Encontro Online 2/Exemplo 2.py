# Uma indústria de cilindros de oxigênio deseja facilitar o armazenamento de seu estoque para seus
# colaboradores. A ideia é desenvolver um programa que receba as medidas de um cilindro (em cm),
# calcule e apresente o volume do mesmo (cm3). A partir do volume, o programa deve mostrar ao
# usuário onde deve ser armazenado o cilindro, segundo a lista a seguir:

# - Até 10cm3 (incluindo 10cm3) -> Galpão 1
# - Entre 10cm3 e 15cm3 -> Galpão 2
# - Maior ou igual a 15cm3 -> Galpão 3

# V = pi x R2 x h

# Sendo V o volume, R o raio e h a altura.

# importar biblioteca de matematica
import math

r = float(input("Informe o raio do cilindro (cm): "))
h = float(input("Informe a altura (cm): "))

volume = math.pi * (r ** 2) * h

print("Volume: {:.2f}cm3".format(volume))

if volume <= 10:
    print("Mova o cilindro para o GALPÃO 1!")

elif volume > 10 and volume < 15:
    print("Mova o cilindro para o GALPÃO 2!")

else:
    print("Mova o cilindro para o GALPÃO 3!")
