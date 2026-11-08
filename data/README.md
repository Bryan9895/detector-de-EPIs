# Dados da pesquisa

Esta pasta organiza **arquivos locais** que serao obtidos nas etapas de dataset e anotacao.

- `raw/`: imagens originais, sem modificacoes.
- `interim/`: dados em revisao/limpeza.
- `processed/`: dados finais preparados para treino, validacao e teste.

Quando chegar a etapa de anotacao, a estrutura YOLO podera incluir `train/images`, `train/labels`, `val/images`, `val/labels`, `test/images` e `test/labels`, acompanhados de configuracao YAML.

**Neste momento nao existe dataset no repositorio.** Imagens, rotulos e videos dessas pastas estao excluidos do Git por padrao. Registrar fonte, licenca e versao dos dados na documentacao.
