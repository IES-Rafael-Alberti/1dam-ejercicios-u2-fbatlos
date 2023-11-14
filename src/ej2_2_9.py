def tabla(contraseña ):
    contraseña_guardada = "panconpan123"
    while contraseña != contraseña_guardada :
        print("Contraseña incorrecta")
        contraseña = input("Intentelo de nuevo : ")
    print("GOD")
    
def main():
    contraseña = (input("Escribe la contraseña : "))
    tabla(contraseña)

if __name__ == "__main__":
    main()