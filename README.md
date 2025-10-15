# Sales Assistant API

API de assistente de vendas para e-commerce de produtos pet, integrada com Groq AI.

## Sobre o Projeto

Esta API foi desenvolvida para servir como assistente de vendas da Petlove, respondendo perguntas sobre produtos para cães e gatos usando inteligência artificial.

## Como executar

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Configurar variável de ambiente
Crie um arquivo `.env`:
```
GROQ_API_KEY=sua_chave_aqui
```
Obtenha uma chave gratuita em: https://console.groq.com/keys

### 3. Executar a API
```bash
python app.py
```

A API estará disponível em: http://localhost:5000

## Endpoint

### POST /api/question-and-answer

Recebe uma pergunta sobre produtos pet e retorna a resposta da IA.

**Request:**
```json
{
    "question": "qual a melhor ração para golden?"
}
```

**Response:**
```json
{
    "response": "Escolher a melhor ração para um Golden Retriever envolve considerar a qualidade dos ingredientes..."
}
```

### Exemplo de uso

```bash
curl --location 'http://localhost:5000/api/question-and-answer' \
--header 'Content-Type: application/json' \
--data '{
    "question": "qual a melhor ração para golden?"
}'
```

## Tecnologias

- Flask (Python)
- Groq AI
- python-dotenv