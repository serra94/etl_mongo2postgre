
## Ferramentas:
- Gerenciador de ambiente
  - [poetry](https://python-poetry.org/)
  - [hatch](https://hatch.pypa.io/latest/)
- Execução de tarefas
  - [taskipy](https://github.com/taskipy/taskipy)
- Testes
  - [pytest](https://docs.pytest.org/en/7.4.x/)
- Formatação de código
  - Remover variávies não utilizadas: [autoflake](https://github.com/PyCQA/autoflake)
  - Formatar o código: [blue](https://blue.readthedocs.io/en/latest/)
  - Ordenar importações: [isort](https://pycqa.github.io/isort/index.html)
- Desenvolvimento de cli's
  - [click](https://click.palletsprojects.com/en/8.1.x/)
  - [typer](https://typer.tiangolo.com/)
- Agendador de tarefas
  - [schedule](https://schedule.readthedocs.io/en/stable/)
  - [python-crontab](https://gitlab.com/doctormo/python-crontab/)
  - [celery](https://typer.tiangolo.com/)
- Banco de dados
  - Orm relacional: [sqlAlchemy](https://www.sqlalchemy.org/)
  - Orm para mongodb: [pymongo](https://pymongo.readthedocs.io/en/stable/)
  - Gerenciador de migrações: [alembic](https://alembic.sqlalchemy.org/en/latest/)
- Servidor wsgi
  - [gunicorn](https://gunicorn.org/)

## Estrutura de pastas e arquivos
```
|- assets
|- docs
|- app
    |- __init__.py
    |- .env
    |- app.py
    |- config.py
|- tests
    |- __init__.py
|- var
|- .editorconfig
|- .gitignore
|- docker-compose.yml
|- pyproject.toml
|- README.md
```

## Configurando o ambiente
Instalar dependências necessárias
```shell
pip install poetry

# Os próximos passos devem ser executados dentro do diretório do projeto

# ativar o ambiente
poetry shell

# configura o diretório .venv na raiz do projeto
# este diretório armazenará as dependências externas
poetry config virtualenvs.in-project true

# Instalar demais bibliotecas
poetry add --group dev blue
poetry add --group dev isort
poetry add --group dev taskipy
poetry add --group dev autoflake
```

Configurar isort
```yml
# Alterar o arquivo pyproject.toml e adicionar a configuração abaixo
[tool.isort]
profile = "black"
line_length = 79
```

Configurar taskipy
```yml
# Alterar o arquivo pyproject.toml e adicionar a configuração abaixo
[tool.taskipy.tasks]
lint = "autoflake --in-place --exclude=*/migrations/* --remove-all-unused-imports -r . && blue . && isort ."
```
