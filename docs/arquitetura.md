# Visão Geral da Arquitetura

A arquitetura do projeto foi pensada para simular um fluxo de dados em camadas, de forma simples e didática.

## Fluxo do pipeline

```text
CSV / dados brutos
        ↓
   Bronze
        ↓
   Silver
        ↓
   Gold
```

## Camada Bronze

A camada bronze é responsável por receber os dados em formato CSV e carregá-los praticamente da forma como chegam. Nesta etapa:

- os arquivos são lidos em Python;
- as colunas são normalizadas;
- metadados de execução são adicionados;
- os dados são persistidos em tabelas de origem.

Objetivo: preservar os dados originais sem perder contexto.

## Camada Silver

A camada silver realiza etapa de limpeza e padronização. O principal foco é:

- validar a qualidade dos dados;
- remover inconsistências;
- transformar colunas e campos;
- separar e organizar informações relevantes para análise.

Essa etapa produz tabelas mais confiáveis para uso analítico.

## Camada Gold

A camada gold é a parte analítica do pipeline. Nesta etapa são criadas:

- tabelas agregadas por paciente;
- resumos por tipo de encontro;
- uma visão conjunta dos dados para análise exploratória.

Essas tabelas são mais adequadas para consultas e relatórios.

## Benefícios do modelo

- organização clara do processamento;
- facilidade de depuração por etapa;
- rastreabilidade das transformações;
- melhor qualidade dos dados para uso analítico.

## Observações

Esse projeto não busca reproduzir uma plataforma completa de dados em produção. A proposta é demonstrar, de maneira acessível, o pensamento de pipeline de dados em camadas usando tecnologias simples e eficientes.
