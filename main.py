from GerenciamentoServicos import GerenciamentoServicos
from EstoqueProdutos import EstoqueProdutos

class MenuPrincipal:
    def __init__(self):
        self.gerenciamento_servicos = GerenciamentoServicos()
        self.estoque_produtos = EstoqueProdutos()
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
            print("1. Gerenciamento de Serviços")
            print("2. Estoque de Produtos")
            print("3. Gestão da Mercearia")
            print("4. Monitoramento Energético")
            print("5. Relatórios e Análises")
            print("6. Sair")

            opcao = input("Digite o número correspondente: ")

            if opcao == "1":
                self.menu_gerenciamento_servicos()
            elif opcao == "2":
                self.menu_estoque_produtos()
            elif opcao == "3":
                self.menu_gestao_mercearia()
            elif opcao == "4":
                self.menu_monitoramento_energetico()
            elif opcao == "5":
                self.menu_relatorio_analise()
            elif opcao == "6":
                print("A EcoEnergy agradece a preferência. Volte Sempre!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def menu_gerenciamento_servicos(self):
        while True:
            print("\nMenu Gerenciamento de Serviços:")
            print("1. Agendar serviço")
            print("2. Registrar serviço prestado")
            print("3. Histórico de serviços por cliente")
            print("4. Voltar ao menu principal")

            opcao = input("Digite o número correspondente: ")

            if opcao == "1":
                self.agendar_servico()
            elif opcao == "2":
                self.registrar_servico_prestado()
            elif opcao == "3":
                self.exibir_historico_servicos()
            elif opcao == "4":
                print("Voltando ao menu principal.")
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

    def menu_estoque_produtos(self):
        while True:
            print("\nMenu Estoque de Produtos:")
            print("1. Receber produtos")
            print("2. Vender produtos")
            print("3. Atualizar estoque após serviço")
            print("4. Emitir alertas de estoque baixo")
            print("5. Reordenar estoque")
            print("6. Mostrar situação do estoque")  # Novo item no menu
            print("7. Voltar ao menu principal")

            opcao = input("Digite o número correspondente: ")

            if opcao == "1":
                self.receber_produtos()
            elif opcao == "2":
                self.vender_produtos()
            elif opcao == "3":
                self.atualizar_estoque_apos_servico()
            elif opcao == "4":
                self.emitir_alertas()
            elif opcao == "5":
                self.reordenar_estoque()
            elif opcao == "6":
                self.estoque_produtos.mostrar_situacao_estoque()  # Chama o novo método
            elif opcao == "7":
                print("Voltando ao menu principal.")
                break
            else:
                print("Opção inválida. Tente novamente.")


    def receber_produtos(self):
        while True:
            produto = input("Digite o nome do produto a ser recebido (gasolina, álcool, diesel, energia solar): ").lower()
            if produto in ["gasolina", "álcool", "diesel", "energia solar"]:
                quantidade = int(input(f"Digite a quantidade de {produto} a ser recebida: "))
                self.estoque_produtos.receber_produtos(produto, quantidade)
                print(f"{quantidade} unidades de {produto} recebidas com sucesso.")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def vender_produtos(self):
        while True:
            produto = input("Digite o nome do produto a ser vendido (gasolina, álcool, diesel, energia solar): ").lower()
            if produto in ["gasolina", "álcool", "diesel", "energia solar"]:
                quantidade = int(input(f"Digite a quantidade de {produto} a ser vendida: "))
                self.estoque_produtos.vender_produtos(produto, quantidade)  # Correção aqui
                break
            else:
                print("Opção inválida. Tente novamente.")

    def atualizar_estoque_apos_servico(self):
        produto = input("Digite o nome do produto relacionado ao serviço (gasolina, álcool, diesel, energia solar): ")
        quantidade = int(input("Digite a quantidade usada no serviço: "))
        self.estoque_produtos.atualizar_estoque_apos_venda(produto, quantidade)
        print(f"Estoque atualizado após serviço de {produto}.")

    def emitir_alertas_estoque_baixo(self):
        alertas = self.estoque_produtos.emitir_alertas_estoque_baixo()
        for alerta in alertas:
            print(alerta)

    def reordenar_estoque(self):
        self.estoque_produtos.reordenar_estoque()
        print("Reordenando estoque de produtos.")

    def menu_gestao_mercearia(self):
        # Adicione a lógica para o módulo Gestão da Mercearia
        pass

    def menu_monitoramento_energetico(self):
        # Adicione a lógica para o módulo Monitoramento Energético
        pass

    def menu_relatorio_analise(self):
        # Adicione a lógica para o módulo Relatórios e Análises
        pass

if __name__ == "__main__":
    menu_principal = MenuPrincipal()
    menu_principal.exibir_menu()



