numero = int(input("Digite um numerp para saber o fatorial: "))

fatorial = 1

if numero < 0:
    print("nao existe fatorial de numero negativo")
elif numero == 0:
    print(f"{numero}! = {0}")
else:
    for x in range(1,numero+1):
        fatorial = fatorial * x
    print(f"{numero}! = {fatorial}")