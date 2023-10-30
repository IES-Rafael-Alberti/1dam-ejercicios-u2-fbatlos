def grupos(nombre , sexo):
    nombre = nombre.upper()
    if (sexo == "F" and nombre < "M") or (sexo == "M" and nombre > "N"):
        return "Grupo A"
    else:
        return "Grupo B"
  
def main():
    edad = (input("Dame el dividendo : "))
    ingresos = (input("Dame tu sexo (F Femenino y M Masculino) : "))
    print(grupos())


if __name__ == "__main__":
    main()