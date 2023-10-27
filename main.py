from GerenciamentoServicos import GerenciamentoServicos

# Lista de serviços disponíveis relacionados a um posto de gasolina
servicos_disponiveis = ["Abastecimento de gasolina", "Abastecimento de álcool", "Abastecimento de diesel",
                       "Troca de óleo", "Balanceamento de rodas", "Lavagem de carro", "Reparo de pneus"]

class MenuPrincipal:
    def __init__(self):
        self.gerenciamento_servicos = GerenciamentoServicos()
        self.servicos_disponiveis = [
            "Abastecimento de gasolina",
            "Abastecimento de álcool",
            "Abastecimento de diesel",
            "Troca de óleo",
            "Balanceamento de rodas",
            "Lavagem de carro",
            "Reparo de pneus"
        ]

    def exibir_menu(self):
        while True:
            print("\nEscolha uma opção:")
            print("1. Agendar serviço")
            print("2. Registrar serviço prestado")
            print("3. Histórico de serviços por cliente")
            print("4. Sair")

            opcao = input("Digite o número correspondente: ")

            if opcao == "1":
                self.agendar_servico()
            elif opcao == "2":
                self.registrar_servico_prestado()
            elif opcao == "3":
                self.exibir_historico_servicos()
            elif opcao == "4":
                print("A EcoEnergy agradece a preferência. Volte Sempre!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def agendar_servico(self):
        cliente = input("Digite o nome do cliente: ")
        self.mostrar_servicos_disponiveis()
        servico_escolhido = int(input("Digite o número do serviço desejado: "))
        if 1 <= servico_escolhido <= len(self.servicos_disponiveis):
            servico = self.servicos_disponiveis[servico_escolhido - 1]
            self.gerenciamento_servicos.agendar_servico(cliente, servico)
            print(f"{servico} agendado com sucesso para {cliente}.")
        else:
            print("Opção inválida. Tente novamente.")

    def registrar_servico_prestado(self):
        cliente = input("Digite o nome do cliente: ")
        self.mostrar_servicos_disponiveis()
        servico_escolhido = int(input("Digite o número do serviço prestado: "))
        if 1 <= servico_escolhido <= len(self.servicos_disponiveis):
            servico = self.servicos_disponiveis[servico_escolhido - 1]
            detalhes = input("Digite os detalhes do serviço: ")
            self.gerenciamento_servicos.registrar_servico(cliente, servico, detalhes)
            print(f"{servico} registrado com sucesso para {cliente}.")
        else:
            print("Opção inválida. Tente novamente.")

    def exibir_historico_servicos(self):
        cliente = input("Digite o nome do cliente: ")
        historico = self.gerenciamento_servicos.historico_servicos(cliente)
        if historico:
            print(f"Histórico de serviços para {cliente}:")
            for i, servico in enumerate(historico, start=1):
                print(f"{i}. {servico}")
        else:
            print(f"Nenhum serviço encontrado para {cliente}")

    def mostrar_servicos_disponiveis(self):
        print("Escolha um tipo de serviço:")
        for i, servico in enumerate(self.servicos_disponiveis, start=1):
            print(f"{i}. {servico}")

if __name__ == "__main__":
    menu = MenuPrincipal()
    menu.exibir_menu()