import './App.css'
import ChatBot from './components/ChatBot'

function App() {
  return (
    <div className="app">
      <header className="app-header">
        <h1>🐾 PetLove Assistant</h1>
        <p>Seu assistente especialista em produtos para pets</p>
      </header>
      <main className="app-main">
        <ChatBot />
      </main>
    </div>
  )
}

export default App
