def pizza(vegano , ingrediente ):
    vegano = vegano.lower()
    ingrediente = ingrediente.lower()
    if vegano == "si" or vegano == "sí" :
  
        if ingrediente == "1":
            return "La pizza es vegetariana y lleva tomate , mozzarella y pimiento"
  
        elif ingrediente == "2":
            return "La pizza es vegetariana y lleva tomate , mozzarella y tofu"
        else:
            return "ERROR"
    else:
  
        if ingrediente == "1"  :
            return "La pizza es no vegetariana y lleva tomate , mozzarella y peperoni"
  
        elif ingrediente == "2" :
            return "La pizza es no vegetariana y lleva tomate , mozzarella y jamón"
  
        elif ingrediente == "3":
            return "La pizza es no vegetariana y lleva tomate , mozzarella y salmón"
        else:
            return "ERROR"

def main():
    vegano = (input("Eres vegetariano? : "))
    print("""Ingredientes vegetarianos: (1))Pimiento y (2)tofu.
Ingredientes no vegetarianos: (1)Peperoni, (2)Jamón y (3)Salmón.""")
    ingrediente = (input("Dame el numero del ingrediente : "))
    print(pizza(vegano , ingrediente))


if __name__ == "__main__":
    main()