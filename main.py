from GerenciamentoServicos import GerenciamentoServicos

def menu_principal():
    gerenciamento_servicos = GerenciamentoServicos()

    while True:
        print("Escolha uma opção:")
        print("1. Agendar serviço")
        print("2. Registrar serviço prestado")
        print("3. Histórico de serviços por cliente")
        print("4. Voltar ao menu principal")

        opcao = input("Digite o número correspondente: ")

        if opcao == "1":
            cliente = input("Digite o nome do cliente: ")
            servico = input("Digite o tipo de serviço: ")
            gerenciamento_servicos.agendar_servico(cliente, servico)
            print("Serviço agendado com sucesso.")
        elif opcao == "2":
            cliente = input("Digite o nome do cliente: ")
            servico = input("Digite o serviço prestado: ")
            detalhes = input("Digite os detalhes do serviço: ")
            gerenciamento_servicos.registrar_servico(cliente, servico, detalhes)
            print("Serviço registrado com sucesso.")
        elif opcao == "3":
            cliente = input("Digite o nome do cliente: ")
            historico = gerenciamento_servicos.historico_servicos(cliente)
            if historico:
                print("Histórico de serviços para", cliente, ":")
                for i, servico in enumerate(historico, start=1):
                    print(f"{i}. {servico}")
            else:
                print("Nenhum serviço encontrado para", cliente)
        elif opcao == "4":
            print("Retornando ao menu principal.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()