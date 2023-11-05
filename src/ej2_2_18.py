def suma_digitos( num ):
    suma = 0
    cont_pares = 0
    cont_impares = 0
    cont_final = str("los numeros ")
    while num != -1 :
        for digito in str(num):
            suma += int(digito) 
        
        if suma % 2 == 0 :
            cont_pares +=1
        
        else:
            cont_impares +=1

        if cont_pares > cont_impares :
            cont_final = f"pares son : {cont_pares}"
        else:
            cont_final = f"impares son : {cont_impares}"
        print(f"La suma de todo es {suma}")
        num = int(input())
        suma=0
    print(f"los que mas se repiten son {cont_final}")


def main():
    num = int(input("Escribe un numero : "))
    suma_digitos(num )

if __name__ == "__main__":
    main()