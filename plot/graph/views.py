from unittest import result
from django.shortcuts import render

from .models import Pedido

# Create your views here.
def home2(req):
    
    pedido = Pedido()
    resultados = pedido.get_pedidos_data()
    
    # Make graph
    labels = [row.year for row in resultados]
    data = [int(row.faturamento) for row in resultados]
    
    return render(req, 'data.html', {
        'labels': labels,
        'datas' : data
    })

def home(req):
    
    pedido = Pedido()
    resultados = pedido.get_pedidos_raw()
    resultados_data = pedido.get_pedidos_data()
    
    # Make graph
    labels = [row.year for row in resultados_data]
    data = [int(row.faturamento) for row in resultados_data]
    
    return render(req, 'raw.html', {
        'resultados': resultados,
        'labels'    : labels,
        'datas'     : data
    })