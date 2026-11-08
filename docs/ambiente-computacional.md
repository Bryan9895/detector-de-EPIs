# Ambiente computacional — etapa de preparacao

> **Situacao:** estrutura do repositorio preparada. As instalacoes abaixo ainda precisam ser feitas no computador do estudante; nenhum comando foi executado remotamente.

## Objetivo da etapa
Aprender a diferenca entre interpretador Python, ambiente virtual, biblioteca e arquivo de dependencias. Configurar uma maquina local para os primeiros exercicios de Python e OpenCV.

## Ferramentas previstas
- Python 3, Git e VS Code.
- Ambiente virtual `.venv` (local, nao versionado).
- Bibliotecas iniciais: NumPy, OpenCV e Ultralytics.
- Google Colab: sera estudado em etapa posterior para experimentos com GPU.

## Passo a passo futuro — Ubuntu
1. Verificar se Python 3 e Git estao instalados: `python3 --version` e `git --version`.
2. Se necessario, instalar as ferramentas de sistema: `sudo apt install python3 python3-venv python3-pip git`.
3. Clonar o repositorio (HTTPS): `git clone https://github.com/Bryan9895/detector-de-EPIs.git`.
4. Entrar na pasta: `cd detector-de-EPIs`.
5. Criar o ambiente virtual: `python3 -m venv .venv`.
6. Ativar: `source .venv/bin/activate`.
7. Instalar dependencias: `python -m pip install -r requirements.txt`.
8. Conferir a instalacao: `python -c "import cv2, numpy, ultralytics; print('Bibliotecas importadas com sucesso')"`.
9. Registrar no diario de bordo as versoes, erros encontrados e o resultado do teste.

> O arquivo `requirements.txt` e uma lista inicial, nao um conjunto de versoes homologadas. Depois de testar, registrar versoes compativeis para reproduzir o ambiente. A instalacao no Raspberry Pi exigira validacao propria.

## O que esta etapa NAO implementa
- Nenhum codigo de detecao de EPIs.
- Nenhum dataset ou anotacao.
- Nenhum treinamento YOLO.
- Nenhuma integracao com webcam nem Raspberry Pi.

## Criterios de conclusao (a verificar pelo estudante)
- [ ] Explicar Python, `pip`, `venv` e dependencias.
- [ ] Mostrar `python --version` e `pip --version` dentro do ambiente.
- [ ] Importar as tres bibliotecas sem erro.
- [ ] Registrar os procedimentos e dificuldades no diario de bordo.
