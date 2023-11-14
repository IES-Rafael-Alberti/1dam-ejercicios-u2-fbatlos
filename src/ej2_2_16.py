def inversa( num ):
    cont=num
    while num != 0 :
        if num>cont:
            cont = num
            num = int(input())
        else:
            num = int(input())   
    print(f"De todos los numeros el mayor es : {cont}")

def main():
    num = int(input("Escribe un numero : "))
    inversa(num )

if __name__ == "__main__":
    main()