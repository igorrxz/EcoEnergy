class GerenciamentoServicos:
    def __init__(self):
        self.servicos_agendados = {}

    def agendar_servico(self, cliente, servico):
        if cliente not in self.servicos_agendados:
            self.servicos_agendados[cliente] = []
        self.servicos_agendados[cliente].append(servico)

    def registrar_servico(self, cliente, servico, detalhes):
        if cliente in self.servicos_agendados:
            self.servicos_agendados[cliente].append(f"Serviço Prestado: {servico}, Detalhes: {detalhes}")

    def historico_servicos(self, cliente):
        if cliente in self.servicos_agendados:
            return self.servicos_agendados[cliente]
        else:
            return []
        

"""
Esse código define uma classe chamada GerenciamentoServicos, que é responsável por gerenciar os serviços agendados para os clientes em uma mercearia ou posto de gasolina. 
Vamos analisar as principais partes desse código:

__init__(self): O método __init__ é o construtor da classe e é chamado quando um objeto da classe é criado. 
Nesse caso, ele inicializa um atributo servicos_agendados como um dicionário vazio. Esse dicionário será usado para mapear clientes aos serviços agendados para eles.

agendar_servico(self, cliente, servico): Este método permite agendar um serviço para um cliente específico. 
Ele verifica se o cliente já possui serviços agendados e, se não, cria uma lista vazia para esse cliente. 
Em seguida, adiciona o serviço agendado à lista de serviços do cliente.

registrar_servico(self, cliente, servico, detalhes): Este método permite registrar um serviço prestado para um cliente, juntamente com detalhes adicionais. 
Ele verifica se o cliente já tem serviços agendados. Se sim, adiciona uma entrada na lista de serviços do cliente com informações sobre o serviço prestado e os detalhes fornecidos.

historico_servicos(self, cliente): Esse método retorna o histórico de serviços para um cliente específico. 
Ele verifica se o cliente possui serviços agendados no dicionário servicos_agendados. 
Se sim, retorna a lista de serviços para esse cliente; caso contrário, retorna uma lista vazia.

Em resumo, essa classe GerenciamentoServicos permite agendar, registrar e recuperar o histórico de serviços para os clientes, 
fornecendo um sistema de gerenciamento simples para serviços em um posto de gasolina ou mercearia
"""