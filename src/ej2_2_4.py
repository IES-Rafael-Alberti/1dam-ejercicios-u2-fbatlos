def cuenta_atras(numero):
    cont=numero
    out=str()
    while numero != -1 :
        if numero != -1 :
            out+=f"{cont} ,"
        cont-=1
        numero-=1
    return out    
