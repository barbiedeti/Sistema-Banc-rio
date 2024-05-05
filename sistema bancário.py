import textwrap

def menu():
    menu = """\n
    =========== MENU ===========
    [d] \tDepositar
    [s] \tSacar
    [e] \tExtrato Bancário
    [cc] \tListar Contas
    [c] \tNova Conta
    [u] \tNovo Usuário
    [o] \tSair
    """
    return input(textwrap.dedent(menu))

def depositar(saldo, extrato):
    valor = float(input("Informe o valor que deseja depositar:"))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor: .2f}\n"
        print(f"O valor de R$: {valor: .2f} \n foi depositado com sucesso!")

    else:
        print("Valor informado inválido! Tente novamente")
    return saldo, extrato

def sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUE):
    valor = float(input("Informe o valor para saque:"))
    print(f"O valor de R$: {valor: .2f} \n foi sacado com sucesso!")

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUE

    if excedeu_saldo:
        print("Você não possui saldo suficiente!")

    elif excedeu_limite:
        print("O Valor do saque ultrapassou o limite disponível em conta. Tente novamente")

    elif excedeu_saques:
        print("Limite de saques diário excedidos. Tente novamente mais tarde")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor: .2f}\n"

    else:
        print("Operação falhou. O valor informado é inválido")
    return saldo, extrato

def extrato(saldo, extrato):
    print("\n ========= EXTRATO ========")
    print("Não houve movimentações bancárias" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def novo_usuario(usuario):
    cpf = input("Por favor, informe seu CPF:")
    usuario = filtrar_usuario(cpf, usuario)

    if usuario:
        print("Usuário já cadastrado")
        return
    nome = input("Informe seu nome:")
    usuario = []

    data_nascimento = input("Informe sua data de nascimento:")
    endereco = input("Informe seu endereço (TIPO, NUMERO, BAIRRO, CIDADE/ESTADO):")
    cpf = input("Informe seu CPF:")

    usuario.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário cadastrado com sucesso!")
    return usuario

def filtrar_usuario(cpf, usuario):
    for user in usuario:
        if user["cpf"] == cpf:
            return user

    return None

def nova_conta(agencia, numero_conta, usuario, saldo, contas):
    cpf = input("Informe o CPF do usuário:")
    usuario = filtrar_usuario(cpf, usuario)

    if not usuario:
        print("Usuário não encontrado. Cadastre um novo usuário")
        return

    limite = float(input("Informe o limite da conta:"))

    contas.append({"agencia": agencia, "numero_conta": numero_conta, "saldo": saldo, "limite": limite, "cpf": cpf})
    print("Conta cadastrada com sucesso!")

def listar_contas(contas):
    print("\n ========= CONTAS =========")
    for conta in contas:
        print(f"Agência: {conta['agencia']}")
        print(f"Conta: {conta['numero_conta']}")
        print(f"Saldo: {conta['saldo']}")
        print(f"Limite: {conta['limite']}")
        print(f"CPF: {conta['cpf']}")
        print("==========================================")

def main():
    saldo = 0
    extrato = ""
    agencia = "0001"
    contas = []
    usuario = []  # Defina a lista de usuários aqui

    while True:
        opcao = menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            limite = 5000  
            LIMITE_SAQUE = 3 
            numero_saques = 0 

            saldo, extrato = sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUE)

        elif opcao == "e":
            extrato(saldo, extrato)

        elif opcao == "u":
            usuario = novo_usuario(usuario)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            nova_conta(agencia, numero_conta, usuario, saldo, contas)

        elif opcao == "cc":
            listar_contas(contas)

        elif opcao == "o":
            print("Operação encerrada. Obrigado!")
            break
        else:
            print("Operação falhou. Volte ao menu inicial")
            opcao = input(menu)

main()
