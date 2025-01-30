import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Card, CardContent } from "@/components/ui/card"
import { Gamepad2, Swords, Trophy } from "lucide-react"

const characters = [
  { id: 1, name: "Ryu", image: "/placeholder.svg?height=100&width=100" },
  { id: 2, name: "Chun-Li", image: "/placeholder.svg?height=100&width=100" },
  { id: 3, name: "Guile", image: "/placeholder.svg?height=100&width=100" },
  { id: 4, name: "Blanka", image: "/placeholder.svg?height=100&width=100" },
]

export default function GameInterface() {
  const [selectedCharacter, setSelectedCharacter] = useState<number | null>(null)

  return (
    <div className="min-h-screen bg-gradient-to-b from-purple-900 to-indigo-900 text-white p-8">
      <header className="text-center mb-8">
        <h1 className="text-4xl font-bold mb-4 pixel-font">Super Combo Fighter</h1>
        <div className="flex justify-center space-x-6">
          <Button
            variant="outline"
            className="pixel-button rounded-full w-16 h-16 flex flex-col items-center justify-center p-0"
          >
            <Gamepad2 className="h-6 w-6 mb-1" />
            <span className="text-xs">Jugar</span>
          </Button>
          <Button
            variant="outline"
            className="pixel-button rounded-full w-16 h-16 flex flex-col items-center justify-center p-0"
          >
            <Trophy className="h-6 w-6 mb-1" />
            <span className="text-xs">Ranking</span>
          </Button>
          <Button
            variant="outline"
            className="pixel-button rounded-full w-16 h-16 flex flex-col items-center justify-center p-0"
          >
            <Swords className="h-6 w-6 mb-1" />
            <span className="text-xs">Versus</span>
          </Button>
        </div>
      </header>

      <main>
        <h2 className="text-2xl font-bold mb-4 text-center pixel-font">Selecciona tu luchador</h2>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {characters.map((character) => (
            <Card
              key={character.id}
              className={`cursor-pointer transition-all duration-300 transform hover:scale-105 ${
                selectedCharacter === character.id ? "ring-4 ring-yellow-400" : ""
              }`}
              onClick={() => setSelectedCharacter(character.id)}
            >
              <CardContent className="p-4 text-center">
                <img
                  src={character.image || "/placeholder.svg"}
                  alt={character.name}
                  className="w-24 h-24 mx-auto mb-2 pixel-image"
                />
                <p className="font-bold pixel-font">{character.name}</p>
              </CardContent>
            </Card>
          ))}
        </div>
      </main>

      <footer className="mt-8 text-center">
        <Button variant="default" size="lg" className="pixel-button" disabled={!selectedCharacter}>
          ¡Luchar!
        </Button>
      </footer>

      <style>{`
        @font-face {
          font-family: 'PixelFont';
          src: url('/path-to-pixel-font.woff2') format('woff2');
        }
        .pixel-font {
          font-family: 'PixelFont', monospace;
          letter-spacing: 1px;
        }
        .pixel-button {
          image-rendering: pixelated;
          box-shadow: 0 4px 0 #000;
          color: #FFD700; /* Cambia el color de la fuente a dorado */
          border-color: #FFD700; /* Cambia el color del borde a dorado */
        }
        .pixel-button:hover {
          background-color: rgba(255, 215, 0, 0.1); /* Añade un efecto hover */
        }
        .pixel-button:active {
          transform: translateY(4px);
          box-shadow: none;
        }
        .pixel-image {
          image-rendering: pixelated;
        }
      `}</style>
    </div>
  )
}

