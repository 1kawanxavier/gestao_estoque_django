
from django.shortcuts import render, redirect
from .models import Produto

# Sua implementação existente:
def adicionar_produto(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        quantidade = int(request.POST.get("quantidade"))
        preco = float(request.POST.get("preco"))
        Produto.objects.create(nome=nome, quantidade=quantidade, preco=preco)
        return redirect("listar_produtos")
    return render(request, "estoque/adicionar_produto.html")

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, "estoque/listar_produtos.html", {"produtos": produtos})

def buscar_produto(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        produtos = Produto.objects.filter(nome__icontains=nome)
        return render(request, "estoque/listar_produtos.html", {"produtos": produtos})
    return render(request, "estoque/buscar_produto.html")

def atualizar_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if request.method == "POST":
        produto.quantidade = int(request.POST.get("quantidade"))
        produto.save()
        return redirect("listar_produtos")
    return render(request, "estoque/atualizar_produto.html", {"produto": produto})

def remover_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    produto.delete()
    return redirect("listar_produtos")

# Nova view para a página inicial
def pagina_inicial(request):
    return render(request, "estoque/pagina_inicial.html")
