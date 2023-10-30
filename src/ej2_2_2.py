def vuelvedad(edad):
    cuenta=0
    edad+=1
    out=str("Tu edad ")
    while edad != 1 :
        cuenta +=1
        out+=str(f"{cuenta}/")
        edad -=1
    return out

