# Scripts de execução

## Primeiro teste de YOLO com webcam

O arquivo `testar_yolo.py` é uma atividade prática introdutória para medir desempenho e visualizar detecções. Não treina um detector de EPIs; utiliza modelos gerais pré-treinados.

### Preparação no Ubuntu

1. Abra a pasta do repositório e ative `.venv` (`source .venv/bin/activate`).
2. Instale as dependências (`python -m pip install -r requirements.txt`).
3. Confira a câmera: normalmente o índice `0` é a webcam integrada.

### Execução

```bash
python scripts/testar_yolo.py --modelo yolo26n.pt --duracao 60
```

Também é possível comparar nas mesmas condições:

```bash
python scripts/testar_yolo.py --modelo yolov8n.pt --duracao 60
python scripts/testar_yolo.py --modelo yolo11n.pt --duracao 60
python scripts/testar_yolo.py --modelo yolo26n.pt --duracao 60
```

Se precisar indicar outra câmera, use `--fonte 1`. Para testar um arquivo de vídeo, use `--fonte caminho/video.mp4`. O vídeo precisa existir no computador.

Pressione **Q** para encerrar. O padrão é **5 segundos de aquecimento** seguidos de **60 segundos de medição**. Cada quadro é processado pelo modelo, sem pular frames. O dispositivo padrão é **CPU**, permitindo uma comparação no notebook sem depender de GPU.

### Como ler os resultados

- **FPS total:** velocidade do programa inteiro, incluindo captura, predição, desenho e janela.
- **Modelo (ms):** tempo completo da chamada `modelo.predict()`.
- **Inferência interna (ms):** valor que a biblioteca Ultralytics informa separadamente (se disponível), registrado no CSV.
- **P95:** 95% dos tempos de chamada ao modelo estão nesse valor ou abaixo (aproximação por posto).

O CSV é gerado em `resultados/` e não é enviado automaticamente ao Git (a pasta está no `.gitignore`). Arquivos `.pt` também são ignorados.

Os três modelos carregados usam pesos **genéricos**, não pesos treinados especificamente para EPIs. As detecções observadas não comprovam conformidade com normas de segurança.

Para uma comparação justa, mantenha a mesma câmera/vídeo, iluminação, computador, `--imgsz`, `--conf` e `--device`. Execute mais de uma vez, sem outros programas pesados.

**Situação:** verificada a sintaxe do script; ainda é necessário testar webcam e desempenho em uma máquina real.
