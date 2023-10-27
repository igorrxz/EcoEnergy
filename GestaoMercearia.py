class GestaoMercearia:
    def __init__(self):
        self.estoque_mercearia = {}  # Dicionário para acompanhar o estoque de produtos
        self.alertas_reposicao = {}  # Dicionário para alertas de reposição

    def adicionar_produto(self, nome, quantidade, detalhes):
        if nome not in self.estoque_mercearia:
            self.estoque_mercearia[nome] = {'quantidade': quantidade, 'detalhes': detalhes}
        else:
            self.estoque_mercearia[nome]['quantidade'] += quantidade

    def registrar_venda(self, nome, quantidade):
        if nome in self.estoque_mercearia and self.estoque_mercearia[nome]['quantidade'] >= quantidade:
            self.estoque_mercearia[nome]['quantidade'] -= quantidade
        else:
            print(f"Não há estoque suficiente de {nome} para esta venda.")

    def analisar_desempenho_produto(self, nome):
        if nome in self.estoque_mercearia:
            detalhes = self.estoque_mercearia[nome]['detalhes']
            print(f"Detalhes do produto {nome}: {detalhes}")

    def emitir_alertas_reposicao(self):
        for nome, quantidade in self.estoque_mercearia.items():
            if quantidade['quantidade'] == 0:
                self.alertas_reposicao[nome] = "Repor estoque"
