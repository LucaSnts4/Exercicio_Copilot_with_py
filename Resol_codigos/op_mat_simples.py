#Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")
resultado = 0  # Inicializando a variável resultado
# Usando condicionais para realizar a operação
if operacao == '+':
  resultado = num1 + num2
elif operacao == '-':
  resultado = num1 - num2
elif operacao == '*':
  resultado = num1 * num2
elif operacao == '/':
  if num2 == 0:
    print("Divisão por zero não é permitida.")
else:
	resultado = num1 / num2
print("Operação inválida.")
# Imprimindo o resultado
print("Resultado:", resultado)