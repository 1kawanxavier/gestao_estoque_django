from django.urls import path
from . import views

urlpatterns = [
    path("", views.pagina_inicial, name="pagina_inicial"),  # Página inicial
    path("adicionar/", views.adicionar_produto, name="adicionar_produto"),
    path("listar/", views.listar_produtos, name="listar_produtos"),
    path("buscar/", views.buscar_produto, name="buscar_produto"),
    path("atualizar/<int:produto_id>/", views.atualizar_produto, name="atualizar_produto"),
    path("remover/<int:produto_id>/", views.remover_produto, name="remover_produto"),
]
