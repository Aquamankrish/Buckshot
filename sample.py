def addplayer():
    name = input("Enter Player Name ")
    player = Player(name)

class Player:
    def __init__(self, name): 
        self.abilities = {}
        self.ability_left = True
        self.name = name
        self.hearts = HEARTS

    def shoot(self):
        global no_of_players_alive, winner_not_decided, current_player, ind, power_of_shot
        #clear_screen()
        print("choose the player to shoot: ")
        for player in players:
            print(player.name, players.index(player),end = "-" * 5)
            print(player.hearts * " ❤︎ " )
        player_to_shoot = int(input(f"which head to shoot {player.name}?? Enter the number after the player name ?"))
        try:
            print(players[ind].name, "shot", players[player_to_shoot].name)
            if gun[0]:
                player = players[player_to_shoot]
                player.hearts = player.hearts - power_of_shot 
                print("It was a LIVE !! Bullet ")
                print(player.name, players.index(player),end = "-" * 5)
                print(player.hearts * " ❤︎ " )
                if player.hearts == 0:
                    print(player.name,"IS DEAD !!")
                    players.remove(player)
                    no_of_players_alive -= 1
                    print("index",ind)
                    if ind > no_of_players_alive - 1:
                        ind -= 1
                    
                    if no_of_players_alive == 1:
                        print("Only one man left...")
                        winner_not_decided = False
                spl_cond = False
                
            else:
                print("It was a FAKE.. bullet")
                if ind == player_to_shoot:
                    spl_cond = True
                    print("Its your chance again ", players[ind].name)   
                else:
                    spl_cond = False  
            if winner_not_decided: 
                if not spl_cond:      
                    if ind == no_of_players_alive - 1:
                        ind = 0
                    elif 0 <= ind < no_of_players_alive - 1:
                        ind += 1
                current_player = players[ind]
            else:
                print("Congratulations", players[0].name, "You won the game")
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
                update_ability()
            else:
                print("Please enter valid ability id")
        else:
            print("You Ran out of Abilities") 
            self.ability_left = False   
