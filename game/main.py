import random

# chois = ["Piedra", "Papel","Tijera" ] 
# playerwins = 0
# botwins = 0
# ronda = 1


# while ronda < 11:    
#     Randomizer = random.randint(0, 2)
#     bot = chois[Randomizer]
#     player = chois[int(input("Que eliges 0 Piedra, 1 Papel o 2 Tijera --> "))]
    
#     if player == chois[0] and bot == chois[1] or player == chois[1] and bot == chois[2] or player == chois[2] and bot == chois[0]:
#         botwins = botwins + 1
#         print("*************************************")
#         print(f"           ROUND {ronda}            ")
#         print("*************************************")
#         print(f" Victorias = {playerwins}   Derrotas = {botwins}")
#         print(f" tu elegiste {player} y el bot {bot}")
#         print("Perdiste")

        
#     elif player == bot:
#         print("*************************************")
#         print(f"           ROUND {ronda}            ")
#         print("*************************************")
#         print(f" Victorias = {playerwins}   Derrotas = {botwins}")
#         print(f" tu elegiste {player} y el bot {bot}")
#         print("Empate")


#     else:
#         playerwins = playerwins + 1
#         print("*************************************")
#         print(f"           ROUND {ronda}            ")
#         print("*************************************")
#         print(f" Victorias = {playerwins}   Derrotas = {botwins}")
#         print(f" tu elegiste {player} y el bot {bot}")
#         print("Ganaste")
#     ronda = ronda + 1
    


def final(playerwinsy,botwinsy,ronday):
    chois = ["Piedra", "Papel","Tijera" ] 
    Randomizer = random.randint(0, 2)
    bot = chois[Randomizer]
    player = chois[int(input("Que eliges 0 Piedra, 1 Papel o 2 Tijera --> "))]
    playerwins = playerwinsy
    botwins = botwinsy
    ronda = ronday
    
    if player == chois[0] and bot == chois[1] or player == chois[1] and bot == chois[2] or player == chois[2] and bot == chois[0]:
        botwins = botwins + 1
        print("*************************************")
        print(f"           ROUND {ronda}            ")
        print("*************************************")
        print(f" Victorias = {playerwins}   Derrotas = {botwins}")
        print(f" tu elegiste {player} y el bot {bot}")
        print("Perdiste")

        
    elif player == bot:
        print("*************************************")
        print(f"           ROUND {ronda}            ")
        print("*************************************")
        print(f" Victorias = {playerwins}   Derrotas = {botwins}")
        print(f" tu elegiste {player} y el bot {bot}")
        print("Empate")

    else:
        playerwins = playerwins + 1
        print("*************************************")
        print(f"           ROUND {ronda}            ")
        print("*************************************")
        print(f" Victorias = {playerwins}   Derrotas = {botwins}")
        print(f" tu elegiste {player} y el bot {bot}")
        print("Ganaste")
    ronda = ronda + 1

        
    return reinicio(playerwins,botwins,ronda)

def reinicio(playerwinsy,botwinsy,ronday  ):
    playerwins = playerwinsy
    botwins = botwinsy
    ronda = ronday
    return final(playerwins,botwins,ronda)



reinicio(0,0,1)