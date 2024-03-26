import random
import time

Players = []  # array for the total number of players
Moved = []  # array for the total number of players who moved
Static = []  # array for the people who did not move
Eliminated = []
for P in range(1, 457, 1):  # create the number for each player
    Players.append(P)

Round = 0
Stage=0
while Round < 6:
    Stage +=1
    Moved.clear()
    print(" ")
    print(" ")
    Round += 1
    print("Round: #" + str(Stage))
    print("Green Lights")
    Len = 0
    Len = int(len(Players) * 0.8)
    random.shuffle(Players)  # shuffle the players to make them move randomly
    # Green light
    for P in range(0, Len, 1):
        Moved.append(Players[P])  # Move the random Player

    for S in range(len(Moved), len(Players) - 1, 1):
        Static.append(Players[S])
        if S == len(Players):
            Static.pop(S)  # get the players who did not move

    print("Moved: ", end="")
    print(Moved)  # get the players eho moved
    print("Static: ", end="")
    print(Static)  # get the player did not move
    print("Eliminated: None")
    time.sleep(5)
    # Red light
    Round +=1
    print(" ")
    print("Red Lights")

    Static.clear()
    Players.pop(len(Players) - 1)
    Len1 = 0
    Len1 = int(len(Players) * 0.05) + 1

    for E in range(0, Len1, 1):
        Eliminated.append(Moved[E])
    for E in range(len(Eliminated)):
        Players.pop(E)
    Players.pop(len(Players) - 1)

    print("Moved: ", end="")
    print(Moved)  # get the players who moved
    print("Static players: ", end="")
    print(Players)  # get the player did not move
    print("Eliminated: ", end="")
    print(Eliminated)  # get the players who moved
    Eliminated.clear()
    time.sleep(5)