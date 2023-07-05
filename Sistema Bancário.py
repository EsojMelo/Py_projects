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


'''Variaveis'''

saque = 0
extrato = 0
linhas_nome("BANCO")

lista_depositos = []
lista_saques = []
total_na_conta = 0
limite_de_saques = 500.00
qtd_saques = 3
count_saques = 0
lista_extrato = []

while True:
    linhas_vazias()
    opcoes()
    opcao_escolhida = str(input("Digite aqui: "))
    if opcao_escolhida == "1":
        depositar = round(float(input(f'Valor de deposito:')), 2)
        if depositar > 0:
            print(f"DEPOSITO DE R${depositar:.2f} BEM SUCEDIDO")
            total_na_conta = total_na_conta + depositar
            lista_depositos.append(depositar)
            lista_extrato.append(f"Desposito: R${depositar:.2f}")
        else:
            print("Não foi possível fazer esse depósito")
            print("tente novamente")
    elif opcao_escolhida == "2":
        if qtd_saques - count_saques == 0:
            linhas_vazias()
            print("Você atingiu o limite de 3 saques diários")
            print("Tente amanhã")
        else:
            while True:
                linhas_vazias()
                print(f"Você ainda possui {qtd_saques - count_saques} saques diários")
                valor_do_saque = round(float(input(f"Valor do saque:")), 2)
                if valor_do_saque > 0:
                    if valor_do_saque <= total_na_conta and valor_do_saque <= limite_de_saques:
                        total_na_conta = total_na_conta - valor_do_saque
                        count_saques = count_saques + 1
                        lista_saques.append(valor_do_saque)
                        print(f"SAQUE DE R${valor_do_saque:.2f} BEM SUCEDIDO.")
                        lista_extrato.append(f"Saque: R${valor_do_saque:.2f}")
                        break
                    elif valor_do_saque > limite_de_saques:
                        print("Não é possível realizar essa operação")
                        print(f"Você pode sacar até R${limite_de_saques:.2f} por saque")
                        print("para continuar essa operação digite: 1\n"
                              "Para retornar ao menu digite: 2")
                        encerrar = int(input("Digite aqui: "))
                        if encerrar == 2:
                            break
                    else:
                        print("Não foi possível realizar essa operação:")
                        print(f"Você tem R${total_na_conta:.2f} na conta")
                        print("para continuar essa operação digite: 1\n"
                              "Para retornar ao menu digite: 2")
                        encerrar = int(input("Digite aqui: "))
                        if encerrar == 2:
                            break
                else:
                    print("Valor inválido, tente novamente")
                    print("para continuar essa operação digite: 1\n"
                          "Para retornar ao menu digite: 2")
                    encerrar = int(input("Digite aqui: "))
                    if encerrar == 2:
                        break
    elif opcao_escolhida == "3":
        linhas_nome("EXTRATO")
        for valores in lista_extrato:
            print(valores)
        linhas_nome("DEPOSITOS")
        for valores in lista_depositos:
            print(f"|R${valores:.2f}|", end=" ")
        print(f"\nTOTAL DE DEPOSITOS: R${sum(lista_depositos)}")
        linhas_vazias()
        linhas_nome("SAQUES")
        for valores in lista_saques:
            print(f"|R${valores:.2f}|", end=" ")
        print(f"\nTOTAL DE SAQUES: R${sum(lista_saques):.2f}")
        linhas_nome("SALDO ATUAL")
        print(f"|R$ {total_na_conta:.2f}|")
        enter = input("Aperte ENTER para voltar ao menu")

    elif opcao_escolhida == "4":
        print("Operação encerrada com sucesso")
        linhas_nome("VOLTE SEMPRE")
        break

    else:
        print("Valor invalido, tente novamente")
