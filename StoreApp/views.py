from django.shortcuts import render
from StoreApp.models import Departamento, Produto
from StoreApp.forms import ContatoForm, ClienteForm
from django.core.mail import send_mail

# Create your views here.
def index(request):
    produtos_em_destaque = Produto.objects.filter(destaque = True)
    context = {
        'produtos' : produtos_em_destaque
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def cadastro(request):
    mensagem = ''
    #instanciar o form de cliente
    if request.method == "POST":
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            formulario = ClienteForm()
            mensagem = "Cliente cadastrado com sucesso :)"
        else:
            mensagem = "Verifique os erros abaixo:"
    else:
        formulario = ClienteForm()
    

    context = {
        'form_cliente' : formulario,
        'mensagem' : mensagem
    }

    return render(request, 'cadastro.html', context)

def contato(request):
    #Se o botão enviar for clicado.
    mensagem = ''

    if request.method == 'POST':
        #recuperando os dados do formulário
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        assunto = request.POST['assunto']
        mensagem = request.POST['mensagem']
        destinatario = ['antoniocoliver@usp.br']
        remetente = request.POST['email']
        corpo = f"Nome: {nome} \nTelefone: {telefone} \nMensagem: {mensagem}"
        
        try:
            #fazer o envio do e-mail
            send_mail(assunto, corpo, remetente, destinatario)
            mensagem = f"Mensagem enviada com sucesso para {destinatario} :)"
        except:
            mensagem = "Erro ao enviar a mensagem :("
    
        
    #criando uma instancia form de contato
    formulario = ContatoForm()

    context = {
        'form_contato' : formulario,
        'mensagem' : mensagem
    }
    return render(request, 'contato.html', context)

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
    produtos_relacionados = Produto.objects.filter(departamento_id = produto.departamento.id).exclude(id = id)[:4]
    context = {
        'produto' : produto,
        'produtos_relacionados' : produtos_relacionados
    }

    return render(request, 'produto_detalhes.html', context)