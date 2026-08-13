# Medicinal

![CI](https://github.com/your-user/medicinal/actions/workflows/ci.yml/badge.svg)

Projeto de estudo e simulação de pipeline de dados com Python, SQL e PostgreSQL, inspirado em dados clínicos sintéticos relacionados à COVID-19.

## Visão geral

Este repositório demonstra um pipeline simples de dados em camadas, seguindo o padrão bronze → silver → gold. A proposta é mostrar, de forma prática e didática, como:

- coletar dados em arquivos CSV;
- carregar esses dados em um banco relacional;
- aplicar limpeza e validações;
- transformar dados em modelos analíticos;
- executar consultas para extrair insights;
- automatizar testes e documentação do projeto.

O projeto utiliza dados sintéticos baseados em pacientes e historicos clínicos gerados pelo Synthea, que são muito úteis para simulações de saúde e dados de pacientes em ambiente acadêmico.

## Objetivo

- facilitar o entendimento de pipelines de dados em arquitetura em camadas;
- mostrar uso de Python para manipular dados estruturados;
- demonstrar armazenamento e consultas em SQL;
- servir como base para estudos de ETL, modelagem analítica e automação de processos.

## Stack tecnológica

- Python 3.11+
- Poetry
- PostgreSQL
- SQLAlchemy
- Pandas
- pytest + pytest-cov
- Black + Ruff
- Taskipy
- MkDocs Material

## Arquitetura do projeto

```text
dados brutos (CSV)
        ↓
    bronze
        ↓
    silver
        ↓
    gold
```

### Camada Bronze

- leitura dos arquivos CSV;
- padronização de colunas;
- armazenamento dos dados originais sem perda de contexto;
- inclusão de metadados de execução.

### Camada Silver

- validação de qualidade dos dados;
- limpeza e normalização;
- transformações aplicadas para padronização e consistência;
- preparação para uso analítico.

### Camada Gold

- agregações por paciente e encontro;
- resumos analíticos;
- tabelas prontas para consultas e relatórios.

## Estrutura do repositório

```text
medicinal/
├── .env
├── .gitignore
├── .python-version
├── README.md
├── mkdocs.yml
├── pyproject.toml
├── poetry.lock
├── notebooks/
├── sql/
│   ├── ddl/
│   └── queries/
├── src/
│   └── medicinal/
│       ├── __init__.py
│       ├── __main__.py
│       ├── main.py
│       ├── reset_db.py
│       ├── bronze/
│       ├── silver/
│       ├── gold/
│       ├── config/
│       └── utils/
├── tests/
│   └── unit/
├── docs/
└── .venv/
```

## Configuração do ambiente

O projeto usa Poetry para gerenciar dependências e ambiente virtual.

### 1. Instalar dependências

```bash
poetry install
```

### 2. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com as variáveis do banco e do ambiente:

```env
DATABASE_URL=postgresql://usuario:senha@host:5432/nome_do_banco
APP_ENV=dev
LOG_LEVEL=INFO
SCHEMA_BRONZE=bronze
SCHEMA_SILVER=silver
SCHEMA_GOLD=gold
RAW_DATA_DIR=data/raw
```

> O arquivo `.env` fica protegido pelo `.gitignore` e não deve ser versionado.

## Execução do pipeline

### Rodar a pipeline completa

```bash
poetry run medicinal
```

### Rodar a pipeline apagando os schemas antes

```bash
poetry run medicinal --reset
```

### Reset manual do banco

```bash
poetry run python -m medicinal.reset_db
```

### Reset manual com confirmação ignorada

```bash
poetry run python -m medicinal.reset_db --no-confirm
```

## Execução de testes

```bash
poetry run task tests
```

Esse comando executa pytest e gera relatório de cobertura.

## Formatação e linting

```bash
poetry run task lint
```

```bash
poetry run task format
```

## Documentação

A documentação do projeto foi criada com MkDocs Material e também pode ser publicada automaticamente via GitHub Pages com o workflow de deploy em [.github/workflows/docs.yml](.github/workflows/docs.yml).

### Rodar a documentação localmente

```bash
poetry run mkdocs serve
```

Acesse:

```text
http://127.0.0.1:8000
```

## Segurança

Algumas precauções importantes:

- nunca commitar o arquivo `.env`;
- manter credenciais em ambiente seguro;
- usar usuário de banco com permissões mínimas;
- evitar execução de `DROP SCHEMA` em ambiente de produção sem confirmação explícita;
- manter `site/` fora do controle de versão quando gerado localmente.

## Casos de uso do projeto

- estudo de ETL simples;
- aprendizado de práticas de bronze/silver/gold;
- manipulação de dados de saúde sintéticos;
- automação de pipelines com Python e SQL;
- documentação de arquitetura de dados em linguagem acessível.

## Próximos passos sugeridos

- adicionar mais fontes de dados e tabelas;
- expandir consultas SQL analíticas;
- criar dashboards simples de BI;
- incluir orquestração via Airflow ou Prefect;
- separar a aplicação em módulos mais especializados.

## Licença

Este projeto é destinado a fins educacionais e de estudo.

## Observação final

O objetivo não é reproduzir um sistema de dados enterprise completo, mas sim representar uma solução clara e compreensível de pipeline de dados, com foco em organização, lógica de ETL e fluidez de desenvolvimento.
