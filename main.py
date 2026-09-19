class Cliente:
    def __init__(self, nome, email, telefone, endereco):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def __str__(self):
        return f"Nome: {self.nome} | E-mail: {self.email} | Telefone: {self.telefone} | Endereço: {self.endereco}"

class Cadastro:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self):
        print("\n====== Cadastro de Cliente ======")
        nome = input("\nDigite o nome do cliente: ")
        email = input("\nDigite o e-mail do cliente: ")
        # verificação simples se email é válido, retornando True se tiver "@" e "."
        if "@" in email and "." in email: 
            if email in [cliente.email for cliente in self.clientes]:
                        while True:
                            print("\nEste e-mail já está cadastrado. Por favor, insira um e-mail diferente.")
                            email = input("Digite o e-mail do cliente: ")
                            if email not in [cliente.email for cliente in self.clientes]:
                                break

        # se o email não for válido de acordo com a verificação simples, entra no loop de validação
        else:
            while True:
                print("\nE-mail inválido. Por favor, insira um e-mail válido.")
                email = input("Digite o e-mail do cliente: ")
                if "@" in email and "." in email:
                    break
        
        telefone = input("\nDigite o telefone do cliente: ")
        if telefone in [cliente.telefone for cliente in self.clientes]:
            while True:
                print("\nEste telefone já está cadastrado. Por favor, insira um telefone diferente.")
                telefone = input("Digite o telefone do cliente: ")
                if telefone not in [cliente.telefone for cliente in self.clientes]:
                    break
        
        endereco = input("\nDigite o endereço do cliente: ")

        novo_cliente = Cliente(nome, email, telefone, endereco)
        self.clientes.append(novo_cliente)
        print("\n====== Cadastro Concluído! ======")

    def listar_clientes(self):
        print("\n====== Clientes Cadastrados ======")
        if not self.clientes:
            print("\nNenhum cliente cadastrado.")
            return
        
        for cliente in self.clientes:
            print(cliente)

class Menu:
    def __init__(self):
        self.cadastro = Cadastro()

    def exibir_menu(self):
        while True:
            print("\nMenu:")
            print("[1] Cadastrar cliente")
            print("[2] Listar clientes")
            print("[3] Sair")

            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                self.cadastro.cadastrar_cliente()
            elif opcao == "2":
                self.cadastro.listar_clientes()
                input("\nPressione Enter para voltar ao menu... ")

            elif opcao == "3":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

menu = Menu()
menu.exibir_menu()



