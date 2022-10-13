# Libs
from unittest import result
from django.shortcuts import render

# Models
from .models import Assinatura
    
# Create your views here.
def dashboard(req):
    return render(req, 'dashboard.html')
    
# Assinaturas
def assinaturas(req):
    
    inputs = req.GET.dict() or False
    assinatura = Assinatura(inputs)
    graficos, medidas, resultados, filtros = assinatura.main()
    
    return render(req, 'assinaturas/index.html', {
        'resultados': resultados,
        'filtros'   : filtros,
        'medidas'   : medidas,
        'graficos'  : graficos,
    })
    


    
