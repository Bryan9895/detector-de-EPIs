# Detector de EPIs — PIBIC-Jr

Projeto de iniciação científica do **IFCE Campus Maranguape (2026–2027)**. O objetivo é estudar Visão Computacional e desenvolver um detector automático de Equipamentos de Proteção Individual (EPIs), com demonstração futura no Raspberry Pi.

## Estrutura

```text
detector-de-EPIs/
├── codigo/
│   ├── testar_yolo.py       # Teste atual de YOLO e desempenho
│   └── vinicius_yolov8.py   # Protótipo original do antigo bolsista
├── manutencao/              # Ferramentas de suporte ao repositório
│   └── publicar_datasets.sh
├── modelos/                 # Pesos .pt e modelos treinados (locais)
├── documentacao/            # Estudos, diário, testes, materiais e autoria
├── README.md
├── AGENTS.md
├── requirements.txt
└── .gitignore
```

## Começar no Ubuntu

```bash
git clone git@github.com:Bryan9895/detector-de-EPIs.git
cd detector-de-EPIs
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python codigo/testar_yolo.py --modelo yolo26n.pt --duracao 60
```

Se já possui o repositório clonado, execute `git pull origin main` antes de testar.

O teste aceita `yolov8n.pt`, `yolo11n.pt` e `yolo26n.pt`. Os pesos baixados são destinados a `modelos/`; medições CSV vão para `documentacao/resultados/` e não são versionadas.

**Atenção:** esses modelos gerais não são detectores treinados de EPIs. A etapa atual é de aprendizado e testes iniciais, não de monitoramento industrial pronto.

## Documentação

Consulte [documentacao/ambiente.md](documentacao/ambiente.md) para preparar o ambiente, [documentacao/testes.md](documentacao/testes.md) para os experimentos e [documentacao/diario-de-bordo.md](documentacao/diario-de-bordo.md) para o acompanhamento científico.

O protótipo inicial é de **Vinicius Rielmison Rocha de Sousa**. O arquivo de código foi preservado sem alterações; veja [documentacao/vinicius.md](documentacao/vinicius.md) para créditos, limitações e a origem.

## Próximos passos

Estudar Python, imagens digitais e OpenCV; validar o ambiente e os testes; depois preparar o dataset de EPIs, treinar e comparar modelos, desenvolver a detecção e avaliar a execução no Raspberry Pi.

## Datasets para treinamento

Os seis arquivos de imagens anotadas para YOLO26 estão identificados em [documentacao/datasets.md](documentacao/datasets.md). Como são ZIPs grandes, devem ser anexados a uma **GitHub Release**, não à branch `main`. O comando `bash manutencao/publicar_datasets.sh "$HOME/Downloads"` auxilia no envio, depois que os seis ZIPs forem baixados para o computador. **Esta documentação não significa que os datasets já foram publicados.**
