# 📘 Atividade: Organizador de Arquivos com Python

## 🎯 Objetivo

Pratique automação e organização de dados usando o sistema de arquivos do Python. Você vai classificar arquivos por extensão, planejar sua organização e movê-los com segurança usando apenas a biblioteca padrão.

## 📝 Tarefas

### 🛠️ Identifique e classifique arquivos

#### Descrição

Use o arquivo `starter-code.py` como ponto de partida e crie uma pasta `sample-files` com cópias de arquivos de teste. Percorra os arquivos dessa pasta e determine uma categoria para cada um com base em sua extensão.

#### Requisitos
O programa concluído deve:

- Usar `pathlib.Path` para acessar a pasta de teste e percorrer seus arquivos.
- Ignorar subpastas e classificar somente arquivos.
- Normalizar a extensão para minúsculas, para que `.JPG` e `.jpg` pertençam à mesma categoria.
- Agrupar arquivos sem extensão em uma categoria chamada `sem_extensao`.
- Organizar os resultados de forma determinística, por exemplo, ordenando os nomes antes de exibi-los.

### 🛠️ Gere uma prévia da organização

#### Descrição

Planeje o destino de cada arquivo sem alterar a pasta de origem. Os arquivos devem ser separados em subpastas pelo nome da categoria.

#### Requisitos
O programa concluído deve:

- Planejar destinos no formato `organized-files/<categoria>/<nome-do-arquivo>`.
- Exibir cada origem e seu destino planejado.
- Operar em modo de prévia: nesta etapa, não deve criar pastas nem mover ou alterar arquivos.
- Informar claramente quando não houver arquivos para organizar.

### 🛠️ Confirme e execute a organização

#### Descrição

Complete o programa para executar o plano somente após uma confirmação explícita. Faça todos os testes usando arquivos de exemplo em `sample-files`, nunca em pastas pessoais ou em arquivos importantes.

#### Requisitos
O programa concluído deve:

- Pedir confirmação antes de mover qualquer arquivo; qualquer resposta diferente de `s` deve cancelar a operação sem alterações.
- Criar as pastas de destino necessárias e mover os arquivos usando `shutil`.
- Não sobrescrever arquivos existentes no destino; ignorar conflitos e informar quais foram pulados.
- Exibir um resumo com a quantidade de arquivos movidos e ignorados.
