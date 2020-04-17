print("Digite 3 notas: ")
notas = []
for x in range(0,3):    
    notas.append(input())
    notas[x] =  int(notas[x])

media = sum(notas) / len(notas)
print(media)