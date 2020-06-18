# Write a Program to Display the Fibonacci Sequences up to nth Term Where n is Provided by the User
nterms = int(input("How many terms of fibonacci sequence? "))

current = 0
next_term = 0
previous = 1

# so o contador do loop
count = 0
if nterms == 1:
    print(f"Fabonacci sequence: {current}",end='')

else:
    while count < nterms:
        if count == nterms - 1:
            print(next_term,end='\n')

        else:    
            print(next_term,end='-')
            current = next_term
            next_term += previous
            previous = current

        count += 1


        