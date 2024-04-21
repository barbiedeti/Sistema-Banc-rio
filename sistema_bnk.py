menu = """

[d] depositar
[s] sacar
[e] extrato bancário
[o] Sair

"""

saldo = 0
limite = 5000
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"
            print(f"O valor de R$: {valor: .2f} \n foi depositado com sucesso!")

        else:
            print("Valor informado inválido! Tente novamente")

    elif opcao == "s":
        valor = float(input("Informe o valor desejado para saque:"))
        print(f"O valor de R$: {valor: .2f} \n foi sacado com sucesso!")

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Você não tem saldo suficiente!")

        elif excedeu_limite:
            print("O Valor do saque ultrapassou o limite disponível em conta. Tente novamente")

        elif excedeu_saques:
            print("Limite de saques diário excedidos. Tente novamente mais tarde")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor: .2f}\n"

        else:
            print("Operação falhou. O valor informado é inválido")

    elif opcao == "e":
        print("\n ========= EXTRATO ========")
        print("Não houve movimentações bancárias" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "o":
        print("Operaçao encerrada. Obrigado!")

    else:
        print("Operação falhou. Volte ao menu inicial")
        opcao = input(menu)

    


