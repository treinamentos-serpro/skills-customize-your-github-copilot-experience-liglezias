# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Aprenda a criar uma API REST com FastAPI, definindo rotas HTTP, validando dados com modelos Pydantic e retornando respostas apropriadas para cada operação.

## 📝 Tarefas

### 🛠️ Inicialize a API e crie uma rota de status

#### Descrição

Use o arquivo `starter-code.py` como ponto de partida. Salve-o como `main.py`, instale FastAPI e Uvicorn e crie uma rota para confirmar que a API está funcionando.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI.
- Responder a `GET /health` com o JSON `{"status": "ok"}`.
- Iniciar com `uvicorn main:app --reload`.
- Disponibilizar a documentação interativa em `/docs`.

### 🛠️ Crie e liste livros

#### Descrição

Crie um modelo de dados para livros e implemente operações para adicionar livros ao catálogo em memória e listar os livros cadastrados.

#### Requisitos
O programa concluído deve:

- Definir um modelo Pydantic `BookCreate` com os campos `title` e `author`, ambos obrigatórios e do tipo texto.
- Implementar `POST /books` para adicionar um livro e retornar seu identificador junto com os dados.
- Responder à criação com o status HTTP `201`.
- Implementar `GET /books` para retornar a lista de livros cadastrados.
- Deixar o FastAPI rejeitar dados inválidos ou campos obrigatórios ausentes com o status HTTP `422`.

Exemplo de corpo para `POST /books`:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien"
}
```

### 🛠️ Consulte um livro por identificador

#### Descrição

Implemente uma rota que localize e retorne um livro específico usando seu identificador na URL.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books/{book_id}`, em que `book_id` é um parâmetro de caminho inteiro.
- Retornar o identificador, o título e o autor quando o livro existir.
- Retornar o status HTTP `404` quando não houver livro com esse identificador.

### 🛠️ Atualize e remova livros

#### Descrição

Complete as operações do catálogo permitindo substituir os dados de um livro existente e removê-lo.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /books/{book_id}` para substituir o título e o autor de um livro existente.
- Retornar o livro atualizado e seu identificador após uma atualização bem-sucedida.
- Implementar `DELETE /books/{book_id}` para remover um livro existente e responder com o status HTTP `204`, sem corpo na resposta.
- Retornar o status HTTP `404` nas operações de atualização ou remoção quando o identificador não existir.
