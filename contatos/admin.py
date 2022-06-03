from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria')
    # apresenta os nomes
    list_display_links = ('id', 'nome', 'sobrenome')
    # onde vai ter os links

    list_per_page = 5
    # qtd de contatos por página
    search_fields = ('nome', 'sobrenome', 'telefone')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)

