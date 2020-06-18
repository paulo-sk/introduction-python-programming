print("\nDuas piramide: ")
base_range = int(input("Tamanho da base, (numero impar): "))
count = 0
for base in range(base_range,0,-2):
    # adiciona o tanto de espace a medida que o triangulo diminui
    for space in range(count):
            print(" ",end='')
  
    for i in range(1,base+1):
        print("*",end='')

    print()
    count +=1

# numero de espacos baseado na metade da base da piramide, serve tanto para n° par ou impar
space = (base_range - 1) // 2

# o topo da piramide muda de acordo com a paridade da base

if base_range % 2 != 0:
    # se par, começa do zero:
    for base in range(1,base_range+1,2):

        for spaces in range(space):
            print(" ",end='')
        
        for x in range(2,base):
            print("*",end='')
        
        print()
        space += -1
else:
    
    for base in range(1,base_range+1,2):

        for spaces in range(space):
            print(" ",end='')
            
    
        for x in range(base+1):
            print("*",end='')
        
        print()
        space += -1
        
