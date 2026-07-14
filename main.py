import random
import time 
import os 


bullet = [True,False]
players = []
winner_not_decided = True
HEARTS = 5

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def addplayer():
    name = input("Enter Player Name ")
    player = Player(name)
    players.append(player)


class Player:
    def __init__(self, name): 
        self.utilities = {}
        self.name = name
        self.hearts = HEARTS

    def shoot(self):
        print("bullet shot")

    def show_abilities(self):
        print("abilities")
        
        

print("---------------Welcome to BUCKSHOT---------------")

# Computer gets to know About how many players are playing and cross checks valid no of players that can play 
no_of_players = int(input("How many players are going to play ? (2/3/4)"))
while no_of_players not in (2,3,4):
    clear_screen()
    print("Sorry!! Only (2/3/4) players can play this game")
    no_of_players = int(input("How many players are going to play ? (2/3/4)"))

# Based on number of players creates a player profile 
for player_entry in range(no_of_players):
    addplayer()
    if player_entry != no_of_players - 1:
        print(" Please pass the device to the next player ")
        time.sleep(1)
        #clear_screen()
    else:
        print("Let Everyone see the screen now !")
        time.sleep(1)

    
max_bullet = int(round(2.5*no_of_players,0))
min_bullet = max_bullet-2


def load_gun():
    '''
    Takes the no of players and calculates how many live bullets and fake bullets should be loaded into the gun and it loads up the gun
    '''
    global gun
    gun = []
    max_bullet = round(no_of_players * 2.8)
    no_of_bullets = random.randint(5,max_bullet)
    no_of_live_bullets = no_of_bullets / 2 
    for _ in range(no_of_bullets):
        
        if no_of_live_bullets > 0:
            gun.append(bullet[0])
            no_of_live_bullets -= 1
        else:
            gun.append(bullet[1])
    random.shuffle(gun)

def decide_starting_player():
    st_player = random.choice(players)
    return st_player

rounds = 1
start_of_game = True
while winner_not_decided:
    if start_of_game:
        current_player = decide_starting_player()
        ind = players.index(current_player)
        start_of_game = False

    
    gun=[]
    if len(gun) == 0:
        print("Round : ",rounds)
        print("Loading Gun .................. ")
        load_gun()
        time.sleep(1)
        #clear_screen()
        print("Gun Loaded !! ")
        print("Live Bullets =",gun.count(True))
        print("Fake Bullets =",gun.count(False))
        rounds +=1

    print("PLayer",current_player.name,"Make a Move")
    decision = int(input("1.Kill\n2.Use\n3.End my move\n"))
    if decision == 1:
        current_player.shoot()
    elif decision == 2:
        current_player.show_abilities()
    elif decision == 3:
        if ind == no_of_players - 1:
            ind = 0
        elif 0 <= ind < no_of_players - 1:
            ind += 1
        current_player = players[ind]
        #clear_screen()
    