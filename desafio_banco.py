# -*- coding: utf-8 -*-

def depositar(saldo, extrato):
    valor = float(input("Digite o valor a ser depositado: R$ ").replace(",", "."))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor inválido! O valor do depósito deve ser positivo.")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, limite_saque, LIMITE_SAQUES):
    if numero_saques >= LIMITE_SAQUES:
        print("Limite diário de saques atingido.")
    else:
        valor = float(input("Digite o valor a ser sacado: R$ ").replace(",", "."))
        if valor > 0:
            if valor > limite_saque:
                print(f"Limite máximo por saque é de R$ {limite_saque:.2f}.")
            elif valor > saldo:
                print("Saldo insuficiente para realizar o saque.")
            else:
                saldo -= valor
                extrato.append(f"Saque: R$ {valor:.2f}")
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido! O valor do saque deve ser positivo.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n--- Extrato ---")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in extrato:
            print(movimento)
        print(f"\nSaldo atual: R$ {saldo:.2f}")

def main():
    saldo = 0
    limite_saque = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        print("\n--- Sistema Bancário ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "2":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, limite_saque, LIMITE_SAQUES)

        elif opcao == "3":
            exibir_extrato(saldo, extrato)

        elif opcao == "4":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()