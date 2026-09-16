# Detecção Automática de EPIs com Visão Computacional

Projeto de iniciação científica do **PIBIC Jr. 2026** voltado ao desenvolvimento de um modelo de Inteligência Artificial capaz de detectar Equipamentos de Proteção Individual em imagens e vídeos de ambientes industriais.

## Sobre o projeto

O projeto **Introdução à Inteligência Artificial por Meio da Detecção Automática de EPIs com Visão Computacional** possui dois objetivos principais: desenvolver uma solução tecnológica para auxiliar o monitoramento de segurança e introduzir o bolsista às práticas de pesquisa aplicada em Inteligência Artificial.

Durante o projeto serão estudados conceitos de programação em Python, Visão Computacional, Deep Learning, detecção de objetos, preparação de datasets, treinamento de modelos e avaliação experimental.

## Problema

A fiscalização do uso de EPIs normalmente depende da observação humana. Em ambientes industriais com muitos trabalhadores e diferentes áreas operacionais, o monitoramento manual contínuo pode ser limitado e sujeito a falhas.

A ausência ou o uso inadequado de equipamentos como capacetes, luvas, botas, coletes e óculos de proteção pode aumentar a exposição dos trabalhadores a acidentes.

## Solução proposta

A proposta é desenvolver e avaliar um modelo baseado em **YOLO11** para identificar automaticamente EPIs em imagens e vídeos.

O fluxo previsto para o sistema é:

1. receber uma imagem ou um vídeo;
2. processar os quadros com o modelo treinado;
3. localizar e classificar os EPIs encontrados;
4. verificar a presença dos equipamentos obrigatórios;
5. indicar possíveis situações de não conformidade;
6. futuramente, permitir a geração de alertas.

## Objetivo geral

Desenvolver um modelo de Inteligência Artificial baseado em Visão Computacional para detecção automática de EPIs em ambientes industriais, promovendo a introdução de estudantes do ensino médio integrado aos conceitos e às práticas de pesquisa aplicada em IA.

## Objetivos específicos

- Estudar Inteligência Artificial, Visão Computacional e detecção de objetos.
- Aprender a utilizar Python, OpenCV, Roboflow e modelos YOLO.
- Construir e organizar uma base de imagens relacionadas ao uso de EPIs.
- Treinar e avaliar um modelo de detecção automática utilizando Deep Learning.
- Desenvolver habilidades de pesquisa científica, documentação e análise experimental.

## Tecnologias e ferramentas

| Ferramenta | Utilização no projeto |
|---|---|
| Python | Linguagem principal para treinamento, inferência e testes |
| YOLO11 | Modelo de detecção de objetos |
| Ultralytics | Biblioteca utilizada para treinar e executar o YOLO11 |
| OpenCV | Processamento de imagens, vídeos e captura de webcam |
| Roboflow | Organização, anotação e exportação do dataset |
| Google Colab | Treinamento do modelo com acesso a GPU |
| NumPy | Manipulação de dados numéricos e matrizes |
| Git e GitHub | Versionamento do código e documentação do projeto |

## Metodologia

O desenvolvimento será dividido nas seguintes etapas:

1. estudo dos conceitos fundamentais;
2. preparação do ambiente de desenvolvimento;
3. coleta e organização das imagens;
4. anotação dos EPIs com caixas delimitadoras;
5. divisão do dataset em treino, validação e teste;
6. treinamento do YOLO11;
7. ajuste de parâmetros e realização de novos testes;
8. avaliação com métricas como Precision, Recall e mAP;
9. aplicação do modelo em imagens e vídeos;
10. documentação e apresentação dos resultados.

## Estrutura prevista do repositório

```text
PIBIC-Jr-Deteccao-EPIs/
├── README.md
├── docs/
│   ├── diario-de-bordo.md
│   ├── objetivos-do-projeto.md
│   └── referencias.md
├── notebooks/
│   └── treinamento_yolo.ipynb
├── src/
│   ├── detectar_imagem.py
│   ├── detectar_video.py
│   └── detectar_webcam.py
├── resultados/
├── models/
├── requirements.txt
└── .gitignore
```

> A estrutura será atualizada conforme o projeto avançar. Pastas e arquivos ainda não desenvolvidos representam a organização planejada.

## Documentação

- [Diário de bordo](docs/diario-de-bordo.md)
- Objetivos e compreensão inicial do projeto
- Referências e materiais de estudo

O diário de bordo registra as atividades realizadas, dificuldades, aprendizados, decisões, experimentos e próximos passos da pesquisa.

## Resultados esperados

- dataset de EPIs organizado e validado;
- modelos YOLO treinados e avaliados;
- scripts para detecção em imagens e vídeos;
- comparação entre diferentes experimentos;
- documentação técnico-científica;
- relatório final e apresentação dos resultados;
- desenvolvimento de conhecimentos em IA e pesquisa científica.

## Situação atual

O projeto está em sua fase inicial. Até o momento foram realizadas:

- leitura e análise do documento do projeto;
- identificação do problema, da solução e dos objetivos;
- estudo sobre iniciação científica;
- criação do relatório de compreensão inicial;
- criação do diário de bordo;
- organização inicial da documentação.

## Próximos passos

- criar e configurar o repositório no GitHub;
- preparar o ambiente Python;
- estudar os fundamentos de Visão Computacional e YOLO;
- pesquisar datasets públicos de EPIs;
- iniciar os primeiros testes de detecção.

## Referência principal

**Projeto PIBIC Jr.** *Introdução à Inteligência Artificial por Meio da Detecção Automática de EPIs com Visão Computacional*. Versão 2.0. Fortaleza, maio de 2026.
