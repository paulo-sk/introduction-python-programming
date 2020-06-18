numero = int(input("Calcule o fatorial: "))

if numero < 0:
    print("Nao existe fatorial de numero negativo.")
elif numero == 0:
    print(f"{numero}! = 1.")
else:
    fatorial = numero
    count = numero -1
    while count > 1:
        fatorial *=  count
        count -= 1
    print(f"{numero}! = {fatorial}.")
