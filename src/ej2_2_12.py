def inversa( frase , vocal ):
    veces_que_aparece = frase.count(vocal)
    print(f"La vocal {vocal} se repite {veces_que_aparece}")
    
def main():
    frase = (input("Escribe una frase : "))
    vocal = input("Dime la vocal que quieres que cuente : ")
    inversa(frase , vocal )

if __name__ == "__main__":
    main()