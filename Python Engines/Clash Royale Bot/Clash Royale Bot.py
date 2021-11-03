import os

def troop_interaction(dps_1, dps_2, health_1, health_2):
    troop_1 = 0
    troop_2 = 0

    while dps_1 > 0:
        
    
    return result

#card = [health, damage, damage per second, hit speed, elixir, move speed]
def clash_royale_bot():
    os.system("clear")
    
    knight = [1380, 167, 139, 1.2, 3, "medium"]
    lumberjack = [1060, 200, 250, 0.8, 4, "very fast"]
    mega_knight = [3300, 222, 130, 1.7, 7, "medium"]
    minni_pekka = [1129, 598, 351, 1.7, 4, "fast"]
    pekka = [3125, 678, 376, 1.8, 7, "slow"]

    knight_current_health = knight[0]
    lumberjack_current_health = lumberjack[0]
    mega_knight_current_health = mega_knight[0]
    minni_pekka_current_health = minni_pekka[0]
    pekka_current_health = pekka[0]

    print(knight[3])

    #temp
    hits_a = 0
    hits_b = 0

    while pekka_current_health > 0:
        hits_a += 1
        
        total_dps = mega_knight[2]
        pekka_current_health = pekka_current_health - mega_knight[2]

        print("health: " + str(pekka_current_health) + ", hits: " + str(hits_a))

    while mega_knight_current_health > 0:
        hits_b += 1
        
        total_dps = knight[2]
        mega_knight_current_health = mega_knight_current_health - pekka[2]

        print("health: " + str(mega_knight_current_health) + ", hits: " + str(hits_b))
        

clash_royale_bot()
