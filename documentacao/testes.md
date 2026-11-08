# Testes iniciais com YOLO

Arquivo: `codigo/testar_yolo.py`. O código realiza inferência em **todos os frames** e mede o tempo do programa completo e o tempo de chamada ao modelo. Não treina EPIs.

## Comandos

```bash
python codigo/testar_yolo.py --modelo yolov8n.pt --duracao 60
python codigo/testar_yolo.py --modelo yolo11n.pt --duracao 60
python codigo/testar_yolo.py --modelo yolo26n.pt --duracao 60
```

Por padrão: webcam `0`, CPU, entrada YOLO `480`, confiança `0.4`, aquecimento de 5 segundos e coleta de 60 segundos. Pressione **Q** para sair antes. Para arquivo de vídeo: `--fonte caminho/video.mp4`. Para pesos locais próprios: `--modelo modelos/seu_modelo.pt`.

**Os pesos baixados são guardados em `modelos/` quando gerados no diretório de execução.** O CSV é salvo em `documentacao/resultados/`.

## Como interpretar

- **FPS total** inclui a leitura de câmera/vídeo, a chamada ao modelo e a tela. Não é apenas FPS de inferência.
- **Modelo (ms)** mede a duração da chamada `predict`.
- **P95** indica um limite abaixo do qual aproximadamente 95% das amostras de latência se encontram.
- O CSV inclui também o tempo interno de inferência informado pelo Ultralytics, quando disponível.

Compare os três modelos com a mesma fonte de vídeo, computador, configurações e iluminação. Registre no diário de bordo o processador (Intel Core i3 7ª geração), 8 GB de RAM, o sistema operacional, a configuração da câmera e as medições obtidas.

Esses testes com pesos gerais **não medem** Precision, Recall ou mAP para detecção de EPIs. Isso exigirá um dataset anotado e uma avaliação separada.

**Status:** código preparado; execução no notebook e métricas reais ainda precisam ser validadas.
