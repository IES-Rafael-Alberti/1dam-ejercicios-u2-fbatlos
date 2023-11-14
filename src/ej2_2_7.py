def tabla_del_10(num):
    
    for i in range(num + 1):
        print(f"{i} * {num} => {num * i}")

def main():
    num = 10
    tabla_del_10(num)

if __name__ == "__main__":
    main()