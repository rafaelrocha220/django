from django.db import models
from .querys import Pedidos_ORM

# Create your models here.
class Pedido(models.Model):
    
    def get_pedidos_data(self):
        # Select query
        query = Pedidos_ORM.get_pedidos_aprovados_data()
        return Pedido.objects.raw(query)
        
    def get_pedidos_raw(self):
        # Select query
        query = Pedidos_ORM.get_pedidos_aprovados_raw()
        return Pedido.objects.raw(query)
        

