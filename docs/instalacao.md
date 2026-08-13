# Instalação e Execução

## Requisitos

- Python 3.11+
- Poetry
- PostgreSQL configurado e acessível
- Arquivos CSV de entrada no diretório de dados

## Clonando o projeto

```bash
git clone <url-do-repositorio>
cd medicinal
```

## Criando o ambiente virtual

```bash
poetry install
```

## Configurando variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com as variáveis necessárias, por exemplo:

```env
DATABASE_URL=postgresql://usuario:senha@host:5432/nome_do_banco
APP_ENV=dev
LOG_LEVEL=INFO
SCHEMA_BRONZE=bronze
SCHEMA_SILVER=silver
SCHEMA_GOLD=gold
RAW_DATA_DIR=data/raw
```

## Executando a pipeline

```bash
poetry run medicinal
```

Se quiser limpar os schemas antes de recriar todo o pipeline:

```bash
poetry run medicinal --reset
```

## Executando o reset do banco

```bash
poetry run python -m medicinal.reset_db
```

## Rodando testes

```bash
poetry run task tests
```

## Rodando a documentação

```bash
poetry run mkdocs serve
```

A documentação será servida localmente e pode ser acessada em:

```text
http://127.0.0.1:8000
```
