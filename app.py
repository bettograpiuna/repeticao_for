# 1. PEÇA UM NÚMERO
numero = int(input("Digite um número entre 1 e 10: "))

# 2. VERIFIQUE SE O NÚMERO É VÁLIDO
if numero >= 1 and numero <= 10:
    print(f"Tabuada do {numero}:")
    
    # 3. FAÇA AS CONTAS E MOSTRE O RESULTADO
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
else:
    # 4. MOSTRE UMA MENSAGEM DE ERRO
    print("Número inválido. Por favor, digite um número entre 1 e 10.")