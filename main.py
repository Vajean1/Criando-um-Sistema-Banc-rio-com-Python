# Projeto Criando um sistema bancário com Python

menu = "\n Opções \n [D] Deposito \n [S] Saque \n [E] Extrato \n [Q] Sair \n => "

saldo = 0
limite = 500
extrato = []
qtd_saques = 0
LIMITE_SAQUES = 3

def depositar(valor):
    global saldo
    
    valor = int(valor)
    
    if valor < 0:
        print('Digite um valor inteiro positivo!')
    saldo = valor + saldo
    print(f'Você depositou o valor de R$ {valor:.2f} na sua conta')
    return extrato.append(f"Deposito no valor de R$ {valor:.2f}")

def sacar(valor):
    global qtd_saques
    global saldo
    global limite
    valor = int(valor)
    if valor < 0:
        print('Digite um valor inteiro positivo')
    
    if qtd_saques < LIMITE_SAQUES:
        if valor <= limite:
            if valor <= saldo:
                saldo = saldo - valor
                qtd_saques = qtd_saques + 1
                print(f'Você sacou R$ {valor:.2f}')
                return extrato.append(f'Saque no valor de R$ {valor:.2f}')
            else:
                print("O valor solicitado é maior que o disponível em conta. Digite outro valor")
        else:
            print("O valor solicitado é maior que o limite de saque permitido. Digite outro valor")
    else:
        print("A quantidade de limite diário foi excedido, volte amanhã")  

    
def mostrar_extrato():
    global saldo
    
    print("=====Extrato=====")
    
    if len(extrato) == 0:
        print("Não houve movimentação")
        
    for i in extrato:
        print(i)

    print(f"\n O valor total disponível em conta é R$ {saldo:.2f}")


while True:
    opcao = input(menu)
    
    if opcao == "d":
        print("Opção deposito selecionada: \n")
        valor = input("Digite o valor que você quer depositar:")
        depositar(valor)
    elif opcao == "s":
        print("Opção saque selecionada: \n")
        valor = input("Qual valor você deseja sacar: ")
        sacar(valor)
    elif opcao == "e":
        print("Opção extrato:")
        print("Segue extrato:")
        mostrar_extrato()
    elif opcao == "q":
        break
    else:
        print("Operação inválida")
    

    
