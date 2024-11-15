# gestao_estoque_django


Gestão de Estoque Django
Sobre o Projeto

Este é um sistema de gestão de estoque desenvolvido com o framework Django. Ele inclui funcionalidades para adicionar, buscar, listar, atualizar e remover produtos.
Pré-requisitos

Certifique-se de que você tem as seguintes ferramentas instaladas:

    Python (3.8 ou superior)
    Pip (gerenciador de pacotes do Python)
    Virtualenv (opcional, mas recomendado)

Configuração do Ambiente

    Clone este repositório

    Crie e ative um ambiente virtual:

python -m venv myenv  # Cria o ambiente virtual
source myenv/bin/activate  # Ativação no Linux/macOS
myenv\Scripts\activate     # Ativação no Windows


Executando o Projeto

    Aplique as migrações do banco de dados:

python manage.py makemigrations
python manage.py migrate

Inicie o servidor de desenvolvimento:

python manage.py runserver

Acesse o sistema:

    Abra o navegador e acesse: http://127.0.0.1:8000.



# Executando os Testes

    Certifique-se de que o ambiente virtual está ativado.

    Execute todos os testes:

    python manage.py test