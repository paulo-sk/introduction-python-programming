x = input("Enter a number x: ")
y = input("Enter a number y: ")

try:
    result = float(x) / float(y)
except ZeroDivisionError:
    print("Can't dive by zero!")
else:
    print(result)
finally:
    print("Finally, aways is executed")