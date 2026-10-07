from django.shortcuts import render
from sistema import *
from django.http import HttpResponse

def index(request):
    return render(
        request,
        'templates/portal/index.html'
    )

# ERRO ENCONTRADO: Cadastro não estava setado como uma view nem como um variavel funcional.
# CORREÇÃO:        Settar cadastro_view em uma pagina de view, na url e no init.


def cadastro_view (request):
    print('Página cadastro funfou!')
    return HttpResponse('Página inicial do cadastro')
     

