from django.db import models
import locale

from graph.entitys.assinatura.Medida import Medida
from graph.entitys.assinatura.Resultado import Resultado
from graph.entitys.assinatura.Grafico import Grafico


# Create your models here.
class Assinatura(models.Model):
        
    def __init__(self, inputs):
        if(inputs != False):
            self.inputs = inputs
        else: 
            self.inputs = False
        
    def main(self):
    
        # Resultados
        resultado  = Resultado()
        resultados = resultado.get_resultados(self.inputs)
        labels     = resultado.labels(resultados)
        filtros    = resultado.filtros(resultados)
        
        # Graficos e medidas
        graficos   = Grafico(labels).assinaturas_graficos()
        medidas    = Medida(labels).assinaturas_medidas()
        
        return graficos, medidas, resultados, filtros
        
 
    



