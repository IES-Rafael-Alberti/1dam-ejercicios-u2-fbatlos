def par_o_impar(numero):
    if numero%2 == 1 :
        return "Tu numero es impar"
    else:
        return "Tu numero es par"

def main():
    numero = int(input("Dime un número : "))
    print(par_o_impar(numero))


if __name__ == "__main__":
    main()
