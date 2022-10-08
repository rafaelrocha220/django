from django.contrib import admin
from django.urls import path

from graph.views import *

urlpatterns = [
    # Dashboard index
    path('', dashboard, name='dashobard'),
    
    # Dimensão
    path('dimensao/pedidos', pedidos, name='pedidos'),

    # Default
    path('admin/', admin.site.urls),
]
