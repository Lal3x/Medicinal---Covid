# Estrutura do Projeto

A estrutura do repositório foi organizada para separar responsabilidades e facilitar a manutenção do pipeline.

```text
medicinal/
├── .env                    # variáveis de ambiente locais
├── .gitignore              # proteção de arquivos sensíveis e locais
├── .python-version         # versão do Python do projeto
├── README.md               # resumo rápido do projeto
├── mkdocs.yml              # configuração do MkDocs Material
├── poetry.lock             # lock do Poetry
├── pyproject.toml          # dependências e configuração do projeto
├── notebooks/              # notebooks de análise e validação
├── sql/
│   ├── ddl/                # scripts SQL de criação de schemas e tabelas
│   └── queries/            # consultas analíticas e SQL utilitário
├── src/
│   └── medicinal/
│       ├── __init__.py
│       ├── __main__.py
│       ├── main.py
│       ├── reset_db.py
│       ├── bronze/
│       │   ├── ingest.py
│       │   └── readers.py
│       ├── silver/
│       │   ├── transform.py
│       │   └── transformations.py
│       ├── gold/
│       │   ├── aggregate.py
│       │   └── aggregations.py
│       ├── config/
│       │   └── settings.py
│       └── utils/
│           ├── db.py
│           └── schema.py
├── tests/
│   ├── __init__.py
│   └── unit/
│       ├── conftest.py
│       ├── test_bronze_readers.py
│       └── test_silver_transformations.py
└── docs/
    ├── index.md
    ├── arquitetura.md
    ├── estrutura.md
    ├── instalacao.md
    └── pipeline.md
```

## Padrão de organização

### `src/medicinal`

Contém os módulos da aplicação, separados por camada funcional:

- `bronze`: ingestão e leitura dos dados brutos;
- `silver`: limpeza, validação e transformações;
- `gold`: agregações e tabelas finais;
- `config`: leitura de configurações e variáveis de ambiente;
- `utils`: utilitários de conexão ao banco e criação de schemas.

### `sql`

Arquivos SQL para criação de objetos no banco e consultas reutilizáveis.

### `tests`

Testes automatizados para garantir a lógica de transformação e leitura dos dados.

### `docs`

Documentação técnica e conceitual do projeto com MkDocs Material.
