def desumidificacao():
    print("Início desumidificação")
    umidade=float(input(LEITURASENSOR(UMIDADE))
    temp_int=float(input(LEITURASENSOR(TEMP_INT))
    if temp_int > 15 and umidade > 40:
            EXAUSTOR(ON)
    elif temp_int <15 and umidade > 40:
            AQUECIMENTO(100)
            EXAUSTOR(ON)

    if umidade < 5:
        EXAUSTOR(OFF)
        AQUECIMENTO(OFF)
        print("Desumidificação concluída")

def coccao();
    print("Iníciando cocção")
    umidade=float(input(LEITURASENSOR(UMIDADE))
    if umidade > 15:
        EXAUSTOR(ON)
        

    temp_int=float(input(LEITURASENSOR(TEMP_INT))
    if temp_int < 200:
            AQUECIMENTO(380)

    if umidade <= 5:
            EXAUSTOR(OFF)

    if umidade < 5 and temp_int = 380:
        print("Inserir conteúdo para cocção - quanto concluir prissionar botão pronto")

    if BOTAO(ON):
        AQUECIMENTO(380
        TIMER(180)

    print("Cocção concluída")
    AQUECIMENTO(OFF)


        
umidade=float(input(LEITURASENSOR(UMIDADE))
temp_ext=float(input(LEITURASENSOR(TEMP_EXT))
    
if tem_ext <= 20:
    desumidificacao()
    coccao()
else:
    coccao()
    
    
    
        
    
