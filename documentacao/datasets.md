# Datasets de EPIs — Preparação para GitHub Releases

**Situação:** os seis arquivos foram localizados no Google Drive pessoal em 08/11/2026. A publicação da Release **não foi realizada por esta documentação**. O conjunto totaliza aproximadamente 1,49 GB.

Os arquivos são exportações de datasets no formato YOLO26. **Não são modelos treinados nem resultados de treinamento.**

| Arquivo | Tamanho em bytes |
| --- | ---: |
| `Personal Protective Equipment.v4i.yolo26.zip` | 133512398 |
| `Personal Protective Equipment.v3i.yolo26.zip` | 133512349 |
| `Personal Protective Equipment.v1i.yolo26-1.zip` | 559190869 |
| `Personal Protective Equipment.v1i.yolo26.zip` | 133512346 |
| `Personal Protective Equipment.v2i.yolo26.zip` | 295873629 |
| `Personal Protective Equipment.v1-2024-05-13-07.17pm-v1.yolo26.zip` | 235047627 |

## Como enviar os seis ZIPs

1. Baixe os seis arquivos do Google Drive pessoal no computador e coloque-os na **mesma pasta**, mantendo os nomes exatamente como na tabela.
2. No Ubuntu, instale o GitHub CLI com `sudo apt install gh` (se ainda não estiver instalado), e autentique-se com `gh auth login`.
3. Na raiz do repositório atualizado, execute `bash codigo/publicar_datasets.sh "$HOME/Downloads"` ou informe o diretório real.
4. O script só continuará se encontrar os **seis** ZIPs com os tamanhos esperados; então criará uma Release `datasets-v1` **em rascunho** e anexará os ZIPs.
5. Confira cada dataset, sua licença e as permissões de redistribuição antes de publicar com `gh release edit datasets-v1 -R Bryan9895/detector-de-EPIs --draft=false`.

Para verificar o que está anexado, execute `gh release view datasets-v1 -R Bryan9895/detector-de-EPIs --json assets`.

**Por que uma Release?** Os ZIPs ultrapassam o limite de 100 MB do Git normal. Como anexos de Release, ficam associados ao repositório sem integrar o histórico da branch `main`.

**Atenção científica:** é preciso comparar classes, qualidade das anotações, possíveis duplicações entre versões, divisões treino/validação/teste e licenças antes de usar os dados para treinar ou publicar. O tamanho, isoladamente, não comprova integridade ou qualidade. O script valida presença e tamanho, mas não valida hashes criptográficos nem conteúdo ZIP.
