from django.contrib import admin
from django.urls import path, include
from estoque import views  # Importando a view para a página inicial

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_inicial, name='pagina_inicial'),  # Definindo a URL raiz para a página inicial do estoque
    path('estoque/', include('estoque.urls')),  # Incluindo as URLs do app estoque
]
