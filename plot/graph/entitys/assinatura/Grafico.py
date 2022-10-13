class Grafico:
    
    def __init__(self, labels):
        self.graficos = []
        self.labels = labels
        
    
    def assinaturas_graficos(self): 
        self.assinatura_sum()
        self.assinatura_count()
        
        return self.graficos
    
        
    def assinatura_sum(self): 
        self.graficos.append({
            'title' : 'Faturamento bruto ao ano (R$)',
            'type'  : 'bar',
            'chart' : 'fat_bruto',
            'labels': self.labels['year'],
            'data'  : self.labels['faturamento']
        })
       
    
    def assinatura_count(self): 
        self.graficos.append({
            'title' : 'Total assinaturas vendidas ao ano (qtd)',
            'chart' : 'total_vendas',
            'type'  : 'bar',
            'labels': self.labels['year'],
            'data'  : self.labels['qtd']
        })
     