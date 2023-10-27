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
    
"""
__init__(self): O construtor da classe inicializa dois atributos:

energia_solar_gerada: Inicializado com 0, rastreia a quantidade total de energia solar gerada.
alertas: Uma lista vazia para rastrear alertas relacionados à geração de energia solar.

adicionar_energia_solar(self, quantidade_energia): Este método permite adicionar a quantidade de energia solar gerada ao atributo energia_solar_gerada. 
Ele simplesmente atualiza o total de energia gerada.

analisar_desempenho_energia_solar(self): Este método calcula e retorna informações sobre o desempenho da energia solar gerada. 
Se a quantidade de energia solar gerada for maior que zero, ele realiza o seguinte cálculo:

Calcula a eficiência da geração de energia solar em quilowatts (kW). Lembre-se de que 1 kW equivale a 1000 kWh.
Calcula a economia estimada com base na eficiência. O exemplo mostra uma economia de 75%, mas você pode personalizar essa porcentagem.
Retorna uma string formatada com informações sobre a energia solar gerada, a eficiência em kW e a economia estimada em reais.

alerta_baixa_geracao_solar(self): Este método verifica se a quantidade de energia solar gerada é inferior a um valor específico (500 kWh, de acordo com o exemplo). 
Se a geração for inferior a esse valor, ele adiciona um alerta à lista de alertas. Em seguida, ele retorna a lista de alertas. 
Isso permite que o sistema rastreie se a geração de energia solar está abaixo do limite especificado.
"""