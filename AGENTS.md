# PIBIC-Jr — Orientações para agentes de código

Este projeto é uma iniciação científica de ensino médio integrado em Informática (IFCE Campus Maranguape). **A compreensão do estudante vem antes da automação.**

- Código do detector e testes: `codigo/`. Ferramentas auxiliares: `manutencao/`. Pesos: `modelos/`. Toda a documentação, registros e materiais: `documentacao/`.
- Antes de desenvolver, explicar o conceito e a finalidade da mudança.
- Respeitar o Kanban; fazer mudanças pequenas e verificáveis.
- Não afirmar que houve execução/validação se a máquina ou câmera não foi testada.
- Preservar a autoria do protótipo de Vinicius em `codigo/vinicius_yolov8.py`.
- Evitar diretórios e abstrações que não resolvam necessidades atuais.
- Não versionar pesos pesados, dados pessoais, datasets volumosos, CSVs locais ou segredos.
- O objetivo final é demonstrar um detector de EPIs funcionando no Raspberry Pi, após treinamento e avaliação científica.
