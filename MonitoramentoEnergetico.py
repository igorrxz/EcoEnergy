class MonitoramentoEnergetico:
    def __init__(self):
        self.energia_solar_gerada = 0
        self.alertas = []

    def adicionar_energia_solar(self, quantidade_energia):
        self.energia_solar_gerada += quantidade_energia

    def analisar_desempenho_energia_solar(self):
        if self.energia_solar_gerada > 0:
            eficiencia = self.energia_solar_gerada / 1000  # Exemplo: 1 kW gera 1000 kWh
            economia = eficiencia * 0.75  # Exemplo: Economia de 75% usando energia solar
            return f"Energia solar gerada: {self.energia_solar_gerada} kWh\nEficiência: {eficiencia:.2f} kW\nEconomia estimada: R$ {economia:.2f}"
        else:
            return "Nenhuma energia solar gerada."

    def alerta_baixa_geracao_solar(self):
        if self.energia_solar_gerada < 500:  # Exemplo: Alerta se a geração solar for inferior a 500 kWh
            self.alertas.append("Baixa geração de energia solar.")
        return self.alertas
