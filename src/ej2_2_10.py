def primo( num ):
    if num%2 == 0:
        print("Es primo")
    else:
        print("No es primo")

def main():
    num = int(input("Escribe numero : "))
    primo(num)

if __name__ == "__main__":
    main()