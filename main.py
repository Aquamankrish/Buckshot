import random
import time 
import os 
class Player:
    def __init__(self, name): 
        self.utilities = {}
        
print("---------------Welcome to BUCKSHOT---------------")  

no_of_players = int(input("How many players are going to play ? (2/3/4)"))
while no_of_players not in (2,3,4):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Sorry!! Only (2/3/4) players can play this game")
    no_of_players = int(input("How many players are going to play ? (2/3/4)"))

bullet = [True,False]
max_bullet = int(round(2.5*no_of_players,0))
min_bullet = max_bullet-2


def load_gun():
    global gun
    
    gun = [random.choice(bullet) for _ in range( random.randint(min_bullet,max_bullet)) ]
    random.shuffle(gun)


load_gun()
print("Live Bullets =",gun.count(True))
print("Fake Bullets =",gun.count(False))
time.sleep(5)
os.system('cls' if os.name == 'nt' else 'clear')

