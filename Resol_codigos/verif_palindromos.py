#Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

def eh_palindromo(palavra):
  return palavra.lower() == palavra.lower()[::-1]

palavra = input("Digite uma palavra: ")

print("É um palíndromo!" if eh_palindromo(palavra) else "Não é um palíndromo!")
