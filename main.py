# Projeto Criando um sistema bancário com Python

#Variável setando saldo em 0
saldo = 0
#Variável com o limite de valor máximo que pode sacar
limite = 500
#Lista onde serão alocados os extratos.
extrato = []
#Variável onde conta a quantidade de saques realizados.
qtd_saques = 0
#Constante que informa o limite de saques
LIMITE_SAQUES = 3
#Listas para alocar os dados de cadastro de contas e usuários.
usuarios = []
contas = []

#Função menu
def menu():
  menu = """\n ---Opções--- \n 
  [d] Deposito \n
  [s] Saque \n
  [e] Extrato \n 
  [c] Cadastre-se \n
  [lc] Listar contas \n
  [q] Sair \n 
  \n
  => """

  return input(menu)

#Função depositar.
def depositar(valor):
    global saldo
    #Converte o valor em string para inteiro
    valor = int(valor)
    #Verificação se o valor é menor que 0
    if valor < 0:
        print('Digite um valor inteiro positivo!')
    #Soma o valor inserido à variável saldo;
    saldo = valor + saldo
    #Expõe na tela o valor depositado.
    print(f'Você depositou o valor de R$ {valor:.2f} na sua conta')
    #Retorna um append na lista de extrato.
    return extrato.append(f"Deposito no valor de R$ {valor:.2f}")

#Função saque de valores
def sacar(valor):
    global saldo
    global limite
    global qtd_saques
    global LIMITE_SAQUES
    #Converte o valor de str para int
    valor = int(valor)
    #Verifica se o valor é menor que 0
    if valor < 0:
        print('Digite um valor inteiro positivo')
    #Verifica se a quantidade de saques é menos que o limite de saques estabelecido.
    if qtd_saques < LIMITE_SAQUES:
        #Verifica se o valor é menor que ou igual ao limite que é possível sacar.
        if valor <= limite:
            #Verifica se o valor está disponível para saque, ou seja, tem no o suficiente no saldo.
            if valor <= saldo:
                #Faz o calculo da extração do valor.
                saldo = saldo - valor
                #Adiciona +1 a quantidade de saques.
                qtd_saques += 1
                #Exibe o valor que foi sacado.
                print(f'Você sacou R$ {valor:.2f}')
                #Retorna um append para o extrato.
                return extrato.append(f'Saque no valor de R$ {valor:.2f}')
            else:
                #Autoexplicativo
                print("O valor solicitado é maior que o disponível em conta. Digite outro valor")
        else:
            #Autoexplicativo
            print("O valor solicitado é maior que o limite de saque permitido. Digite outro valor")
    else:
        #Autoexplicativo
        print("A quantidade de limite diário foi excedido, volte amanhã")

#Função mostrar extrato c/saldo
def mostrar_extrato():
    print("+++++=====Extrato=====+++++")
    #Checa se tem item dentro da lista
    if len(extrato) == 0:
        print("Não houve movimentação")
    #Exibe os itens dentro da lista
    for i in extrato:
        print(i)
    #Exibe o saldo atual da conta.
    print(f"\n O valor total disponível em conta é R$ {saldo:.2f}")

#Função para cadastrar o usuário
def cadastrarUsuario(nome : str, dataNascimento : str, cpf : int, endereco : str):
  try:
  #Verificação, se a quantidade de números inseridos for diferente de 11, informa que o CPF está incorreto.
    if len(str(cpf)) != 11:
      return print('Digite um CPF válido')
    #Percorre a lista de usuários, checando CPF para verificar se o CPF inserido já consta dentro da lista.
    for usuario in usuarios:
      if usuario['cpf'] == cpf:
        return print('CPF já cadastrado.')
    #Aqui faz o append de todos os dados inseridos dentro da lista, sendo uma lista de dicionários.
    return usuarios.append({'nome':nome, 'data de nascimento':dataNascimento, 'cpf':cpf, 'endereco':endereco})
  except:
    print('error')

#Função de criação de contas
def criarContaCorrente():
  try:
  #Percorre a lista de usuários e seta o usuário
    for usuario in usuarios:
      usuario = usuario['cpf']

    #Faz a contagem das contas
    conta = len(contas) + 1

    #Aqui faz o append dos dados da conta.
    return contas.append({'agencia':'0001', 'conta':conta, 'usuario':usuario})
  except:
    print('error')

#Função de listar contas
def listar_contas():
  #Verifica se há algum item dentro da lista
  if len(contas) == 0:
    return print('Não há contas cadastradas.')

  print('+++++++Contas Cadastradas+++++++')
  #Percorre a lista contas
  for conta in contas:
    #Percorre cada item dentro do dicionario que está dentro da lista
    for indice, valor in conta.items():
      #Imprime os valores
      print(f'{indice} : {valor}')
    print('++++++++++++++++++++++++++++++++')  


#Função principal
def main():
  
  opcao = menu()

  while True:
    if opcao == 'd':
      print('---Opção deposito selecionada---')
      valor = input('Digite o valor que você deseja depositar: ')
      depositar(valor)
    elif opcao == 's':
      print('---Opção saque selecionada---')
      valor = input('Digite o valor que você deseja sacar: ')
      sacar(valor)
    elif opcao == 'e':
      mostrar_extrato()
    elif opcao == 'c':
      print('---Opção cadastro selecionada, digite os dados necessários---')
      nome = input('Digite seu nome completo: ')
      dataDeNascimento = input('Digite sua data de nascimento no modelo 00/00/0000: ')
      cpf = input('Digite seu CPF, apenas números: ')
      endereco = input('Digite seu endereço: ')
      cadastrarUsuario(nome, dataDeNascimento, cpf, endereco)
      criarContaCorrente()
    elif opcao == 'lc':
      print('---Opcao listar contas selecionada---')
      listar_contas()
    elif opcao == 'q':
      break
    else:
      print('Opção invalida.')   
    
main()
