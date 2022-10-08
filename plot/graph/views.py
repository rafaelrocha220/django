# Libs
from unittest import result
from django.shortcuts import render

# Models
from .models import Pedido

# Create your views here.

def dashboard(req):
    return render(req, 'dashboard.html')
    

def pedidos(req):
    
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