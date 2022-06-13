from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria', 'mostrar')
    # apresenta os nomes
    list_display_links = ('id', 'nome', 'sobrenome')
    # onde vai ter os links

    list_per_page = 5
    # qtd de contatos por página
    search_fields = ('nome', 'sobrenome', 'telefone')

    list_editable = ('telefone', 'mostrar')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)

