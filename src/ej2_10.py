def pizza(vegano , ingrediente ):
    vegano = vegano.lower()
    if vegano == "si" or vegano == "sí" :
  
        if ingrediente == "1":
            return "La pizza es vegetariana y lleva tomate , mozzarella y pimiento"
  
        else:
            return "La pizza es vegetariana y lleva tomate , mozzarella y tofu"
  
    else:
  
        if ingrediente == "1" :
            return "La pizza es no vegetariana y lleva tomate , mozzarella y peperoni"
  
        elif ingrediente == "2" :
            return "La pizza es no vegetariana y lleva tomate , mozzarella y jamón"
  
        else:
            return "La pizza es no vegetariana y lleva tomate , mozzarella y salmón"

def main():
    vegano = (input("Dame el dividendo : "))
    ingrediente = (input("Dame el divisor : "))
    print(pizza())


if __name__ == "__main__":
    main()