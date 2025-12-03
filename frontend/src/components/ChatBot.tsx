import axios from 'axios'
import { Heart, Loader2, MessageCircle, Send } from 'lucide-react'
import { useEffect, useRef, useState } from 'react'
import './ChatBot.css'

interface Message {
  id: string
  text: string
  isUser: boolean
  timestamp: Date
}

const API_URL = 'http://localhost:5000/api/question-and-answer'

const SUGGESTED_QUESTIONS = [
  "🐱 Melhor ração premium para gatos?",
  "🐕 Brinquedos para cães grandes?",
  "🍼 Cuidados com filhotes?",
  "💉 Calendário de vacinas?",
  "🦴 Petiscos saudáveis?"
]

const ChatBot = () => {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: '1',
      text: '🐾 **Olá! Sou seu Assistente Pet!**\n\n🤖 **O que posso fazer por você:**\n• Recomendar rações ideais para seu pet\n• Sugerir brinquedos e acessórios\n• Orientar sobre cuidados veterinários\n• Dar dicas de alimentação e bem-estar\n\n💡 **Experimente as sugestões abaixo ou digite sua própria pergunta!**',
      isUser: false,
      timestamp: new Date()
    }
  ])
  const [inputText, setInputText] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    if (messages.length === 1) {
      messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
    } else {
      scrollToBottom()
    }
  }, [messages])

  const sendMessage = async (text: string) => {
    if (!text.trim() || isLoading) return

    const userMessage: Message = {
      id: Date.now().toString(),
      text: text.trim(),
      isUser: true,
      timestamp: new Date()
    }

    setMessages(prev => [...prev, userMessage])
    setInputText('')
    setIsLoading(true)

    try {
      const response = await axios.post(API_URL, {
        question: text.trim()
      }, {
        headers: {
          'Content-Type': 'application/json'
        }
      })

      const assistantMessage: Message = {
        id: (Date.now() + 1).toString(),
        text: response.data.response.trim(), // Remove espaços extras
        isUser: false,
        timestamp: new Date()
      }

      setMessages(prev => [...prev, assistantMessage])
    } catch (error) {
      console.error('Erro ao enviar mensagem:', error)

      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        text: 'Desculpe, ocorreu um erro. Verifique se a API está rodando em http://localhost:5000',
        isUser: false,
        timestamp: new Date()
      }

      setMessages(prev => [...prev, errorMessage])
    } finally {
      setIsLoading(false)
    }
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    sendMessage(inputText)
  }

  const handleSuggestedQuestion = (question: string) => {
    sendMessage(question)
  }

  const clearChat = () => {
    setMessages([
      {
        id: '1',
        text: '🐾 **Olá! Sou seu Assistente Pet!**\n\n🤖 **O que posso fazer por você:**\n• Recomendar rações ideais para seu pet\n• Sugerir brinquedos e acessórios\n• Orientar sobre cuidados veterinários\n• Dar dicas de alimentação e bem-estar\n\n💡 **Experimente as sugestões abaixo ou digite sua própria pergunta!**',
        isUser: false,
        timestamp: new Date()
      }
    ])
  }

  return (
    <div className="chatbot-container">
      <div className="chatbot-header">
        <MessageCircle className="header-icon" />
        <h2>Assistente Pet</h2>
        <button onClick={clearChat} className="clear-button">
          Limpar
        </button>
      </div>

      <div className="messages-container">
        {messages.map((message) => (
          <div
            key={message.id}
            className={`message ${message.isUser ? 'user-message' : 'assistant-message'}`}
          >
            <div className="message-content">
              <p>{message.text}</p>
              <span className="message-time">
                {message.timestamp.toLocaleTimeString('pt-BR', {
                  hour: '2-digit',
                  minute: '2-digit'
                })}
              </span>
            </div>
          </div>
        ))}

        {isLoading && (
          <div className="message assistant-message">
            <div className="message-content loading">
              <Loader2 className="loading-icon" />
              <p>Pensando...</p>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      {messages.length === 1 && (
        <div className="suggestions-container">
          <p className="suggestions-title">💡 Perguntas sugeridas para começar:</p>
          <div className="suggestions-grid">
            {SUGGESTED_QUESTIONS.map((question, index) => (
              <button
                key={index}
                onClick={() => handleSuggestedQuestion(question)}
                className="suggestion-button"
                disabled={isLoading}
              >
                {question}
              </button>
            ))}
          </div>
        </div>
      )}

      <form onSubmit={handleSubmit} className="input-form">
        <div className="input-container">
          <input
            type="text"
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            placeholder="Digite sua pergunta sobre pets..."
            className="message-input"
            disabled={isLoading}
          />
          <button
            type="submit"
            disabled={isLoading || !inputText.trim()}
            className="send-button"
          >
            {isLoading ? (
              <Loader2 className="button-icon loading" />
            ) : (
              <Send className="button-icon" />
            )}
          </button>
        </div>
      </form>

      <div className="footer">
        <p>
          <Heart className="heart-icon" />
          Desenvolvido com amor para pets
        </p>
      </div>
    </div>
  )
}

export default ChatBot