def opciones( num ):
    if num == 1 or num == 2 :
        print ("Ole macarrone")
    else :
        print("Escribe un numero/ 1- comenzar programa, 2- imprimir listado, 3-finalizar programa./ : ")

def main():
    num = int(input("Escribe un numero/ 1- comenzar programa, 2- imprimir listado, 3-finalizar programa./ : "))
    while num != 1 and num != 2 and num != 3 :
        print("ERROR - la elección no se encuentra -")
        num = int(input("Escribe un numero/ 1- comenzar programa, 2- imprimir listado, 3-finalizar programa./ : "))
    opciones(num )

if __name__ == "__main__":
    main()