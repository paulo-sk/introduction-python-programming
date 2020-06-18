n = int(input("Enter how much: "))

print("Padrao 1:")
for x in range(1,n+1):
    for y in range(1,x+1):
        print(x,end='')
    print('')

print("\nPadrao 2:")
for x in range(n,0,-1):
    for y in range(1,x+1):
        print(y,end='')
    print('')

