# Inicialize variáveis
soma = 0
quantidade_valores = 0
maior_valor = float('-inf')

while True:
    entrada = input("Digite um valor (ou 'fim' para encerrar): ")

    if entrada.lower() == 'fim':
        break

    try:
        valor = float(entrada)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
        continue

    soma += valor
    quantidade_valores += 1
    if valor > maior_valor:
        maior_valor = valor

if quantidade_valores > 0:
    media = soma / quantidade_valores
    print(f"A média dos valores é: {media}")
    print(f"O maior valor inserido é: {maior_valor}")
else:
    print("Nenhum valor foi inserido.")
