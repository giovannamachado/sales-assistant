# Sales Assistant API

API de assistente de vendas especializada em produtos para pets (cães e gatos), integrada com Groq AI.

## 📋 Sobre o Projeto

Esta API funciona como um assistente de vendas inteligente para e-commerce de produtos pet. Ela recebe perguntas sobre produtos para cães e gatos e retorna respostas especializadas usando IA, ajudando clientes a encontrarem os melhores produtos para seus pets.

**Principais funcionalidades:**
- Endpoint `/api/question-and-answer` para perguntas sobre produtos pet
- Integração com Groq AI (modelos Llama 3)
- Sistema resiliente com fallback automático entre modelos
- Respostas especializadas em produtos para cães e gatos

## 🚀 Como executar

### 1. Pré-requisitos
- Python 3.8+
- Chave da API Groq (gratuita)

### 2. Instalação
```bash
# Clone o repositório
git clone <url-do-repositorio>
cd sales-assistant

# Instale as dependências
pip install -r requirements.txt
```

### 3. Configuração
Crie um arquivo `.env` na raiz do projeto:
```bash
GROQ_API_KEY=sua_chave_aqui
```

**Para obter uma chave gratuita:** https://console.groq.com/keys

### 4. Executar a API
```bash
python app.py
```

A API estará disponível em: http://localhost:5000

## 📡 Como usar

### Endpoint principal
```bash
POST /api/question-and-answer
Content-Type: application/json

{
  "question": "qual a melhor ração para golden retriever?"
}
```

### Exemplo com PowerShell
```powershell
Invoke-RestMethod -Uri "http://localhost:5000/api/question-and-answer" -Method Post -Headers @{ "Content-Type" = "application/json" } -Body '{"question": "qual a melhor ração para golden?"}'
```

### Exemplo com cURL
```bash
curl -X POST http://localhost:5000/api/question-and-answer \
  -H "Content-Type: application/json" \
  -d '{"question": "qual a melhor ração para golden?"}'
```

## 🛠️ Tecnologias

- **Flask** - Framework web Python
- **Groq AI** - API de IA com modelos Llama 3
- **python-dotenv** - Gerenciamento de variáveis de ambiente
- **requests** - Cliente HTTP