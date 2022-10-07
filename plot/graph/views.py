from django.shortcuts import render

from .models import Pedido

# Create your views here.
def home(req):
    
    pedido = Pedido()
    resultados = pedido.get_pedidos()
    
    # Make graph
    labels = [row.year for row in resultados]
    data = [int(row.faturamento) for row in resultados]
    
    context = {'labels': labels, 'datas': data}
    
    return render(req, 'graph/index.html', context)