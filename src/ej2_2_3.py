def impares(numero):
    cuenta=0
    numero+=1
    out=str(" ")
    while numero != 0 :
        cuenta +=1
        if cuenta%2 == 1:
            if numero != 1 :
                out+=str(f" {cuenta} ,")
        numero -=1
    return out
print(impares(46))