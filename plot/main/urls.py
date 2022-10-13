from django.contrib import admin
from django.urls import path

from graph.views import *

urlpatterns = [
    # Dashboard index
    path('', dashboard, name='dashobard'),
    
    # Dimensão assinaturas
    path('assinaturas/aprovadas', assinaturas, name='assinaturas'),
    
    # Default
    path('admin/', admin.site.urls),
]
