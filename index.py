usuario = 'Raquel'
empresas = ['Kinross', 'PCG']
qnt_empresas = len(empresas)
mes = 'Maio'


print(f"Olá,{usuario}!")
print(f"Você possui {qnt_empresas} para verificar este mês de {mes}")

#Empresa, Data Inicio, Data Fim, Orçamento líquido, Orçamento Usado.  
class Campanha:
    def __init__(self, empresa, tipo, plataforma, mes, data_inicio, data_fim, orcamento_liquido, orcamento_usado):
        self.empresa = empresa
        self.tipo = tipo
        self.plataforma = plataforma
        self.mes = mes
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.orcamento_liquido = orcamento_liquido
        self.orcamento_usado = orcamento_usado
    pass

dia_das_maes = Campanha('PCG', 'Alcance', 'Meta', 'Maio','01/05', '10/05', 3000.00, 2046.82)

print(dia_das_maes.mes)
