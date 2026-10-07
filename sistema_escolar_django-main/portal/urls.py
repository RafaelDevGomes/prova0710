from django.urls import path
from sistema import *
from portal import views

# ERRO ENCONTRADO: Problema na view tendo conflito entre views.py e urls.py onde tinha comandos de url em views e criar a def "cadastro_view".
# CORREÇÃO:        Adicionar "cadastro_view" na view.py e em cadastro_view.py.

urlpatterns = [
    path('index/', views.index),
    path('cadastro/', views.cadastro_view),
]
