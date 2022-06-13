from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


def index(request):

    contatos = Contato.objects.order_by('-id').filter(
        mostrar=True
    )
    # contacts order
    # if prefer to order by another field, use: objects.order_by ('field'), in decreasing order just put the signal "-"
    paginator = Paginator(contatos, 3)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def see_contact(request, contact_id):
    # contato = Contato.objects.get(id=contact_id)
    contato = get_object_or_404(Contato, id=contact_id)

    if not contato.mostrar:
        raise Http404

    return render(request, 'contatos/see_contact.html', {
        'contato': contato
    })


def busca(request):
    termo = request.GET.get('termo')
    campos = Concat('nome', Value(' '), 'sobrenome')

    if termo is None or not termo:
        messages.add_message(
            request,
            messages.ERROR,
            'Campo termo não pode ficar vazio.'
        )
        return redirect('index')

    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )

    paginator = Paginator(contatos, 3)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })
