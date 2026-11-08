# Estrutura planejada do repositorio

Esta organizacao foi inspirada na separacao entre fonte, exemplos, documentacao e testes de projetos profissionais como **Ultralytics** (https://github.com/ultralytics/ultralytics) e **Roboflow Supervision** (https://github.com/roboflow/supervision), com simplificacoes apropriadas para um PIBIC-Jr.

| Pasta/arquivo | Objetivo |
| --- | --- |
| `README.md` | Descricao geral da pesquisa (existente; preservado). |
| `AGENTS.md` | Orientacoes para agentes auxiliarem sem substituir a aprendizagem. |
| `requirements.txt` | Dependencias iniciais do ambiente Python. |
| `docs/` | Diario de bordo, guias, fundamentacao e registros de metodologia. |
| `uteis/` | Materiais de estudo ja presentes no repositorio. |
| `notebooks/` | Exercicios guiados e notebooks futuros do Colab. |
| `data/` | Dados locais: brutos, intermediarios e preparados; nao versionados. |
| `configs/` | Configuracoes futuras de dataset e experimentos. |
| `src/detector_epis/` | Codigo-fonte futuro, separado por responsabilidade. |
| `scripts/` | Pontos de entrada futuros para tarefas de linha de comando. |
| `tests/` | Testes automatizados futuros. |
| `experimentos/` | Protocolos e fichas dos testes cientificos. |
| `models/` | Modelos/pesos locais, nao versionados por padrao. |
| `resultados/` | Saidas produzidas por experimentos, nao versionadas por padrao. |
| `deploy/raspberry_pi/` | Preparacao futura da demonstracao embarcada. |

## Responsabilidades previstas em src/detector_epis/
- `captura/`: leitura futura de imagens, videos e camera.
- `processamento/`: manipulacao e preparo de imagens.
- `deteccao/`: integracao com modelo YOLO.
- `visualizacao/`: desenho de caixas, rotulos e resultados.
- `verificacao/`: associacao de EPIs a pessoas e criterios de conformidade.
- `avaliacao/`: calculo e registro de desempenho.

Essas subpastas sao **vazias**. Elas indicam apenas destinos provaveis do codigo, nao funcionalidades concluidas.

## Proximas mudancas, por ordem
1. Concluir a instalacao e documentar o ambiente local.
2. Criar exercicios curtos em `notebooks/` e `scripts/` para imagens digitais e OpenCV.
3. Definir classes antes de criar `configs/dataset.yaml` real.
4. Selecionar, anotar e separar imagens em treinamento, validacao e teste.
5. Implementar e comparar YOLO11n e YOLO11s.
6. Construir inferencia em imagens, videos e webcam.
7. Adaptar e validar a inferencia no Raspberry Pi.
