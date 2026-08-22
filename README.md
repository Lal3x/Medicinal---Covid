# Medicinal Analytics

[![CI](https://github.com/Lal3x/Medicinal---Covid/actions/workflows/ci.yml/badge.svg?branch=dev)](https://github.com/Lal3x/Medicinal---Covid/actions/workflows/ci.yml?query=branch%3Adev)

Pipeline educacional de dados clínicos sintéticos, organizado nas camadas Bronze,
Silver e Gold. O Apache Airflow orquestra o processamento, o PostgreSQL armazena
os dados e o Streamlit apresenta os indicadores em uma interface executiva.

## Arquitetura

```text
CSV (patients, encounters, conditions)
                  │
                  ▼
               Airflow
                  │
        Bronze → Silver → Gold
                  │
                  ▼
              Streamlit
```

- **Bronze:** lê os CSVs, normaliza nomes de colunas, adiciona metadados e faz
  upsert idempotente por chave natural.
- **Silver:** valida, limpa e padroniza pacientes, atendimentos e condições.
- **Gold:** cria a visão integrada e os resumos analíticos consumidos pelo painel.

## Tecnologias

- Python 3.13, Poetry, Pandas e SQLAlchemy;
- PostgreSQL 17;
- Apache Airflow 3.1.7;
- Streamlit e Plotly;
- Docker Compose;
- pytest, pytest-cov, Ruff, Black e pre-commit;
- MkDocs Material.

## Início rápido

### 1. Prepare o ambiente

```bash
cp .env.example .env
openssl rand -hex 64
```

Copie o valor gerado para `AIRFLOW_JWT_SECRET` no `.env`. Em Linux, ajuste
`AIRFLOW_UID` para o resultado de `id -u` se quiser que os logs sejam gravados com
o seu usuário.

### 2. Adicione os dados

Coloque os arquivos abaixo em `data/raw/`:

```text
patients.csv
encounters.csv
conditions.csv
```

### 3. Suba os serviços

```bash
docker compose up -d --build
docker compose ps
```

O `airflow-init` executa automaticamente as migrações e cria o usuário inicial.
Com o `.env.example`, as interfaces ficam disponíveis em:

| Serviço | Endereço | Credenciais locais |
| --- | --- | --- |
| Airflow | http://localhost:8080 | `airflow` / `airflow` |
| Streamlit | http://localhost:8501 | não exige login |
| PostgreSQL da aplicação | `localhost:5432` | definidas no `.env` |
| PostgreSQL do Airflow | `localhost:5433` | definidas no `.env` |

As credenciais de exemplo são exclusivas para desenvolvimento local.

## Executar o pipeline

Na interface do Airflow, abra `medicinal_pipeline` e clique em **Trigger DAG**. A
DAG executa:

```text
verificar_banco ───────┐
                       ├─> criar_schemas -> carregar_bronze
verificar_arquivos ────┘                         │
                                                ▼
                                      transformar_silver
                                                │
                                                ▼
                                          agregar_gold
```

Também é possível executar diretamente pelo Poetry:

```bash
poetry install
poetry run medicinal
```

Para recriar as camadas desde o início:

```bash
poetry run medicinal --reset
```

## Comandos de desenvolvimento

```bash
poetry run task tests   # 39 testes, coverage atual de 77%, mínimo de 70%
poetry run task lint    # imports, Ruff e Black
poetry run task format  # aplica formatação
poetry run mkdocs serve # documentação em http://127.0.0.1:8000
```

## Estrutura principal

```text
app/                    painel Streamlit
dags/                   DAG do Airflow
data/raw/               CSVs locais, não versionados
sql/ddl/                criação dos schemas
src/medicinal/          pipeline Python
tests/unit/             testes automatizados
docs/                   documentação MkDocs
config/airflow/         configurações avançadas opcionais
plugins/                extensões opcionais do Airflow
logs/airflow/           logs locais, não versionados
```

As pastas `config/airflow` e `plugins` estão preparadas para extensões futuras,
mas não possuem configuração obrigatória no estado atual.

## Documentação

A documentação completa inclui instalação, arquitetura, pipeline e cobertura de
testes. Ela também é validada e publicada pelo workflow
[docs.yml](.github/workflows/docs.yml).

## Automação no GitHub

- `ci.yml`: mantém as verificações de qualidade e testes do projeto;
- `docker.yml`: valida o Compose e constrói as imagens em alterações relevantes;
- `codeql.yml`: executa SAST para Python em pushes, pull requests e semanalmente;
- `docs.yml`: publica o MkDocs pelas Actions oficiais do GitHub Pages;
- `dependabot.yml`: verifica semanalmente Actions, Python e Docker.

O DAST não faz parte do fluxo atual. Ele pode ser incluído futuramente contra o
Streamlit quando houver um ambiente de teste estável.

## Segurança

- não versione `.env`, dados locais ou logs;
- use uma chave JWT forte e igual em todos os serviços Airflow;
- substitua as credenciais padrão fora do ambiente local;
- não execute reset de schemas em produção sem uma estratégia de recuperação.

## Escopo

O projeto usa dados sintéticos e tem finalidade educacional. Ele não representa
um sistema clínico de produção nem deve ser usado para decisões médicas.
