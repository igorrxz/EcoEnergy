from GerenciamentoServicos import GerenciamentoServicos

# Lista de serviços disponíveis relacionados a um posto de gasolina
servicos_disponiveis = ["Abastecimento de gasolina", "Abastecimento de álcool", "Abastecimento de diesel",
                       "Troca de óleo", "Balanceamento de rodas", "Lavagem de carro", "Reparo de pneus"]

def menu_principal():
    gerenciamento_servicos = GerenciamentoServicos()

    while True:
        print("\nEscolha uma opção:")
        print("1. Agendar serviço")
        print("2. Registrar serviço prestado")
        print("3. Histórico de serviços por cliente")
        print("4. Sair")

        opcao = input("Digite o número correspondente: ")

        if opcao == "1":
            cliente = input("Digite o nome do cliente: ")
            print("Escolha um tipo de serviço:")
            for i, servico in enumerate(servicos_disponiveis, start=1):
                print(f"{i}. {servico}")
            servico_escolhido = int(input("Digite o número do serviço desejado: "))
            if 1 <= servico_escolhido <= len(servicos_disponiveis):
                servico = servicos_disponiveis[servico_escolhido - 1]
                gerenciamento_servicos.agendar_servico(cliente, servico)
                print(f"{servico} agendado com sucesso para {cliente}.")
            else:
                print("Opção inválida. Tente novamente.")
        elif opcao == "2":
            cliente = input("Digite o nome do cliente: ")
            print("Escolha um tipo de serviço prestado:")
            for i, servico in enumerate(servicos_disponiveis, start=1):
                print(f"{i}. {servico}")
            servico_escolhido = int(input("Digite o número do serviço prestado: "))
            if 1 <= servico_escolhido <= len(servicos_disponiveis):
                servico = servicos_disponiveis[servico_escolhido - 1]
                detalhes = input("Digite os detalhes do serviço: ")
                gerenciamento_servicos.registrar_servico(cliente, servico, detalhes)
                print(f"{servico} registrado com sucesso para {cliente}.")
            else:
                print("Opção inválida. Tente novamente.")
        elif opcao == "3":
            cliente = input("Digite o nome do cliente: ")
            historico = gerenciamento_servicos.historico_servicos(cliente)
            if historico:
                print(f"Histórico de serviços para {cliente}:")
                for i, servico in enumerate(historico, start=1):
                    print(f"{i}. {servico}")
            else:
                print(f"Nenhum serviço encontrado para {cliente}")
        elif opcao == "4":
            print("A EcoEnergy agradece a prefêrencia, Volte Sempre!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
