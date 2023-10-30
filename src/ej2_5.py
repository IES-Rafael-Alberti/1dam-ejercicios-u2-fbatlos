def tributar(edad , ingresos):
    if edad>16 and ingresos>=1000 :
        return "Tributas crack"
    else:
        return "No tributas crack"

def main():
    edad = int(input("Dame tu edad : "))
    ingresos = int(input("Dame tus ingresos : "))
    print(tributar())


if __name__ == "__main__":
    main()
    