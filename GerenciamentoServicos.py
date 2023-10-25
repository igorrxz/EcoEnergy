class GerenciamentoServicos:
    def __init__(self):

        self.servicos_agendados = {}

    def agendar_servico(self, cliente, servico):
        
        
        if cliente not in self.servicos_agendados:
            self.servicos_agendados[cliente] = []
        self.servicos_agendados[cliente].append(servico)

    def registrar_servico(self, cliente, servico, detalhes):
        
        pass

    def historico_servicos(self, cliente):
        
        if cliente in self.servicos_agendados:
            return self.servicos_agendados[cliente]
        else:
            return []