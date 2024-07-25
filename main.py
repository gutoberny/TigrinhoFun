from game import Game

new_game = Game(slots=[])

jogos = [0] * 100

derrotas = 0
horizontais = 0
diagonais = 0

for j in jogos:
    new_game.girar_roleta()
    new_game.desenhar()
    result = new_game.verificar()

    if not result: 
        derrotas += 1
    elif result.startswith('horizontal'):
        horizontais += 1
    elif result.startswith('diagonal'):
        diagonais += 1

    print("")
    
print("Jogos: ", len(jogos))
print("Derrotas: ", derrotas)
print("Vitorias nas Horizontais: ", horizontais)
print("Vitorias nas Diagonais: ", diagonais)