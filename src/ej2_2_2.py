def vuelvedad(edad):
    cuenta=0
    edad+=1
    out=str("Tu edad ")
    while edad != 1 :
        cuenta +=1
        out+=str(f"{cuenta}/")
        edad -=1
    return out
def main():
    edad = int(input("Edad : "))
    print(vuelvedad(edad))


if __name__ == "__main__":
    main()
