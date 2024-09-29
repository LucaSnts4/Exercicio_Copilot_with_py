#Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

# Obter a entrada do usuário
string_original = input("Digite a string: ")

# Solicitar o número de repetições
num_repeticoes = int(input("Digite o número de repetições (não negativo): "))

# Repetir a string
resultado = string_original * num_repeticoes

# Imprimir o resultado
print(resultado)
