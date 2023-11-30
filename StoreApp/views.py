from django.shortcuts import render
from StoreApp.models import Departamento, Produto

# Create your views here.
def index(request):
    produtos_em_destaque = Produto.objects.filter(destaque = True)
    context = {
        'produtos' : produtos_em_destaque
    }
    return render(request, 'index.html', context)

def produto_lista(request):
    #buscando produtos na lista
    produtos = Produto.objects.all()

    context = {
        'produtos' : produtos,
        'categoria' : 'Todos Produtos'
    }
    return render(request, 'produtos.html', context)


def produto_lista_por_id(request, id):
    #buscando produtos no banco filtrando por depto
    produtos = Produto.objects.filter(departamento_id = id) 
    #Buscando o depto no banco
    departamento = Departamento.objects.get(id = id)

    context = {
        'produtos' : produtos,
        'categoria' : departamento.nome
    }
    return render(request, 'produtos.html', context)

def produto_detalhe(request, id):
    produto = Produto.objects.get(id = id)
    context = {
        'produto' : produto
    }

    return render(request, 'produto_detalhes.html', context)

'''
def produto_lista(request):
    departamentos = Departamento.objects.all()
    context = {
        'departamentos' : departamentos
    }
    return render(request, 'produtos.html', context)

def produto_detalhe(request):
    departamentos = Departamento.objects.all()
    context = {
        'departamentos' : departamentos
    }
    return render(request, 'produto_detalhes.html', context)
'''