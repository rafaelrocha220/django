from django.db import models

class Query:
    
    def query_assinaturas(inputs):
        
        where = "" 
        # Tipo assinatura
        # [286,1716,3432]
        if(inputs != False and inputs.get('tipo')):
            where += " AND total = '{}'".format(str(inputs.get('tipo')))
            
        # Status pagamento
        if(inputs != False and inputs.get('status')):
            where += " AND status = '{}'".format(str(inputs.get('status')))
        
        # Ano
        if(inputs != False and inputs.get('periodo')):
            where += " AND YEAR(created_at) = '{}'".format(str(inputs.get('periodo')))
            
        # Periodo
    
        return """ 
            SELECT id, COUNT(id) as qtd, SUM(total) as faturamento, YEAR(created_at) as year 
            FROM assinaturas_faturas
            WHERE 1 
            {}
            GROUP BY year
            ORDER BY year  
        """.format(where)
  
        
   