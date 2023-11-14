def tabla(num):
    
    for i in range(1, num + 1, 2):
     for j in range(i, 0, -2):
        print(j, end=" ")

def main():
    num = int(input("Dame un numero para la piramide invertida : "))
    tabla(num)

if __name__ == "__main__":
    main()