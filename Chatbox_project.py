import { useState, useRef, useEffect } from 'react'
import { Input } from "/components/ui/input"
import { Button } from "/components/ui/button"
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "/components/ui/card"
import { Send } from 'lucide-react'

type Message = {
  text: string
  sender: 'user' | 'bot'
  timestamp: Date
}

const botResponses: Record<string, string> = {
  'hello': 'Hi there! How can I help you today?',
  'hi': 'Hello! What can I do for you?',
  'how are you': "I'm just a bot, but I'm functioning well! How about you?",
  'what can you do': 'I can respond to simple greetings and questions. Try asking me "hello" or "how are you"!',
  'bye': 'Goodbye! Have a great day!',
  'default': "I'm not sure how to respond to that. Try asking me something else!"
}

export default function SimpleChatbot() {
  const [inputValue, setInputValue] = useState('')
  const [messages, setMessages] = useState<Message[]>([
    {
      text: 'Hello! I am a simple chatbot. Try saying "hello" or "how are you" to start.',
      sender: 'bot',
      timestamp: new Date()
    }
  ])
  const messagesEndRef = useRef<HTMLDivElement>(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const handleSendMessage = () => {
    if (!inputValue.trim()) return

    // Add user message
    const userMessage: Message = {
      text: inputValue,
      sender: 'user',
      timestamp: new Date()
    }
    setMessages(prev => [...prev, userMessage])
    setInputValue('')

    // Generate bot response after a short delay
    setTimeout(() => {
      const userInput = inputValue.toLowerCase().trim()
      let botResponse = botResponses.default

      // Check for matching responses
      for (const [key, value] of Object.entries(botResponses)) {
        if (userInput.includes(key)) {
          botResponse = value
          break
        }
      }

      const botMessage: Message = {
        text: botResponse,
        sender: 'bot',
        timestamp: new Date()
      }
      setMessages(prev => [...prev, botMessage])
    }, 500)
  }

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      handleSendMessage()
    }
  }

  const formatTime = (date: Date) => {
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
  }

  return (
    <Card className="w-full max-w-md mx-auto h-[600px] flex flex-col">
      <CardHeader>
        <CardTitle className="text-xl">Simple Chatbot</CardTitle>
      </CardHeader>
      <CardContent className="flex-grow overflow-y-auto space-y-4">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`flex ${message.sender === 'user' ? 'justify-end' : 'justify-start'}`}
          >
            <div
              className={`max-w-xs md:max-w-md rounded-lg px-4 py-2 ${message.sender === 'user' 
                ? 'bg-primary text-primary-foreground' 
                : 'bg-muted'}`}
            >
              <p>{message.text}</p>
              <p className={`text-xs mt-1 ${message.sender === 'user' ? 'text-primary-foreground/70' : 'text-muted-foreground'}`}>
                {formatTime(message.timestamp)}
              </p>
            </div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </CardContent>
      <CardFooter className="flex gap-2">
        <Input
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Type a message..."
          className="flex-grow"
        />
        <Button onClick={handleSendMessage} disabled={!inputValue.trim()}>
          <Send className="h-4 w-4" />
        </Button>
      </CardFooter>
    </Card>
  )
}