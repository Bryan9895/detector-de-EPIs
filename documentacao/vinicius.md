# Código original — Vinicius Rielmison Rocha de Sousa

O arquivo `codigo/vinicius_yolov8.py` é uma cópia **sem alterações de conteúdo** do script `detcção_yolo.py` do antigo bolsista.

- Autor: **Vinicius Rielmison Rocha de Sousa**.
- Origem: https://github.com/vinicius-rielmison/detect-yolo-v8-py
- Commit de origem consultado: `a903aa7389567f60c5c8c8b27465cab23e760379`.
- README original: [README-original-vinicius.md](README-original-vinicius.md).
- Atribuição e termos: [LICENSE-vinicius](LICENSE-vinicius) (o repositório original declara licença MIT no README).

## O que o código faz

YOLOv8n + OpenCV com webcam, caixas personalizadas, painel HUD, contagem de pessoas, FPS do loop, tempo coletivo e aviso visual. **Não é ainda um detector especializado em EPIs.**

## Limitações já identificadas

- Usa `cv2.CAP_DSHOW`, destinado ao Windows (não adequado diretamente ao Ubuntu).
- Faz inferência a cada dois frames, podendo exibir caixas defasadas.
- O FPS mostrado não isola o tempo da inferência.
- O tempo de permanência não acompanha cada pessoa individualmente.
- O README original recomenda `main.py`, mas o script tem outro nome.

Para preservar a rastreabilidade científica, novas alterações devem ser feitas em outro arquivo da pasta `codigo/`, não no original.
