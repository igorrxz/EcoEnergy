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
