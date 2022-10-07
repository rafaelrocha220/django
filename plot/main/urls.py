from django.contrib import admin
from django.urls import path

from graph.views import home

urlpatterns = [
    path('', home, name='index'),
    path('admin/', admin.site.urls),
]
