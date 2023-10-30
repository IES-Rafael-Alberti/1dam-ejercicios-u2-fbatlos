def grupos(nombre , sexo):
    nombre = nombre.upper()
    sexo = sexo.upper()
    if (sexo == "F" and nombre < "M") or (sexo == "M" and nombre > "N"):
        return "Grupo A"
    else:
        return "Grupo B"
  
def main():
    nombre = (input("Dame tu nombre : "))
    sexo = (input("Dame tu sexo (F Femenino y M Masculino) : "))
    print(grupos(nombre , sexo))


if __name__ == "__main__":
    main()