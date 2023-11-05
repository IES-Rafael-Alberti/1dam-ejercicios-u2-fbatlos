def calcular_capital_a_obtener(amount , interes , años):
    cont=0
    tot=0
    for i in range (años):
        tot+=amount*(1+(interes/100))
        tot=round(tot , 2)
        cont=1+i
        print (f"Tras el {cont}º año obtendras {tot}€")



def main():
    amount = int(input("Cantidad a invertir : "))
    interes = int(input("Interes porcentual anual : "))
    años = int(input("Cuantos años vas a invertir : "))
    print(calcular_capital_a_obtener(amount , interes , años ))


if __name__ == "__main__":
    main()