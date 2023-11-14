def inversa( num ):
    cont=0
    while num != 0 :
        cont += num
        num = int(input())
    print(f"La suma de todo es igual a {cont}")

def main():
    num = int(input("Escribe un numero : "))
    inversa(num )

if __name__ == "__main__":
    main()