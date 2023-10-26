numeros = []
numero = int(input("Digite um número inteiro (ou 0 para sair): "))

while numero != 0:
    numeros.append(numero)
    numero = int(input("Digite um número inteiro (ou 0 para sair): "))

quantidade = len(numeros)
soma = sum(numeros)
media = soma / quantidade

print("Quantidade de números digitados:", quantidade)
print("Soma dos números digitados:", soma)
print("Média aritmética dos números digitados:", media)
