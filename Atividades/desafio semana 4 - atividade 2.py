temperatura = int(input("Qual a temperatura atual?"))

if temperatura < 7:
     print("Congelando")
elif temperatura <10:
     print("Frio")
elif temperatura > 26:
     print("Ótimo")
else:
     print("Fresco")
