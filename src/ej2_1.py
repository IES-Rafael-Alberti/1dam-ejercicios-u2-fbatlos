
def compara(edad):
    if (edad>=18):
        return "Eres mayor de edad"
    else:
        return "Eres menor de edad"


def main():
    edad = int(input("Edad: "))
    print(compara())


if __name__ == "__main__":
    main()