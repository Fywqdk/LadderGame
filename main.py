"""

Created on Tue Jan  5 18:19:50 2021

@author: Fywq/Morten

Ladder game simulator

"""



import random
import pylab

destinations = [ 0,  1,  2,  3, 23,  5,  6,  7,  8,  9,
                10, 11, 12, 27, 14, 15, 16, 17, 18, 19,
                20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                30, 10, 32, 33, 34, 35, 36, 37, 38, 39,
                40, 41, 42, 43, 37, 45, 46, 53, 48, 49,
                50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
                60, 61, 62, 77, 64, 65, 66, 67, 68, 69,
                87, 71, 72, 73, 74, 75, 76, 77, 78, 41,
                80, 81, 98, 83, 84, 85, 86, 87, 88, 89,
                90, 91, 92, 74, 94, 95, 96, 97, 98, 99]

die = [1, 2, 3, 4, 5, 6]


def play_game():
    
    position = 0
    move_count = 0
    moves = []
    
    move_again = True
    game_won = False
    
    while move_again:
        
        roll = random.choice(die)
        
        if position + roll < 99:
            position = destinations[position + roll]
        elif position + roll == 99:
            move_again = False
            game_won = True
            position = destinations[position + roll]
        else:
            position = 198 - (roll + position)

        move_count += 1
        
        if move_count >= 100:
            move_again = False
        else:
            moves.append(roll)
           
    if game_won:
        return True, move_count
    else:
        return False, move_count
             

def simulate(trials):
    
    games_won = []
    games_lost = 0
    
    for i in range(trials):
        result, moves = play_game()
        
        if result:
            games_won.append(moves)
        else:
            games_lost += 1
    

    print("games lost:", games_lost)
    print("shortest win:", min(games_won))


    pylab.hist(games_won, bins=90, label = "Moves")
    pylab.title("Moves to complete game")
    pylab.show()
       

simulate(1000000)
        
