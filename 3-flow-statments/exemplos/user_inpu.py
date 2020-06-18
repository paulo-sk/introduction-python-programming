numbers = []
while True:
    n = input("Digite um numero: ")
    if n == 'done':
        print(f"Soma do numeros: {sum(numbers)}")
        print(f"Total de numeros: {len(numbers)}")
        print(f"Media dos numeros: {sum(numbers)/len(numbers)}")
        break
    else:
        try:
            numbers.append(float(n))
        except:
            print("Entrada invalida")
            continue
