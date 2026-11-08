# Protótipo histórico — Vinicius Rielmison

Este diretório guarda o código desenvolvido pelo antigo bolsista **Vinicius Rielmison Rocha de Sousa**, preservado como referência histórica do projeto PIBIC-Jr.

- **Origem:** https://github.com/vinicius-rielmison/detect-yolo-v8-py
- **Revisão de origem:** `a903aa7389567f60c5c8c8b27465cab23e760379` (branch `main` consultada em 08/11/2026).
- **Arquivo original:** `detcção_yolo.py` (nome e código mantidos como no repositório de origem).
- **README original:** `README-original.md` (mantido integralmente para consulta).
- **Autoria:** Vinicius Rielmison Rocha de Sousa.
- **Licenciamento:** o README do repositório original declara **MIT**; veja o arquivo `LICENSE` neste diretório com a licença e o aviso de autoria do código reproduzido. O repositório original, na revisão consultada, não continha arquivo LICENSE separado.

## O que o protótipo faz

Usa `yolov8n.pt`, OpenCV e webcam. Desenha caixas delimitadoras, uma interface HUD, contagem de pessoas, estimativa de FPS, tempo coletivo com pessoas visíveis e um aviso quando identifica alguém. É **um monitor de objetos/pessoas**, ainda **não um modelo especializado em capacetes, luvas, botas e outros EPIs**.

## Limitações conhecidas

- O código usa `cv2.CAP_DSHOW`, backend de câmera próprio de Windows. No Ubuntu (e em Raspberry Pi), será necessária uma versão adaptada e testada.
- O script original é `detcção_yolo.py`, apesar de o README original citar `main.py`.
- O tempo de permanência não identifica pessoas individualmente, e a métrica de FPS representa o loop de apresentação, não uma medida isolada de latência de inferência.
- As detecções são executadas a cada dois frames e reapresentadas nos frames intermediários; não há rastreamento de pessoas nem associação de EPIs a trabalhadores.

## Como consultar / executar depois

Antes de rodar, preparar e validar o ambiente indicado em `docs/ambiente-computacional.md`. No Windows, com webcam disponível e dependências instaladas, o comando original poderá ser testado a partir da raiz do repositório:

```bash
python 'legado/vinicius-rielmison/detcção_yolo.py'
```

Pressione `q` para encerrar. **A execução não foi testada nesta importação.** Não modificar este arquivo histórico: para adaptações futuras, criar implementações novas em `src/` ou `scripts/`, mantendo o registro das diferenças.
