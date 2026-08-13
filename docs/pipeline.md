# Pipeline de Dados

A execução do projeto segue uma sequência lógica e bem organizada para transformar dados brutos em informações analíticas.

## 1. Coleta e ingestão

Os dados são lidos a partir de arquivos CSV. Essa etapa representa a entrada do sistema e é a base para o restante do fluxo.

## 2. Camada Bronze

Nesta etapa, os dados são carregados da forma mais próxima possível do que foi recebido. As principais ações são:

- leitura dos arquivos;
- normalização de colunas;
- registro de metadados da execução;
- persistência em schemas bronze.

## 3. Camada Silver

Depois de carregados, os dados passam por validações e transformações. Essa camada é responsável por:

- remover ruídos e dados inconsistentes;
- padronizar nomes e formatos;
- tratar valores nulos e campos críticos;
- preparar os dados para análise.

## 4. Camada Gold

A última etapa transforma os dados em modelos mais próximos do consumo analítico. Aqui são criados:

- resumos por paciente;
- resumos por tipo de encontro;
- visões integradas para consultas e relatórios.

## 5. Observabilidade

Durante o processo, o código registra mensagens de status e validações. Isso facilita a identificação de falhas e a compreensão do que aconteceu em cada etapa.

## 6. Reexecução segura

Quando necessário, é possível reiniciar o processo apagando os schemas do banco antes de executar novamente a pipeline.

Esse mecanismo é útil em ambientes de desenvolvimento e testes, auxiliando a reprodução de cenários e a validação de novas regras de negócio.
