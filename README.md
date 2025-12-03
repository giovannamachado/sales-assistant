# 🐾 Pet Sales Assistant

> **Assistente de vendas inteligente com IA para e-commerce de produtos pet**

## 📋 Sobre o Projeto

Este é um **assistente de vendas especializado** que utiliza inteligência artificial para responder perguntas sobre produtos para pets. A aplicação integra-se com modelos de linguagem avançados da **Groq AI** para oferecer recomendações personalizadas sobre:

- 🐕 **Rações ideais** para diferentes raças e idades
- 🧸 **Brinquedos e acessórios** seguros e adequados
- 💊 **Cuidados veterinários** e calendário de vacinas
- 🏥 **Bem-estar animal** e dicas de saúde

### ✨ Principais características:

- **API REST** desenvolvida com Flask
- **Fallback automático** entre 6 modelos de IA da Groq
- **Interface web moderna** com React + TypeScript
- **Respostas educativas** formatadas e contextualizadas
- **CORS habilitado** para integração frontend

---

## 🚀 Como Executar o Backend

### Pré-requisitos

- Python 3.8+
- Conta gratuita na Groq AI

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/sales-assistant.git
cd sales-assistant
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure a chave da API

1. Acesse [console.groq.com/keys](https://console.groq.com/keys)
2. Crie uma conta gratuita (se não tiver)
3. Gere uma nova chave de API
4. Crie um arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=sua_chave_da_groq_aqui
```

### 4. Execute a API

```bash
python app.py
```

**⚠️ Importante:** Esta é uma API REST que só aceita requisições POST. Não há interface web no navegador - você deve usar ferramentas como cURL, Postman ou um cliente HTTP para testá-la.

---

## 🧪 Como Testar a API

A API não possui interface web. Para testá-la, você precisa fazer requisições HTTP POST. Aqui estão as formas de testar:

### Método 1: Usando cURL

Abra um **novo terminal** (deixe a API rodando no primeiro) e execute:

```bash
$response = Invoke-RestMethod -Uri "http://localhost:5000/api/question-and-answer" -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"question":"Que brinquedos são bons para cães?"}'; $response | ConvertTo-Json -Depth 10
```

### Método 2: Usando Postman

1. Abra o Postman
2. Configure:
   - **Método:** POST
   - **URL:** `http://localhost:5000/api/question-and-answer`
   - **Headers:** `Content-Type: application/json`
   - **Body (raw JSON):**
   ```json
   {
     "question": "qual a melhor ração para golden?"
   }
   ```

## 📡 Documentação da API

### **POST** `/api/question-and-answer`

**⚠️ Atenção:** Este endpoint só aceita requisições POST com JSON. Acessar pelo navegador resultará em erro "Method Not Allowed".

Endpoint principal que recebe perguntas sobre produtos pet e retorna respostas inteligentes.

#### Request

```json
{
    "question": "qual a melhor ração para golden?"
}
```

#### Response

```json
{
    "response": "🐕 **Para Golden Retrievers, recomendo rações premium específicas para a raça!**\n\n🏆 **Melhores opções:**\n• Royal Canin Golden Retriever - Fórmula específica para pele e pelagem\n• Premier Pet Golden - Rico em ômega 3 e 6\n• Premiatta Golden - Proteínas de alta qualidade\n\n💡 **Dica:** Escolha sempre rações com carne como primeiro ingrediente!"
}
```

#### Códigos de resposta:

- `200` - Sucesso
- `400` - Erro na requisição (JSON inválido ou campo ausente)
- `405` - Método não permitido (use POST, não GET)
- `500` - Erro interno do servidor

---

## 🛠️ Tecnologias

### Backend

- **Flask** - Framework web Python
- **Groq AI** - API de inteligência artificial
- **python-dotenv** - Gerenciamento de variáveis de ambiente
- **requests** - Cliente HTTP

---

## 🔧 Recursos Avançados

### Fallback de Modelos
A API possui fallback automático entre 6 modelos diferentes da Groq para garantir alta disponibilidade:
- `llama-3.3-70b-versatile`
- `llama3-groq-70b-8192-tool-use-preview`
- `llama3-groq-8b-8192-tool-use-preview`
- `llama-3.1-8b-instant`
- `gemma2-9b-it`
- `gemma-7b-it`

### CORS Habilitado
A API possui CORS configurado para permitir requisições do frontend.

### Validações Robustas
- Validação de Content-Type
- Verificação de campos obrigatórios
- Tratamento de erros com timeouts

---

## 🎨 Frontend (Bonus)

O projeto também inclui uma interface web moderna desenvolvida com **React + TypeScript + Vite**.

### Como executar o Frontend

#### Pré-requisitos
- Node.js 16+
- npm ou yarn

#### 1. Navegue até a pasta do frontend
```bash
cd frontend
```

#### 2. Instale as dependências
```bash
npm install
```

#### 3. Execute o servidor de desenvolvimento
```bash
npm run dev
```

✅ **O frontend estará disponível em:** `http://localhost:5173`



### 🌟 Funcionalidades do Frontend

- 💬 Interface de chat intuitiva
- 🎯 Sugestões de perguntas pré-definidas
- 📱 Design responsivo
- 🎨 Tema moderno com gradientes
- ⚡ Carregamento em tempo real

### Frontend - Tecnologias

- **React 18** - Library de interface
- **TypeScript** - Tipagem estática
- **Vite** - Build tool moderna
- **Axios** - Cliente HTTP
- **Lucide React** - Ícones modernos

---


<div align="center">

**🐾 Desenvolvido com amor para pets! 🐾**
