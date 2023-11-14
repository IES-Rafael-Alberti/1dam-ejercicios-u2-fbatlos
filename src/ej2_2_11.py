def inversa( palabra ):
    for letra in reversed(palabra):
        print(letra , end=(" "))

def main():
    palabra = (input("Escribe una palabra : "))
    inversa(palabra)

if __name__ == "__main__":
    main()