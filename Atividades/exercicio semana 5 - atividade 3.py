#Desafio
import math

dados=[[20,19.5],[20,19.7],[20,20.2],[20,20.1],[21,19.9],[21,20.7],[21,21.2],[21,21.5],[25,25.5],[25,24.7],[25,25.2],[25,24.1]]

somasp=0
somapv=0
i=1
for coluna in dados:
    for linha in coluna:
      if i == 1:
          somasp=somasp+float(linha)
          i+=i
      else:
          somapv=somapv+float(linha)
          i=1
          
mediasp=somasp/12
mediapv=somapv/12

somadesviopadraopv=0
somadesviopadraosp=0

for coluna in dados:
    for linha in coluna:
      if i == 1:
          desviopadraosp=(float(linha)-mediasp)
          desviopadraosp=desviopadraosp*desviopadraosp
          somadesviopadraosp=somadesviopadraosp+desviopadraosp
          i+=i
      else:
          desviopadraopv=(float(linha)-mediapv)
          desviopadraopv=desviopadraopv*desviopadraopv
          somadesviopadraopv=somadesviopadraopv+desviopadraopv
          i=1

totaldesviopadraosp=math.sqrt(somadesviopadraosp/12)
totaldesviopadraopv=math.sqrt(somadesviopadraopv/12)

print("A média SP é:",mediasp)
print("A média PV é:",mediapv)
print()
print("O desvio padrão SP é:",totaldesviopadraosp)
print("O desvio padrão PV é:",totaldesviopadraopv)

#dados=[[1,2,3],[4,5,6],[7,8,9]]

#for coluna in dados:
#    print(coluna)

#for linha in dados:
#    for coluna in linha:
#        print(coluna)

#for linha in dados:
#    for coluna in range(3):
#        print(coluna)

#for coluna in dados:
#    for linha in range(3):
#        print(linha)


#tabela=[]
#contador=0
#for linha in tabela:
#    linha=[]
#    for coluna in linha:
#        tabela.append(contador)
#        contador+=1
#tabela.append(linha)
#        contador=contador+
#print(tabela)

#for numerador in range(10):
#    print('Tabuada do número', numerador)
#    for multiplicador in range(10):
#        print(numerador*multiplicador)

#for numerador in range(10):
#    print('Tabuada do número', numerador)
#    for multiplicador in numerador:
#        print((numerador+1)*multiplicador)

#for numerador in range(10):
#    print('Tabuada do número', numerador)
#    for valor in numerador:
#        print(valor)

#for numerador in range(10):
#    print('Tabuada do número', numerador)

#    for (multiplicador+1) in numerador:
#        print(numerador*multiplicador)

#for numerador in range(10):
#    print('Tabuada do número', numerador+1)
#    for multiplicador in range(10):
#        print((numerador+1)*(multiplicador+1))
