def inversa( frase ):
    while frase != "salir" :
        print(frase*2 , end=(" "))
        frase = frase.lower()
        frase = input()
        
def main():
    frase = (input("Escribe una frase : "))
    inversa(frase )

if __name__ == "__main__":
    main()