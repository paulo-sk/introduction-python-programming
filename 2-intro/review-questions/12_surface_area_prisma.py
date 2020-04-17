# Surface area of a prisma = 2ab + 2bc + 2ac

a,b,c = [int(x) for x in input("Enter the 3 sides of a prisma: ").split(' ')]
area = 2*a*b + 2*c*b + 2*a*c
print(f"The area of the prisma is = {area}")