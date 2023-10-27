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

"""
__init__(self): O método __init__ é o construtor da classe e é chamado quando um objeto da classe é criado. Neste caso, ele inicializa dois dicionários:

estoque_mercearia: Mapeia o nome dos produtos para um dicionário com a quantidade e detalhes do produto.
alertas_reposicao: Inicialmente vazio, este dicionário será usado para rastrear produtos que precisam ser repostos.

adicionar_produto(self, nome, quantidade, detalhes): Este método permite adicionar produtos ao estoque da mercearia. 
Ele verifica se o produto já está no estoque. Se o produto não estiver no estoque, um novo registro é criado. 
Se já estiver no estoque, a quantidade do produto é atualizada.

registrar_venda(self, nome, quantidade): Esse método permite registrar uma venda e atualizar o estoque após uma venda bem-sucedida. 
Ele verifica se o produto está no estoque e se a quantidade vendida não excede a quantidade disponível. 
Se as condições forem atendidas, a quantidade vendida é subtraída do estoque.

analisar_desempenho_produto(self, nome): Este método permite analisar o desempenho de um produto específico. 
Ele verifica se o produto está no estoque e, se estiver, imprime os detalhes do produto.

emitir_alertas_reposicao(self): Este método verifica o estoque atual dos produtos e emite alertas de reposição para produtos que estão com estoque esgotado (quantidade igual a 0). 
Os produtos que precisam ser repostos são registrados no dicionário alertas_reposicao.

Em resumo, a classe GestaoMercearia é usada para gerenciar o estoque de produtos em uma mercearia. 
Ela oferece métodos para adicionar produtos, registrar vendas, analisar o desempenho de produtos e emitir alertas de reposição quando um produto está com estoque esgotado. 
Isso ajuda a manter o controle sobre o estoque e a garantir que os produtos estejam disponíveis quando necessário.
"""