num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

# Verificando se a operação é válida
if operacao not in ['+', '-', '*', '/']:
    print("Operação inválida.")
else:
    # Realizando a operação
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    else:  # Operação é '/'
        if num2 == 0:
            print("Divisão por zero não é permitida.")
        else:
            resultado = num1 / num2

    # Imprimindo o resultado
    print("Resultado:", resultado)