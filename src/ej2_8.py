def puntuacion(puntos):
    if puntos == 0.0 :
        return "Tu nivel de rendimiento es inaceptable y tu dinero es 0.0 "
    elif puntos == 0.4 :
        return "Tu nivel de rendimiento es aceptable y tu dinero es 960.0 "
    elif puntos >= 0.6 :
        return f"Tu nivel de rendimiento es meritorio y tu dinero es {puntos*2400} "
    else:
        return "ERROR"

def main():
    puntos = float(input("Dime los puntos obtenidos : "))
    print(puntuacion())


if __name__ == "__main__":
    main()