def linhas_nome(nome):
    print(f"{nome:=^40}")


def linhas_vazias():
    print(40 * "=")


def opcoes():
    print(f"{'Menu Principal':^40}")
    print("Escolha:\n"
          "1 - para depositar\n"
          "2 - para sacar\n"
          "3 - para ver o extrato\n"
          "4 - Sair")

def deposito(saldo, valor, extrato):
    valor = float(input(f'Valor de deposito:'))
    if valor > 0:
        print(f"DEPOSITO DE R${valor:.2f} BEM SUCEDIDO")
        saldo = saldo + valor
        extrato = f"Deposito: {valor}"
    else:
        print("Não foi possível fazer esse depósito")
        print("Número inválido, tente novamente")
    return valor, saldo, extrato

def saque(saldo = saldo, valor = valor, extrato = extrato, limite = 500, numeros_saques = numeros_saques, limite_saques = 3):
        if numeros_saques == limite_saques:
            linhas_vazias()
            print("Você atingiu o limite de 3 saques diários")
            print("Tente amanhã")
        else:
            linhas_vazias()
            print(f"Você ainda possui {limite_saques - numeros_saques} saques diários")
            valor = float(input(f"Valor do saque:"))
            if valor > 0:
                
                if valor <= saldo and valor <= limite:
                    valor = saldo - valor
                    numeros_saques = numeros_saques + 1
                    extrato.append(f"Saque: {valor}")
                    print(f"SAQUE DE R${valor:.2f} BEM SUCEDIDO.")           
                
                elif valor > limite:
                    print("Não é possível realizar essa operação")
                    print(f"Você pode sacar até R${limite:.2f} por saque")
                
                else:
                    print("Não foi possível realizar essa operação, tente novamente")
                    print(f"Você tem R${saldo:.2f} na conta")
            else:
                print("Valor inválido, tente novamente")
        return saldo, extrato

def extrato(saldo, extrato = extrato):
    saldo = sum(deposito(saldo) )

'''Variaveis'''
linhas_nome("BANCO")
lista_extrato = []
while True:
    linhas_vazias()
    opcoes()
    opcao_escolhida = str(input("Digite aqui: "))
    if opcao_escolhida == "1":
        deposito()
        lista_extrato = deposito
    elif opcao_escolhida == "2":
        saque(saldo=deposito,extrato=deposito )
    elif opcao_escolhida == "3":
       
    elif opcao_escolhida == "4":
        print("Operação encerrada com sucesso")
        linhas_nome("VOLTE SEMPRE")
        break

    else:
        print("Valor invalido, tente novamente")
