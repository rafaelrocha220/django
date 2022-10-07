from django.db import models

# Create your models here.
class Pedido(models.Model):
    
    def get_pedidos(self, query=""):
        
        # Select query
        query += "SELECT id, COUNT(id) as qtd, SUM(total) as faturamento, YEAR(created_at) as year FROM assinaturas_faturas"
        
        # Filter query
        query += " WHERE status NOT IN(1,4)"
        
        # And filter
        query += " AND total < 300"
        
        # Group query
        query += " GROUP BY year"
        
        # Order query
        query += " ORDER BY year"
        
        # Limit query
        # query += " LIMIT 5"
        
        return Pedido.objects.raw(query)
        

