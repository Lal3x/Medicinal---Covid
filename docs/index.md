# Simulação de Pipeline de Dados com SQL e Python (COVID-19)

Este projeto demonstra um pipeline de dados simples construído com Python e SQL, usando dados sintéticos de pacientes gerados pelo Synthea e relacionados à COVID-19.

## Objetivo

O objetivo do projeto é mostrar, de forma didática, como:

- baixar e organizar arquivos em formato CSV;
- carregar dados em um banco relacional;
- transformar esses dados em camadas de processamento;
- aplicar consultas analíticas para obter insights;
- simular uma arquitetura de dados em bronze, silver e gold.

## Contexto

A ideia central é representar um fluxo realista de dados clínicos em um ambiente de dados moderno, sem depender de ferramentas pesadas de engenharia de dados. O projeto usa uma abordagem simples e educacional, focada em estrutura, organização e lógica de processamento.

## Tecnologias utilizadas

- Python: manipulação dos dados, leitura de CSV, transformação e execução do pipeline.
- SQL: criação de schemas, criação de tabelas e consultas analíticas.
- PostgreSQL: banco de dados relacional utilizado como camada de armazenamento.
- SQLAlchemy: integração entre Python e banco de dados.
- Pandas: processamento tabular dos dados.
- pytest e pytest-cov: testes automatizados e cobertura.
- Black, Ruff e Taskipy: padronização, linting e automação de tarefas.
- MkDocs Material: documentação do projeto.

## Arquitetura em camadas

O fluxo de processamento do projeto segue o modelo medalhão:

1. Bronze: dados brutos e originados em CSV.
2. Silver: dados limpos, normalizados e validados.
3. Gold: agregações e tabelas analíticas prontos para consumo.

Esse padrão ajuda a separar dados crus de dados prontos para análise e facilita a manutenção e auditoria do pipeline.

## Casos de uso

- Validação de qualidade dos dados carregados.
- Transformação de dados clínicos e demográficos.
- Agregação de métricas por paciente, encontro e condição.
- Estudo de comportamento e indicadores em dados sintéticos de saúde.

## Próximos passos

- expandir o volume de dados e cenários;
- adicionar mais consultas SQL analíticas;
- incluir automações de orquestração do pipeline;
- criar dashboards de exploração dos resultados.
