def main():
    x = int(input("Ingrese X:"))
    if is_par(x):
        print("Par")
    else:
        print("impar")

def is_par(n):
    return True if n % 2 == 0 else False
    


main()

