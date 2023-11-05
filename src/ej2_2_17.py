def inversa( num ):
    suma=0
    for digito in str(num):
        suma += int(digito) 
    print(f"La suma de todo = {suma}")

def main():
    num = int(input("Escribe un numero : "))
    inversa(num )

if __name__ == "__main__":
    main()