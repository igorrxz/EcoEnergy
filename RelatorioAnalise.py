import datetime
from datetime import datetime, timedelta

class RelatorioAnalise:
    def __init__(self):
        self.vendas = []  # Lista de vendas (data, produto, quantidade, preço, cliente)
        self.servicos = []  # Lista de serviços (data, tipo de serviço, cliente, detalhes)
        self.energia_solar = []  # Lista de geração de energia solar (data, quantidade em kWh)

    def adicionar_venda(self, produto, quantidade, preco, cliente):
        data = (datetime.now(), produto, quantidade, preco, cliente)
        self.vendas.append(data)

    def adicionar_servico(self, tipo_servico, cliente, detalhes):
        data = (datetime.now(), tipo_servico, cliente, detalhes)
        self.servicos.append(data)

    def adicionar_energia_solar(self, quantidade):
        data = (datetime.now(), quantidade)
        self.energia_solar.append(data)

    def gerar_relatorio_vendas(self, periodo):
        data_atual = datetime.now()
        data_inicial = None

        if periodo == "diario":
            data_inicial = data_atual - timedelta(days=1)
        elif periodo == "semanal":
            data_inicial = data_atual - timedelta(weeks=1)
        elif periodo == "mensal":
            data_inicial = data_atual - timedelta(days=data_atual.day - 1)
        else:
            return "Período inválido. Escolha entre 'diario', 'semanal' ou 'mensal'."

        vendas_periodo = [v for v in self.vendas if data_inicial <= v[0] <= data_atual]

        return vendas_periodo

    def gerar_relatorio_servicos(self, periodo):
        data_atual = datetime.now()
        data_inicial = None

        if periodo == "diario":
            data_inicial = data_atual - timedelta(days=1)
        elif periodo == "semanal":
            data_inicial = data_atual - timedelta(weeks=1)
        elif periodo == "mensal":
            data_inicial = data_atual - timedelta(days=data_atual.day - 1)
        else:
            return "Período inválido. Escolha entre 'diario', 'semanal' ou 'mensal'."

        servicos_periodo = [s for s in self.servicos if data_inicial <= s[0] <= data_atual]

        return servicos_periodo

    def gerar_relatorio_energia_solar(self, periodo):
        data_atual = datetime.now()
        data_inicial = None

        if periodo == "diario":
            data_inicial = data_atual - timedelta(days=1)
        elif periodo == "semanal":
            data_inicial = data_atual - timedelta(weeks=1)
        elif periodo == "mensal":
            data_inicial = data_atual - timedelta(days=data_atual.day - 1)
        else:
            return "Período inválido. Escolha entre 'diario', 'semanal' ou 'mensal'."

        energia_solar_periodo = [e for e in self.energia_solar if data_inicial <= e[0] <= data_atual]

        return energia_solar_periodo
    
"""
Esta classe é responsável por gerar relatórios e análises de vendas, serviços e geração de energia solar. Aqui estão os principais pontos do código:

__init__(self): O construtor da classe inicializa três listas vazias: vendas, servicos e energia_solar, que são usadas para armazenar informações sobre vendas, 
serviços e geração de energia solar.

Métodos para adicionar dados:

adicionar_venda(self, produto, quantidade, preco, cliente): Este método registra uma venda na lista de vendas, incluindo a data e os detalhes da venda.

adicionar_servico(self, tipo_servico, cliente, detalhes): Registra um serviço na lista de serviços, incluindo a data e informações sobre o serviço.

adicionar_energia_solar(self, quantidade): Registra a geração de energia solar na lista de energia solar, incluindo a data e a quantidade em kWh.

Métodos para gerar relatórios:

gerar_relatorio_vendas(self, periodo): Este método gera um relatório de vendas com base no período especificado. 
Ele filtra as vendas dentro do período desejado e retorna uma lista de vendas no formato (data, produto, quantidade, preço, cliente).

gerar_relatorio_servicos(self, periodo): Gera um relatório de serviços com base no período especificado. 
Ele filtra os serviços dentro do período desejado e retorna uma lista de serviços no formato (data, tipo de serviço, cliente, detalhes).

gerar_relatorio_energia_solar(self, periodo): Gera um relatório de geração de energia solar com base no período especificado. 
Ele filtra a geração de energia solar dentro do período desejado e retorna uma lista no formato (data, quantidade em kWh).

Resumo: A classe RelatorioAnalise permite adicionar e rastrear vendas, serviços e geração de energia solar. 
Além disso, ela oferece a capacidade de gerar relatórios com base em diferentes períodos. 
Isso é útil para análise de desempenho e tomada de decisões em relação aos negócios. 
Cada relatório fornece informações detalhadas sobre os eventos registrados no período especificado.
"""