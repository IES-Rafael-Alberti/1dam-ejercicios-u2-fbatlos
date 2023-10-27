def renta(renta_anual):
    if renta_anual < 10000 :
        return "Tipo impositivo del 5%"
    elif renta_anual >= 10000 and renta_anual < 20000 :
        return "Tipo impositivo del 15%"
    elif renta_anual >= 20000 and renta_anual < 35000 :
        return "Tipo impositivo del 20%"
    elif renta_anual >= 35000 and renta_anual < 60000 :
        return "Tipo impositivo del 30%"
    elif renta_anual >= 60000 :
        return "Tipo impositivo del 45%"
