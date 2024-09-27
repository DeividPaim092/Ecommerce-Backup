# isso serve para colocar o que o usuário pode ver?
from django.http import HttpResponse
from multiprocessing import context
from django.shortcuts import render
from .forms import ProdutosModelForm
from core.forms import ProdutosModelForm
from django.contrib import messages
from core.models import Produto

# Create your views here.


def index(request):
    return render(request, 'index.html')


def contato(request):
    return render(request, 'contato.html')


def produto(request):
    if request.method == 'POST':
        # se esse request.metodo for igual a post, então formulário
        form = ProdutosModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Produto Salvo com sucesso ')
            return HttpResponse('produto salvo com sucesso')
        else:
            messages.error(request, 'Os dados não foram enviados')
    else:
        form = ProdutosModelForm()
    context = {
        'form': form

    }
    return render(request, 'produto.html', context)
