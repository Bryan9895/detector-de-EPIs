#!/usr/bin/env bash
# Publicação de datasets do PIBIC-Jr como anexos de uma GitHub Release.
# Uso: bash codigo/publicar_datasets.sh "/caminho/para/pasta-com-os-6-zips"
set -euo pipefail

REPO="Bryan9895/detector-de-EPIs"
TAG="datasets-v1"
PASTA="${1:-$HOME/Downloads}"

if ! command -v gh >/dev/null 2>&1; then
    echo "ERRO: GitHub CLI (gh) não encontrado. Instale com: sudo apt install gh"
    exit 1
fi
if ! gh auth status >/dev/null 2>&1; then
    echo "ERRO: faça login no GitHub primeiro: gh auth login"
    exit 1
fi
if [ ! -d "$PASTA" ]; then
    echo "ERRO: pasta inexistente: $PASTA"
    exit 1
fi

NOMES=(
    "Personal Protective Equipment.v4i.yolo26.zip"
    "Personal Protective Equipment.v3i.yolo26.zip"
    "Personal Protective Equipment.v1i.yolo26-1.zip"
    "Personal Protective Equipment.v1i.yolo26.zip"
    "Personal Protective Equipment.v2i.yolo26.zip"
    "Personal Protective Equipment.v1-2024-05-13-07.17pm-v1.yolo26.zip"
)
TAMANHOS=(133512398 133512349 559190869 133512346 295873629 235047627)

ARQUIVOS=()
echo "Verificando os 6 datasets em $PASTA ..."
for i in "${!NOMES[@]}"; do
    caminho="$PASTA/${NOMES[$i]}"
    if [ ! -f "$caminho" ]; then
        echo "FALTANDO: ${NOMES[$i]}"
        exit 1
    fi
    tamanho=$(stat -c %s -- "$caminho")
    if [ "$tamanho" -ne "${TAMANHOS[$i]}" ]; then
        echo "TAMANHO DIFERENTE: ${NOMES[$i]} (encontrado $tamanho, esperado ${TAMANHOS[$i]})"
        echo "Confira se o download foi concluído e se o arquivo não foi alterado."
        exit 1
    fi
    echo "OK: ${NOMES[$i]} ($tamanho bytes)"
    ARQUIVOS+=("$caminho")
done

echo
echo "ATENÇÃO: estes arquivos serão anexados a uma Release em $REPO."
echo "Datasets podem conter imagens e licenças de terceiros."
echo "Confira os termos de redistribuição de CADA dataset antes de torná-los públicos."
read -r -p "Deseja enviar os arquivos para uma Release em RASCUNHO? [s/N] " resposta
if [ "$resposta" != "s" ] && [ "$resposta" != "S" ]; then
    echo "Operação cancelada."
    exit 0
fi

if gh release view "$TAG" -R "$REPO" >/dev/null 2>&1; then
    echo "A Release $TAG já existe; verificando os anexos..."
else
    gh release create "$TAG" -R "$REPO" --target main \
        --title "Datasets EPIs - exportações YOLO26 (outubro de 2026)" \
        --notes "Seis exportações de datasets de EPIs. Arquivos de dados para experimentos; não são pesos treinados. Origem e licenças de redistribuição devem ser verificadas antes da publicação." \
        --latest=false --draft
fi

for caminho in "${ARQUIVOS[@]}"; do
    nome=$(basename "$caminho")
    existente=$(gh release view "$TAG" -R "$REPO" --json assets --jq ".assets[] | select(.name == \"$nome\") | .name")
    if [ -n "$existente" ]; then
        echo "JÁ PRESENTE: $nome (não será sobrescrito)"
    else
        gh release upload "$TAG" "$caminho" -R "$REPO"
        echo "ENVIADO: $nome"
    fi
done

echo
echo "Arquivos presentes na Release:"
gh release view "$TAG" -R "$REPO" --json assets --jq '.assets[] | "\(.name) — \(.size) bytes"'
echo
echo "Release mantida em RASCUNHO para revisar licenças:"
gh release view "$TAG" -R "$REPO" --web
echo "Depois da revisão, publique com:"
echo "gh release edit $TAG -R $REPO --draft=false"
