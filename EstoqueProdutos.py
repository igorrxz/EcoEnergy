class EstoqueProdutos:
    def __init__(self):
        self.estoque = {
            "gasolina": 1000,
            "alcool": 800,
            "diesel": 500,
            "energia_solar": 100
        }
        self.limite_minimo = {
            "gasolina": 100,
            "alcool": 80,
            "diesel": 50,
            "energia_solar": 10
        }

    def receber_produtos(self, produto, quantidade):
        if produto in self.estoque:
            self.estoque[produto] += quantidade

    def atualizar_estoque_apos_venda(self, produto, quantidade_vendida):
        if produto in self.estoque and self.estoque[produto] >= quantidade_vendida:
            self.estoque[produto] -= quantidade_vendida
        else:
            print(f"Não há estoque suficiente de {produto} para esta venda.")

    def emitir_alertas_estoque_baixo(self):
        alertas = []
        for produto, quantidade in self.estoque.items():
            if quantidade < self.limite_minimo[produto]:
                alertas.append(f"Estoque baixo de {produto}.")
        return alertas

    def reordenar_estoque(self):
        for produto, quantidade in self.estoque.items():
            if quantidade < self.limite_minimo[produto]:
                quantidade_faltante = self.limite_minimo[produto] - quantidade
                self.receber_produtos(produto, quantidade_faltante)

    def vender_produtos(self, produto, quantidade):
        if produto in self.estoque and self.estoque[produto] >= quantidade:
            self.estoque[produto] -= quantidade
            print(f"{quantidade} unidades de {produto} vendidas com sucesso.")
        else:
            print(f"Não há estoque suficiente de {produto} para esta venda.")

    def mostrar_situacao_estoque(self):
        print("Situação atual do estoque:")
        for produto, quantidade in self.estoque.items():
            print(f"{produto}: {quantidade} unidades")



"""
Esse código define a classe EstoqueProdutos, que é responsável por gerenciar o estoque de produtos em um posto de gasolina ou mercearia. 
Vamos explicar as partes principais desse código:

__init__(self): O método __init__ é o construtor da classe e é chamado quando um objeto da classe é criado. Nesse caso, ele inicializa dois dicionários:

estoque: Mapeia os tipos de produtos (gasolina, álcool, diesel, energia solar) para suas quantidades em estoque.
limite_minimo: Define a quantidade mínima desejada em estoque para cada tipo de produto.

receber_produtos(self, produto, quantidade): Este método permite receber produtos e atualizar o estoque. 
Ele verifica se o produto está no dicionário de estoque e, se estiver, adiciona a quantidade recebida ao estoque existente.

atualizar_estoque_apos_venda(self, produto, quantidade_vendida): Esse método atualiza o estoque após uma venda. 
Ele verifica se o produto está no estoque e se a quantidade vendida não excede a quantidade em estoque. 
Em caso afirmativo, a quantidade vendida é subtraída do estoque.

emitir_alertas_estoque_baixo(self): Este método verifica se o estoque de qualquer produto caiu abaixo do limite mínimo definido. 
Se sim, ele emite alertas para os produtos que estão com estoque baixo.

reordenar_estoque(self): Esse método verifica se o estoque de algum produto está abaixo do limite mínimo e, se estiver, 
encomenda produtos adicionais para reabastecer o estoque até o limite mínimo.

vender_produtos(self, produto, quantidade): Este método permite vender produtos e atualiza o estoque após uma venda bem-sucedida. 
Ele verifica se o produto está no estoque e se a quantidade vendida não excede a quantidade em estoque.

mostrar_situacao_estoque(self): Esse método exibe a situação atual do estoque, mostrando a quantidade de cada tipo de produto em estoque.

Em resumo, a classe EstoqueProdutos oferece métodos para receber, vender, atualizar e monitorar o estoque de produtos, 
bem como emitir alertas quando o estoque de um produto está baixo. 
Essa classe é essencial para o gerenciamento de produtos em um posto de gasolina ou mercearia.
"""