numeros = []
while (numero := int(input("Digite um número inteiro (ou 0 para sair): "))) != 0:
    numeros.append(numero)

quantidade = len(numeros)
soma = sum(numeros)
media = soma / quantidade if quantidade > 0 else 0

print(f"Quantidade de números digitados: {quantidade}")
print(f"Soma dos números digitados: {soma}")
print(f"Média aritmética dos números digitados: {media}")
