import random
import time 
import os 


bullet = [True,False]
players = []
winner_not_decided = True
HEARTS = 5
game_over = False
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def addplayer():
    name = input("Enter Player Name ")
    player = Player(name)
    players.append(player)

def move_to_next_player(ind):
    if ind == no_of_players_alive - 1:
            ind = 0
    elif 0 <= ind < no_of_players_alive - 1:
            ind += 1
    current_player = players[ind]
    return current_player,ind

class Player:
    def __init__(self, name): 
        self.utilities = {}
        self.name = name
        self.hearts = HEARTS

    def shoot(self,inde):
        global no_of_players_alive, winner_not_decided, current_player, ind
        #clear_screen()
        print("choose the player to shoot: ")
        for player in players:
            print(player.name, players.index(player))
            print(player.hearts * " ❤︎ " )
        player_to_shoot = int(input(f"which head to shoot {player.name}?? Enter the number after the player name ?"))
        print(players[inde].name, "shot", players[player_to_shoot].name)
        if gun[0]:
            player = players[player_to_shoot]
            player.hearts = player.hearts - 1 
            print("It was a LIVE !! Bullet ")
            if player.hearts == 0:
                print(player.name,"IS DEAD !!")
                players.remove(player)
                no_of_players_alive -= 1
                
                if no_of_players_alive == 1:
                    print("Only one man left... The Crown is Claimed By: ")
                    game_over == True                
                    winner_not_decided = False
            spl_cond = False
            
        else:
            print("It was a FAKE.. bullet")
            if inde == player_to_shoot:
                spl_cond = True
                print("Its your chance again ", players[inde].name)   
            else:
                spl_cond = False  
        if not game_over: 
            if not spl_cond:      
                if ind == no_of_players_alive - 1:
                    ind = 0
                elif 0 <= ind < no_of_players_alive - 1:
                    ind += 1
            current_player = players[ind]
        else:
            print("Congratulations", players[0].name, "You won the game")
        gun.pop(0)

    def show_abilities(self):
        print("abilities")
        
print("---------------Welcome to BUCKSHOT---------------")

# Computer gets to know About how many players are playing and cross checks valid no of players that can play 
no_of_players = int(input("How many players are going to play ? (2/3/4)"))
no_of_players_alive = no_of_players
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
gun=[]
rounds = 1
start_of_game = True
while winner_not_decided:
    if start_of_game:
        current_player = decide_starting_player()
        ind = players.index(current_player)
        start_of_game = False

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
        sp_cond = current_player.shoot(ind)
    elif decision == 2:
        current_player.show_abilities()
    elif decision == 3:
        current_player = move_to_next_player()
        
        #clear_screen()
    