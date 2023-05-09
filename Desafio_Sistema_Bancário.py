menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saque = 0
saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d": 
        valor = float(input("Digite o valor a ser depositado: "))
        if valor>0:
            saldo += valor
            extrato += f"Depósito: {valor:.2f}\n"
        else:
            print("Operação falhou pois o valor é inválido.")

    elif opcao == "s": 
        valor = float(input("Digite o valor a ser sacado: "))
        if valor>0 and saldo>=valor:
            saldo -= valor
            extrato += f"Saque: {valor:2f}\n"
        else:
            print("Operação falhou pois o valor é inválido.")
        
    elif opcao == "e": print(extrato)
    elif opcao == "q": break
    else: print("Opção inválida, selecione novamente.")




