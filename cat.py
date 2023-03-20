def main():
    number = get_number()
    miau(number)

def get_number():
    while True:
        n = int(input("Ingrese nro rep:"))
        if n > 0:
            break
    return n

def miau(n):
    print("miauuuu!! "*n)



main()

i = 0
while i < 3:
    print("meow")
    i += 1

for i in range(3):
    print("guau")

n = int(input("Nro de miaus?"))
print("meow\n" * n)  

while True:
    n = int(input("Numero repeticiones:"))
    if n > 0:
        break

for _ in range(n):
    print("Miauuuu")

