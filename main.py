class Cliente:
    def __init__(self, id, nome, email, telefone, endereco):
        # atributos privados
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_telefone(telefone)
        self.set_endereco(endereco)


    # GETTERS (ACESSAR OS ATRIBUTOS)
    def get_id(self):
        return self._id

    def get_nome(self):
        return self._nome

    def get_email(self):
        return self._email

    def get_telefone(self):
        return self._telefone

    def get_endereco(self):
        return self._endereco

    # SETTERS (ALTERAR OS ATRIBUTOS)
    def set_id(self, id):
        if not str(id).isdigit():
            raise ValueError("O ID deve ser um número inteiro.")
        self._id = int(id)

    def set_nome(self, nome):
        if not nome or len(nome) < 3:
            raise ValueError("O nome deve ter pelo menos 3 caracteres.")
        self._nome = nome

    def set_email(self, email):
        if "@" not in email or "." not in email:
            raise ValueError("E-mail inválido. Por favor, insira um e-mail válido.")
        self._email = email

    def set_telefone(self, telefone):
        if not telefone.isdigit() or len(telefone) < 8:
            raise ValueError("Telefone inválido. Por favor, insira um telefone válido.")
        self._telefone = telefone

    def set_endereco(self, endereco):
        if not endereco or len(endereco) < 4:
            raise ValueError("O endereço deve ter pelo menos 4 caracteres.")
        self._endereco = endereco

    def __str__(self):
        return (f"ID: {self._id} | Nome: {self._nome} | E-mail: {self._email} | "
                f"Telefone: {self._telefone} | Endereço: {self._endereco}")

class Cadastro:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self):
        print("\n====== Cadastro de Cliente ======")
        id = input("\nDigite o ID do cliente: ")
        # verifica se o id ja esta cadastrado
        if id in [str(cliente.get_id()) for cliente in self.clientes]:
            while True:
                print("\nEste ID já está cadastrado. Por favor, insira um ID diferente.")
                id = input("Digite o ID do cliente: ")
                if id not in [str(cliente.get_id()) for cliente in self.clientes]:
                    break

        nome = input("\nDigite o nome do cliente: ")

        email = input("\nDigite o e-mail do cliente: ")
        # verifica se o email ja esta cadastrado
        if email in [cliente.get_email() for cliente in self.clientes]:
                    while True:
                        print("\nEste e-mail já está cadastrado. Por favor, insira um e-mail diferente.")
                        email = input("Digite o e-mail do cliente: ")
                        if email not in [cliente.get_email() for cliente in self.clientes]:
                            break
        
        telefone = input("\nDigite o telefone do cliente: ")
        # verifica se o telefone ja esta cadastrado
        if telefone in [cliente.get_telefone() for cliente in self.clientes]:
            while True:
                print("\nEste telefone já está cadastrado. Por favor, insira um telefone diferente.")
                telefone = input("Digite o telefone do cliente: ")
                if telefone not in [cliente.get_telefone() for cliente in self.clientes]:
                    break
        
        endereco = input("\nDigite o endereço do cliente: ")

        try:
            novo_cliente = Cliente(id, nome, email, telefone, endereco)
            self.clientes.append(novo_cliente)
            print("\n====== Cadastro Concluído! ======")
        except ValueError as e:
            print(f"\nErro ao cadastrar cliente: {e}")

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