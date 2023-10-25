class GerenciamentoServicos:
    def __init__(self):
        # Inicialize variáveis ou estruturas de dados para gerenciar serviços.
        self.servicos_agendados = {}

    def agendar_servico(self, cliente, servico):
        # Simplesmente registra o agendamento neste exemplo.
        if cliente not in self.servicos_agendados:
            self.servicos_agendados[cliente] = []
        self.servicos_agendados[cliente].append(servico)

    def registrar_servico(self, cliente, servico, detalhes):
        # Implemente a lógica para registrar detalhadamente cada serviço prestado.
        pass

    def historico_servicos(self, cliente):
        # Retorna o histórico de serviços para um cliente.
        if cliente in self.servicos_agendados:
            return self.servicos_agendados[cliente]
        else:
            return []