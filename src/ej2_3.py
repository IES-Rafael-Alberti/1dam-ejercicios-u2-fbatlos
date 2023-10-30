def disvision(dividendo,divisor):
    if divisor==0:
        return "ERROR"
    else:
        return dividendo/divisor
    
def main():
    dividendo = int(input("Dame el dividendo : "))
    divisor = int(input("Dame el divisor : "))
    print(disvision())


if __name__ == "__main__":
    main()

