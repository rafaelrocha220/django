from django.db import models

class Pedidos_ORM:
    
    def get_pedidos_aprovados_data():
    
        return """ 
            SELECT id, COUNT(id) as qtd, SUM(total) as faturamento, YEAR(created_at) as year 
            FROM assinaturas_faturas
            WHERE status NOT IN(1,4)
            AND total < 300
            GROUP BY year
            ORDER BY year  
        """
        
    def get_pedidos_aprovados_raw():
    
        return """ 
            SELECT *
            FROM assinaturas_faturas
            WHERE status NOT IN(1,4)
            LIMIT 20
        """
        

