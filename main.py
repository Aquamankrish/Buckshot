import random
import time 
import os 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def addplayer():
    name = input("Enter Player Name ")
    player = Player(name)
    players.append(player)

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

def check_death(player_shot):
    global winner_not_decided,no_of_players_alive,ind
    if player_shot.hearts == 0:
        print(player_shot.name,"IS DEAD !!")
        players.remove(player_shot)
        no_of_players_alive -= 1
        if no_of_players_alive == 1:
            print("Only one man left...")
            winner_not_decided = False
        return True
    return False
            
def rotate_player(player_killed=False):
    global spl_cond,current_player,ind,no_of_players_alive
    if winner_not_decided: 
        if not spl_cond and not player_killed:      
            print("before",players[ind].name)
            if ind == no_of_players_alive - 1:
                ind = 0
            elif 0 <= ind < no_of_players_alive - 1:
               ind += 1
            current_player = players[ind]
            print("after",players[ind].name)

    else:
        print("Congratulations", players[0].name, "You won the game")
class Player:
    def __init__(self, name): 
        self.abilities = {}
        self.ability_left = True
        self.name = name
        self.hearts = HEARTS

    def shoot(self):
        global no_of_players_alive, winner_not_decided, spl_cond, power_of_shot,ind
        #clear_screen()
        print("choose the player to shoot: ")
        for player in players:
            print(player.name, players.index(player),end = "-" * 5)
            print(player.hearts * " ❤︎ " )
        player_to_shoot = int(input(f"which head to shoot {current_player.name}?? Enter the number after the player name ?"))
        try:
            print(players[ind].name, "shot", players[player_to_shoot].name)
            player_shot = players[player_to_shoot]
            if gun[0]:   
                player_shot.hearts = player_shot.hearts - power_of_shot 
                power_of_shot = 1
                print("It was a LIVE !! Bullet ")
                print(player_shot.hearts * " ❤︎ " )
                spl_cond = False
            else:
                print("It was a FAKE.. bullet")
                if ind == player_to_shoot:
                    spl_cond = True
                    print("Its your chance again ", players[ind].name)   
                else:
                    spl_cond = False  
            player_killed=check_death(player_shot)
            rotate_player(player_killed)
            gun.pop(0)
        except IndexError:
            print("Please Enter Valid number after the player name")
            current_player.shoot()

    def show_abilities(self):
        if not len(current_player.abilities) == 0:
            for ab in current_player.abilities:
                print(ab, sep= " " * 5) 
            ability_decision_ind = input("enter the number before the ability id ")
            ability_list = list(current_player.abilities.keys())
            index_ability_list = [_[0] for _ in ability_list]
            if ability_decision_ind in index_ability_list:
                current_player.abilities[ability_list[int(ability_decision_ind)]]()
                current_player.abilities.pop(ability_list[int(ability_decision_ind)])
                update_ability(current_player)
            else:
                print("Please enter valid ability id")
        else:
            print("You Ran out of Abilities") 
            self.ability_left = False   


def use_magnify_glass():
    print("Using magnifying glass")
    if gun[-1]:
        print("Live bulltet")
    else:
        print("Fake bullet")
def use_hand_saw():
    global power_of_shot
    power_of_shot = 2
    print("Power increased -=>|")
def drink_beer():
    if gun[-1]:
        print("Ejected Live bulltet")
    else:
        print("Ejected Fake bullet")
    gun.pop()
def use_cigar():
    current_player.hearts+=1
    print("{current_player.name} used Beer")
    print(current_player.hearts * " ❤︎ ")
def call_hacker():
    round_len = len(gun_round)
    revealed_list = []
    random_bullet_index = random.randrange(0, round_len)
    while random_bullet_index in revealed_list and len(revealed_list) != round_len:
        random_bullet_index = random.randrange(0, round_len)
    else:          
        revealed_list.append(random_bullet_index)
        if gun_round[random_bullet_index]:
                print(random_bullet_index+1, "is a LIVE Bullet")
        else:
                print(random_bullet_index+1, "is a FAKE Bullet")
def inverter():
    for bi in range(len(gun)):
        if gun[bi]:
            gun[bi] = False
        else:
            gun[bi] = True
    print("Inverting the bullets")
def drink_medicine():
    lucky = bool(random.randint(0,1))
    if lucky:
        current_player.hearts+=2
        print("{current_player.name} drank medicine... LUCKY")    
    else:
        current_player.hearts-=1
        print("{current_player.name} drank medicine... UNFORTUNATE")
    print(current_player.hearts * " ❤︎ ")       
def use_adrenaline():
    print("used adrenaline")
def use_handcuff():
    print("handcuffed player")
abilities = {
    "Magnifying Glass": use_magnify_glass,
    "Hand Saw" : use_hand_saw,
    "Handcuffs" : use_handcuff,
    "Beer" : drink_beer,
    "Cigarette Pack" : use_cigar,
    "Hacker Phone" : call_hacker,
    "Inverter" : inverter,
    "Expired Medicine" : drink_medicine,
    "Adrenaline" : use_adrenaline
}

def generate_ability():
    for player in players:
        player.ability_left = True
        ability_index = 0
        for _ in range(3):
            if len(player.abilities) < 8:
                key,value = random.choice(list(abilities.items()))
                count_of_item = list(player.abilities.values()).count(value) 
                key = f"{str(ability_index)} <=- {key} {str(count_of_item)}"                
                player.abilities[key] = value
                ability_index += 1
        if not( len(player.abilities) <= 3):
            update_ability(player)
    print("Each player has recieved their special items to use ")

def update_ability(player):
    ability_index = 0
    new_ability_dict={}
    for key,val in player.abilities.items():
        #count_of_item = len([k for k in player.abilities if key in k[:-1]])
        count_of_item = list(player.abilities.values()).count(val)
        new_key = f"{str(ability_index)} {key[2:-2]} {str(count_of_item)}"  
        new_ability_dict[new_key] = val
        ability_index += 1
    player.abilities = new_ability_dict

print("---------------Welcome to BUCKSHOT---------------")

bullet = [True,False]
players = []
winner_not_decided = True
HEARTS = 5
power_of_shot = 1
spl_cond = False

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
        time.sleep(0)
        #clear_screen()
    else:
        print("Let Everyone see the screen now !")
        #time.sleep(1)

    
max_bullet = int(round(2.5*no_of_players,0))
min_bullet = max_bullet-2



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
        generate_ability()
        print("Round : ",rounds)
        print("Loading Gun .................. ")
        load_gun()
        gun_round = gun.copy()
        #time.sleep(1)
        #clear_screen()
        print("Gun Loaded !! ")
        print("Live Bullets =",gun.count(True))
        print("Fake Bullets =",gun.count(False))
        
        rounds +=1
    # print(".................................",len(gun_round))
    print("PLayer",current_player.name,"Make a Move")
    if current_player.ability_left:
        decision = int(input("1.Kill\n2.Show Special Items\n"))
    else:
        decision = int(input("1.Kill\n"))


    if decision == 1:
        sp_cond = current_player.shoot()
    elif decision == 2 and current_player.ability_left:
            current_player.show_abilities()
    else:
        clear_screen()
        print("Please enter valid numbers as shown: ")  

# \\ some problem is there in the player removal system alter the shooting function 
# choose the player to shoot: 
# aa 0----- ❤︎  ❤︎  ❤︎ 
# bb 1-----
# cc 2----- ❤︎  ❤︎  ❤︎  ❤︎  ❤︎ 
# dd 3----- ❤︎  ❤︎  ❤︎  ❤︎  ❤︎ 
