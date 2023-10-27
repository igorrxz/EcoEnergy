from GerenciamentoServicos import GerenciamentoServicos
from EstoqueProdutos import EstoqueProdutos
from GestaoMercearia import GestaoMercearia
from MonitoramentoEnergetico import MonitoramentoEnergetico
from RelatorioAnalise import RelatorioAnalise

class MenuPrincipal:
    def __init__(self):
        self.gerenciamento_servicos = GerenciamentoServicos()
        self.estoque_produtos = EstoqueProdutos()
        self.gestao_mercearia = GestaoMercearia()
        self.monitoramento_energetico = MonitoramentoEnergetico()
        self.relatorio_analise = RelatorioAnalise()
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
                self.emitir_alertas_estoque_baixo()
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
        while True:
            print("\nMenu Gestão da Mercearia:")
            print("1. Adicionar produto à mercearia")
            print("2. Registrar venda de produto")
            print("3. Análise de desempenho de produto")
            print("4. Emitir alertas de reposição")
            print("5. Voltar ao menu principal")

            opcao = input("Digite o número correspondente: ")

            if opcao == "1":
                self.adicionar_produto_mercearia()
            elif opcao == "2":
                self.registrar_venda_mercearia()
            elif opcao == "3":
                self.analisar_desempenho_produto_mercearia()
            elif opcao == "4":
                self.emitir_alertas_reposicao_mercearia()
            elif opcao == "5":
                print("Voltando ao menu principal.")
                break
            else:
                print("Opção inválida. Tente novamente.")
    
    def adicionar_produto_mercearia(self):
        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade a ser adicionada: "))
        detalhes = input("Digite os detalhes do produto: ")
        self.gestao_mercearia.adicionar_produto(nome, quantidade, detalhes)
        print(f"{quantidade} unidades de {nome} adicionadas à mercearia.")

    def registrar_venda_mercearia(self):
        nome = input("Digite o nome do produto a ser vendido: ")
        quantidade = int(input("Digite a quantidade a ser vendida: "))
        self.gestao_mercearia.registrar_venda(nome, quantidade)

    def analisar_desempenho_produto_mercearia(self):
        nome = input("Digite o nome do produto para análise: ")
        self.gestao_mercearia.analisar_desempenho_produto(nome)

    def emitir_alertas_reposicao_mercearia(self):
        self.gestao_mercearia.emitir_alertas_reposicao()
        print("Alertas de reposição emitidos.")

    def menu_monitoramento_energetico(self):
        monitoramento_energetico = MonitoramentoEnergetico()
        
        while True:
            print("\nMenu Monitoramento Energético:")
            print("1. Adicionar energia solar gerada")
            print("2. Análise de desempenho da energia solar")
            print("3. Alertas de baixa geração de energia solar")
            print("4. Voltar ao menu principal")

            opcao = input("Digite o número correspondente: ")

            if opcao == "1":
                quantidade_energia = float(input("Digite a quantidade de energia solar gerada (em kWh): "))
                monitoramento_energetico.adicionar_energia_solar(quantidade_energia)
                print(f"{quantidade_energia} kWh de energia solar adicionados com sucesso.")
            elif opcao == "2":
                desempenho = monitoramento_energetico.analisar_desempenho_energia_solar()
                print(desempenho)
            elif opcao == "3":
                alertas = monitoramento_energetico.alerta_baixa_geracao_solar()
                if alertas:
                    for alerta in alertas:
                        print(alerta)
                else:
                    print("Nenhum alerta de baixa geração de energia solar.")
            elif opcao == "4":
                print("Voltando ao menu principal.")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def menu_relatorio_analise(self):
        while True:
            print("\nMenu Relatórios e Análises:")
            print("1. Gerar relatório de vendas")
            print("2. Gerar relatório de serviços")
            print("3. Gerar relatório de energia solar")
            print("4. Voltar ao menu principal")

            opcao = input("Digite o número correspondente: ")

            if opcao == "1":
                periodo = input("Digite o período do relatório (diário, semanal, mensal): ")
                relatorio = self.relatorio_analise.gerar_relatorio_vendas(periodo)
                print("Relatório de Vendas:")
                for data, produto, quantidade, preco, cliente in relatorio:
                    print(f"Data: {data}, Produto: {produto}, Quantidade: {quantidade}, Preço: {preco}, Cliente: {cliente}")

            elif opcao == "2":
                periodo = input("Digite o período do relatório (diário, semanal, mensal): ")
                relatorio = self.relatorio_analise.gerar_relatorio_servicos(periodo)
                print("Relatório de Serviços:")
                for data, tipo_servico, cliente, detalhes in relatorio:
                    print(f"Data: {data}, Tipo de Serviço: {tipo_servico}, Cliente: {cliente}, Detalhes: {detalhes}")

            elif opcao == "3":
                periodo = input("Digite o período do relatório (diário, semanal, mensal): ")
                relatorio = self.relatorio_analise.gerar_relatorio_energia_solar(periodo)
                print("Relatório de Energia Solar:")
                for data, quantidade in relatorio:
                    print(f"Data: {data}, Quantidade: {quantidade} kWh")

            elif opcao == "4":
                break

if __name__ == "__main__":
    menu_principal = MenuPrincipal()
    menu_principal.exibir_menu()


"""
__init__(self): O construtor da classe inicializa várias instâncias de diferentes classes, como GerenciamentoServicos, EstoqueProdutos, GestaoMercearia, 
MonitoramentoEnergetico e RelatorioAnalise. Ele também cria uma lista chamada servicos_disponiveis para rastrear os tipos de serviços disponíveis.

exibir_menu(self): Este método inicia um loop que exibe um menu principal e permite que o usuário escolha uma opção. 
As opções possíveis são 1 a 6 (gerenciamento de serviços, estoque de produtos, gestão da mercearia, monitoramento energético, relatórios e sair). 
Dependendo da opção escolhida, ele chama um método de menu correspondente.

menu_gerenciamento_servicos(self): Este método lida com as opções relacionadas ao gerenciamento de serviços. 
Permite ao usuário agendar um serviço, registrar um serviço prestado e visualizar o histórico de serviços por cliente.

menu_estoque_produtos(self): Este método lida com as opções relacionadas ao estoque de produtos. 
Ele permite ao usuário receber produtos, vender produtos, atualizar o estoque após um serviço, emitir alertas de estoque baixo, 
reordenar o estoque e mostrar a situação atual do estoque.

menu_gestao_mercearia(self): Este método lida com as opções relacionadas à gestão da mercearia. 
Ele permite ao usuário adicionar produtos à mercearia, registrar vendas de produtos, analisar o desempenho de produtos e emitir alertas de reposição.

menu_monitoramento_energetico(self): Este método lida com as opções relacionadas ao monitoramento energético. 
Ele permite ao usuário adicionar a quantidade de energia solar gerada, analisar o desempenho da energia solar e verificar alertas de baixa geração de energia solar.

menu_relatorio_analise(self): Este método lida com as opções relacionadas à geração de relatórios e análises. 
Ele permite ao usuário gerar relatórios de vendas, relatórios de serviços e relatórios de energia solar para diferentes períodos (diário, semanal, mensal).

agendar_servico(self): Este método permite que o usuário agende um serviço especificando o cliente e o tipo de serviço.

registrar_servico_prestado(self): Este método permite que o usuário registre um serviço prestado, fornecendo detalhes do serviço.

exibir_historico_servicos(self): Este método permite ao usuário visualizar o histórico de serviços de um cliente específico.

mostrar_servicos_disponiveis(self): Este método exibe os tipos de serviços disponíveis para o usuário escolher ao agendar ou registrar um serviço.

receber_produtos(self): Permite ao usuário receber produtos especificando o tipo de produto e a quantidade a ser recebida.

vender_produtos(self): Permite ao usuário vender produtos especificando o tipo de produto e a quantidade a ser vendida.

atualizar_estoque_apos_servico(self): Atualiza o estoque após um serviço específico.

emitir_alertas_estoque_baixo(self): Emite alertas se o estoque de produtos estiver baixo.

reordenar_estoque(self): Reordena o estoque de produtos automaticamente.

adicionar_produto_mercearia(self): Permite ao usuário adicionar produtos à mercearia.

registrar_venda_mercearia(self): Registra vendas de produtos da mercearia.

analisar_desempenho_produto_mercearia(self): Permite ao usuário analisar o desempenho de um produto da mercearia.

emitir_alertas_reposicao_mercearia(self): Emite alertas de reposição para produtos na mercearia com estoque esgotado.

menu_monitoramento_energetico(self): Menu para gerenciar aspectos relacionados ao monitoramento energético, 
incluindo a adição de energia solar, análise de desempenho e alertas.

menu_relatorio_analise(self): Menu para geração de relatórios e análises sobre vendas, serviços e energia solar.

if __name__ == "__main__":: Isso garante que o código no bloco seja executado somente quando o script é executado como um programa principal. 
Aqui, ele cria uma instância do MenuPrincipal e exibe o menu principal para o usuário.

O código é uma interface interativa para diferentes funcionalidades do sistema e coordena a interação com os diferentes módulos e classes que fazem parte do sistema de gestão de negócios.
"""
