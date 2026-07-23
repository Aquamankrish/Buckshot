import random
gun = []
max_bullet = 9
no_of_bullets = random.randint(5,max_bullet)
no_of_live_bullets = no_of_bullets / 2 
for _ in range(no_of_bullets):
        
        if no_of_live_bullets > 0:
            gun.append(True)
            no_of_live_bullets -= 1
        else:
            gun.append(False)
gun_round = gun.copy()
print(gun_round)
revealed_list = []
for i in range(len(gun_round)):
    round_len = len(gun_round)
    random_bullet_index = random.randrange(0, round_len)
    while random_bullet_index in revealed_list and len(revealed_list) != round_len:
        random_bullet_index = random.randrange(0, round_len)
    else:          
        revealed_list.append(random_bullet_index)
        if gun_round[random_bullet_index]:
                print(random_bullet_index+1, "is a LIVE Bullet")
        else:
                print(random_bullet_index+1, "is a FAKE Bullet")

