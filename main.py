# Projeto Criando um sistema bancário com Python 

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        if len(str(cpf)) != 11:
            raise ValueError("CPF inválido! Deve conter 11 dígitos.")
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
    
    def __repr__(self):
        return f"Usuário(nome={self.nome}, CPF={self.cpf})"


class ContaCorrente:
    LIMITE_SAQUES = 3

    def __init__(self, usuario):
        self.agencia = '0001'
        self.numero = ContaCorrente.gerar_numero_conta()
        self.usuario = usuario
        self.saldo = 0
        self.limite = 500
        self.extrato = []
        self.qtd_saques = 0

    @staticmethod
    def gerar_numero_conta():
        return len(banco.contas) + 1  # Gerar número de conta baseado na quantidade de contas

    def depositar(self, valor):
        valor = float(valor)
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo += valor
        self.extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Você depositou R$ {valor:.2f}")

    def sacar(self, valor):
        valor = float(valor)
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if self.qtd_saques >= ContaCorrente.LIMITE_SAQUES:
            print("Limite diário de saques excedido.")
            return
        if valor > self.limite:
            print(f"Valor excede o limite de saque de R$ {self.limite:.2f}.")
            return
        if valor > self.saldo:
            print(f"Saldo insuficiente. Saldo atual: R$ {self.saldo:.2f}.")
            return
        self.saldo -= valor
        self.qtd_saques += 1
        self.extrato.append(f"Saque: R$ {valor:.2f}")
        print(f"Você sacou R$ {valor:.2f}")

    def mostrar_extrato(self):
        print("+++++ EXTRATO +++++")
        if not self.extrato:
            print("Nenhuma movimentação.")
        for linha in self.extrato:
            print(linha)
        print(f"Saldo atual: R$ {self.saldo:.2f}")


class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []

    def cadastrar_usuario(self, nome, data_nascimento, cpf, endereco):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                print("CPF já cadastrado.")
                return
        novo_usuario = Usuario(nome, data_nascimento, cpf, endereco)
        self.usuarios.append(novo_usuario)
        print(f"Usuário {nome} cadastrado com sucesso!")

    def criar_conta_corrente(self, cpf_usuario):
        for usuario in self.usuarios:
            if usuario.cpf == cpf_usuario:
                nova_conta = ContaCorrente(usuario)
                self.contas.append(nova_conta)
                print(f"Conta criada com sucesso para {usuario.nome}. Agência: {nova_conta.agencia}, Conta: {nova_conta.numero}")
                return
        print("Usuário não encontrado. Cadastre o usuário primeiro.")

    def listar_contas(self):
        if not self.contas:
            print("Nenhuma conta cadastrada.")
            return
        print("+++++ CONTAS +++++")
        for conta in self.contas:
            print(f"Agência: {conta.agencia}, Conta: {conta.numero}, Usuário: {conta.usuario.nome}")

# Instanciando o banco
banco = Banco()

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

def main():
    while True:
        opcao = menu()

        if opcao == 'd':
            cpf = input("Digite seu CPF: ")
            for conta in banco.contas:
                if conta.usuario.cpf == cpf:
                    valor = float(input("Digite o valor a ser depositado: "))
                    conta.depositar(valor)
                    break
            else:
                print("Conta não encontrada.")

        elif opcao == 's':
            cpf = input("Digite seu CPF: ")
            for conta in banco.contas:
                if conta.usuario.cpf == cpf:
                    valor = float(input("Digite o valor a ser sacado: "))
                    conta.sacar(valor)
                    break
            else:
                print("Conta não encontrada.")

        elif opcao == 'e':
            cpf = input("Digite seu CPF: ")
            for conta in banco.contas:
                if conta.usuario.cpf == cpf:
                    conta.mostrar_extrato()
                    break
            else:
                print("Conta não encontrada.")

        elif opcao == 'c':
            nome = input("Nome completo: ")
            data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
            cpf = input("CPF (somente números): ")
            endereco = input("Endereço: ")
            banco.cadastrar_usuario(nome, data_nascimento, cpf, endereco)
            banco.criar_conta_corrente(cpf)

        elif opcao == 'lc':
            banco.listar_contas()

        elif opcao == 'q':
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
  
