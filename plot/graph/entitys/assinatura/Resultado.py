from .Query import *
from django.db import models

class Resultado(models.Model):
    
    def get_resultados(self, inputs):
        query = Query.query_assinaturas(inputs)
        return Resultado.objects.raw(query)
        
    def labels(self, resultados):
        return {
            'year'       : [row.year for row in resultados],
            'faturamento': [int(row.faturamento) for row in resultados],
            'qtd'        : [row.qtd for row in resultados]
        }
    
    def filtros(self, resultados): 
        return [
            {
                'label'  : 'tipo assinatura',
                'name'  : 'tipo',
                'options': [
                    {'label':'mensal', 'value': 286},
                    {'label':'semestral', 'value': 1716},
                    {'label':'anual', 'value': 3432},
                ]
            },
            {
                'label'  : 'status pagamento',
                'name'  : 'status',
                'options': [
                    {'label':'aprovados', 'value': 2},
                    {'label':'cancelados', 'value': 4},
                ]
            },
            
            {
                'label'  : 'periodo anual',
                'name'  : 'periodo',
                'options': [
                    {'label':'2017', 'value': 2017},
                    {'label':'2018', 'value': 2018},
                    {'label':'2018', 'value': 2019},
                    {'label':'2018', 'value': 2020},
                    {'label':'2018', 'value': 2021},
                    {'label':'2018', 'value': 2022},
                ]
            },
        ]
       