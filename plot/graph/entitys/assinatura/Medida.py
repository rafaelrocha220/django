from graph.entitys.Helper import Helper

class Medida:
     
    def __init__(self, labels):
        self.medidas = []
        self.labels = labels
        self.helper = Helper()
        
        
    def assinaturas_medidas(self):
        self.total_faturado()
        self.avg_faturamento_ano()
        self.qtd_total_vendidos()
        self.avg_qtd_vendas_ano()
        return self.medidas # Return array sizes
    
    
    def append_medidas(self, title, total):
        self.medidas.append({'title': title, 'total': total })
        
        
    # Medidas
    def total_faturado(self):
        title = 'Faturamento bruto'
        total = self.helper.moeda( sum(self.labels['faturamento']) )
        self.append_medidas(title, total)
        
        
    def avg_faturamento_ano(self):
        title = 'Média fat. ano'
        total = self.helper.moeda(sum(self.labels['faturamento']) / len(self.labels['year']))
        self.append_medidas(title, total)
        
    
    def qtd_total_vendidos(self):
        title = 'Vendas totais'
        total = self.helper.quantidade(sum(self.labels['qtd']))
        self.append_medidas(title, total)
        
        
    def avg_qtd_vendas_ano(self):
        title = 'Média vendas ano'
        total = self.helper.quantidade(int(sum(self.labels['qtd']) / len(self.labels['year'])))
        self.append_medidas(title, total)
        
    




    
    