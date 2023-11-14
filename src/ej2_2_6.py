def poner_asterisco(num):
    for i in range(num + 1):
        print("*" * i)

def main():
    num = int(input("Cuantos * vas a imprimir: "))
    poner_asterisco(num)

if __name__ == "__main__":
    main()