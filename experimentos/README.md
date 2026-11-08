# Experimentos científicos

Pasta destinada a protocolos de comparação e fichas de experimentos, contemplando dados, classes, parâmetros, hardware, Precision, Recall, mAP, latência e FPS.

## Teste exploratório inicial de velocidade

O script `scripts/testar_yolo.py` permite medir FPS do programa e tempo de chamada ao modelo de YOLOv8n, YOLO11n e YOLO26n. Ele grava as medições por frame em `resultados/`.

Para documentar o experimento, registre no diário de bordo: data; modelo; comando; processador, RAM e sistema; fonte de vídeo; resolução; duração e aquecimento; FPS médio; tempo médio, mediana e P95 da chamada ao modelo; dificuldades encontradas.

**Cuidado:** o teste de velocidade não mede precisão, recall ou mAP. Essas métricas exigem imagens rotuladas e um protocolo de avaliação específico. Não confundir objetos gerais detectados por pesos COCO com detecção especializada de EPIs.
