import random
import time
Players = []  # array for the total number of players
Moved = []  # array for the total number of players who moved
Static = []  # array for the people who did not move
Eliminated = []
Winners = []
Win = []

Val = 0
for P in range(1, 457, 1):  # create the number for each player
    Players.append(P)

Round = 0
while Round < 6:
    Static.clear()
    Moved.clear()
    print(" ")
    print(" ")
    Round += 1
    print("Round: #" + str(Round))
    print("Green Lights")
    time.sleep(5)

    Len = int(len(Players) * 0.8)
    random.shuffle(Players)  # shuffle the players to make them move randomly

    # Green light
    for P in range(0, Len, 1):
        Moved.append(Players[P])   # Move the random Player

    for S in range(len(Moved), len(Players) - 1, 1):
        Static.append(Players[S])
     
    print("Moved: ", end="")
    print(Moved)  # get the players eho moved
    print("Static: ", end="")
    print(Static)  # get the player did not move
    print("Eliminated: None")
    Winners.clear()
    Winners = Moved
    # Red light
    print(" ")
    Round += 1
    print("Round: #" + str(Round))
    print("Red Lights")
    time.sleep(5)
    Static.clear()
    Moved.clear()
    random.shuffle(Players)

    Len1 = int(len(Players) * 0.05) + 1
    for M in range(0, Len1, 1):
        Moved.append(Players[M])  # get the players who moved
        Eliminated.append(Moved[M])   # get the eliminated players
        Players.pop(M)  # remove the eliminated players from the players array

    for S in range(Len1, len(Players), 1):
        Static.append(Players[S])  # get the players who did not move
    print("Moved: ", end="")
    print(Moved)  # get the players who moved
    print("Static players: ", end="")
    print(Static)  # get the player did not move
    print("Eliminated: ", end="")
    print(Eliminated)  # get the players who moved
    Eliminated.clear()
    Moved.sort()
    Winners.sort()
    for W in range(0, len(Winners) , 1):
        for M in range(0,len(Moved) , 1):
            if not Winners[W] == Moved[M]:
                Win.append(Moved[W]) # remove
            elif Win.__contains__(Moved[M]):
                break

Wins = []
for S in Win:
    if S not in Wins:
        Wins.append(S)
print("The winners are:", end=" ")
print(Wins)