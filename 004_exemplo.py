#Crie um calculado onde o usuario insira dois valores
#Avançado

# Função para soma
def soma(a, b):
    return a + b

# Função para subtração
def subtracao(a, b):
    return a - b

# Função para multiplicação
def multiplicacao(a, b):
    return a * b

# Função para divisão
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero!"

# Função principal da calculadora
def calculadora():
    while True:
        # Exibe o menu de opções
        print("\nSelecione a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("0. Sair")

        # Solicita ao usuário que escolha uma opção
        escolha = input("\nDigite sua escolha (1/2/3/4/0): ")

        # Verifica a escolha do usuário
        if escolha == '0':
            print("Encerrando a calculadora.")
            break
        elif escolha in ('1', '2', '3', '4'):
            # Solicita os números para operar
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            # Realiza a operação baseado na escolha
            if escolha == '1':
                print(f"\n{num1} + {num2} = {soma(num1, num2)}")
            elif escolha == '2':
                print(f"\n{num1} - {num2} = {subtracao(num1, num2)}")
            elif escolha == '3':
                print(f"\n{num1} * {num2} = {multiplicacao(num1, num2)}")
            elif escolha == '4':
                print(f"\n{num1} / {num2} = {divisao(num1, num2)}")
        else:
            print("Escolha inválida. Por favor, tente novamente.")

# Executa a calculadora
calculadora()
