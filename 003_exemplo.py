#Crie um calculado onde o usuario insira dois valores
#Basico

print("Insira 2 valores para realizar o cálculo!")

x = int(input("Primeiro valor: "))
y = int(input("Segundo valor: "))
z = input("Sinal matemático \n1=Soma \n2=Subtração \n3=Multiplicação: ")

#Avaliando operação

if z == '1':
    print(x + y)
elif z == '2':
    print(x - y)
elif z == '3':
    print(x * y)