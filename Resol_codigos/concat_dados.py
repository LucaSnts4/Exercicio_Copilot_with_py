# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!

#Utilizando f-strings (formatação de strings):
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
mensagem = f"Olá, {nome}! Você tem {idade} anos."
print(mensagem)
#As f-strings permitem inserir variáveis diretamente dentro de uma string utilizando chaves {}