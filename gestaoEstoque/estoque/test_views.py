import logging
from django.test import TestCase, Client
from django.urls import reverse
from .models import Produto

# Configuração básica do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestEstoqueApp(TestCase):
    def setUp(self):
        """
        Configuração inicial para os testes.
        """
        self.client = Client()
        logger.info("Configuração inicial concluída.")

    def test_pagina_inicial(self):
        """
        Testa se a página inicial carrega corretamente.
        """
        logger.info("Iniciando teste para a página inicial.")
        response = self.client.get(reverse('pagina_inicial'))
        logger.info(f"Status da resposta: {response.status_code}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'estoque/pagina_inicial.html')
        logger.info("Teste para a página inicial concluído com sucesso.")

    def test_adicionar_produto(self):
        """
        Testa a funcionalidade de adicionar um novo produto.
        """
        logger.info("Iniciando teste para adicionar produto.")
        data = {'nome': 'Produto Teste', 'quantidade': 10, 'preco': 100.50}
        response = self.client.post(reverse('adicionar_produto'), data)
        logger.info(f"Status da resposta ao adicionar produto: {response.status_code}")
        self.assertEqual(response.status_code, 302)  # Sucesso redireciona
        logger.info("Teste para adicionar produto concluído com sucesso.")

    def test_buscar_produto(self):
        """
        Testa a funcionalidade de buscar um produto pelo nome.
        """
        logger.info("Iniciando teste para buscar produto.")
        # Cadastra o produto no banco de testes
        produto = Produto.objects.create(nome='Produto Buscar', quantidade=5, preco=30.00)
        logger.info(f"Produto criado para teste: {produto}")

        # Faz uma requisição GET para buscar o produto
        response = self.client.get(reverse('buscar_produto'), {'nome': 'Produto Buscar'})
        logger.info(f"Status da resposta ao buscar produto: {response.status_code}")

        # Verifica o status da resposta
        self.assertEqual(response.status_code, 200)

        # Confirma que o produto aparece na resposta
        self.assertContains(response, 'Produto Buscar')
        logger.info("Teste para buscar produto concluído com sucesso.")

    def test_atualizar_produto(self):
        """
        Testa a funcionalidade de atualizar um produto existente.
        """
        logger.info("Iniciando teste para atualizar produto.")
        # Cadastra um produto
        produto = Produto.objects.create(nome='Produto Atualizar', quantidade=5, preco=50.00)
        logger.info(f"Produto criado para atualização: {produto}")

        # Atualiza o produto
        response_update = self.client.post(reverse('atualizar_produto', args=[produto.id]), {
            'nome': 'Produto Atualizado',
            'quantidade': 20,
            'preco': 75.00
        })
        logger.info(f"Status da resposta ao atualizar produto: {response_update.status_code}")
        self.assertEqual(response_update.status_code, 302)  # Sucesso redireciona

        # Verifica se as alterações foram aplicadas
        produto_atualizado = Produto.objects.get(id=produto.id)
        logger.info(f"Produto atualizado: {produto_atualizado}")
        self.assertEqual(produto_atualizado.nome, 'Produto Atualizado')
        self.assertEqual(produto_atualizado.quantidade, 20)
        self.assertEqual(produto_atualizado.preco, 75.00)
        logger.info("Teste para atualizar produto concluído com sucesso.")

    def test_listar_produtos(self):
        """
        Testa a funcionalidade de listar todos os produtos.
        """
        logger.info("Iniciando teste para listar produtos.")
        # Cadastra dois produtos
        Produto.objects.create(nome='Produto 1', quantidade=5, preco=10.00)
        Produto.objects.create(nome='Produto 2', quantidade=8, preco=20.00)
        logger.info("Produtos criados para listagem.")

        # Lista os produtos
        response = self.client.get(reverse('listar_produtos'))
        logger.info(f"Status da resposta ao listar produtos: {response.status_code}")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Produto 1')
        self.assertContains(response, 'Produto 2')
        logger.info("Teste para listar produtos concluído com sucesso.")
