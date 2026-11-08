# Ambiente computacional

O repositório já contém a estrutura e as dependências previstas. **Os comandos abaixo devem ser executados no computador do estudante; não representam uma instalação já validada.**

## Ubuntu

```bash
python3 --version
git --version
# Se o Python não tiver venv: sudo apt install python3-venv python3-pip
git clone git@github.com:Bryan9895/detector-de-EPIs.git
cd detector-de-EPIs
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -c "import cv2, numpy, ultralytics; print('Bibliotecas OK')"
```

Se já clonou o repositório, basta entrar na pasta e executar `git pull origin main`, sem clonar novamente.

## Execução do teste inicial

```bash
python codigo/testar_yolo.py --modelo yolo26n.pt --duracao 60
```

- `codigo/`: códigos do projeto.
- `modelos/`: pesos utilizados e treinados, armazenados localmente.
- `documentacao/resultados/`: CSVs locais dos testes.
- `documentacao/`: diário de bordo, documentação e materiais de estudo.

Documente as versões do Python e das bibliotecas, os problemas encontrados e a execução no diário de bordo. `requirements.txt` ainda não fixa versões; ele poderá ser ajustado quando o ambiente tiver sido validado.

O Raspberry Pi precisará de uma instalação e validação próprias em etapa posterior.
