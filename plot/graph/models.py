from django.db import models

# Create your models here.
class Pedido(models.Model):
    
    def get_pedidos(self, query=""):
        
        # Select query
        query = """ 
                    SELECT id, COUNT(id) as qtd, SUM(total) as faturamento, YEAR(created_at) as year 
                    FROM assinaturas_faturas
                    WHERE status NOT IN(1,4)
                    AND total < 300
                    GROUP BY year
                    ORDER BY year  
                    LIMIT 5
                """
        
        return Pedido.objects.raw(query)
        

