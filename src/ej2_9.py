def entrada(edad):
    if  edad<4 :
        return "Pasas gratis"
    elif edad>=4 and edad<18 :
        return "La entrada son 5€"
    elif edad>=18 :
        return "La entrada son 10€"