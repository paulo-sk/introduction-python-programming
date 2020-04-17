print("-----------Codigo unicode e caracter------------------")
numero = input("Digite um numero para saber seu caracter correspondente: ")
char = input("Digite um caracter para saber seu numero correspondente: ")
string_of_number = chr(int(numero))
number_of_string = ord(char)
print(f"O caracter do numero {numero} = {string_of_number}")
print(f"O numero do caracter {char} = {number_of_string}")


print(f"----------------------The complex() function--------------------")
# simplesmente usado para descrever/reprensentar numeros complexos.
# complex(1) = 1 +0j
# complex(5,8) = 5 + 8j
# se colocar uma string, ja converte pra number caso seja possivel
complex_with_string = complex('1')
complex_with_number = complex(5,8)
print(complex_with_string)
print(complex_with_number)
_2201discout = input("letra")