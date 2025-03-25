import random, os

def intro():
    """Plays the intro sequence."""
    money = 100
    
    print("""NOTE: If the game design ever feels weird it's likely
because this was a school assignment and I had a
criteria to follow.""")
    input(">")
    print("Also, fair warning that this game is heavily rng based!")
    input(">")
    print("""Also for best playing experience you should press
Ctrl & + twice. That's about it.""")
    input(">")
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(""" _____ _   _ ______ _____ _____ _   _ _____ _    ______ 
|_   _| | | || ___ \  ___/  ___| | | |  _  | |   |  _  \
  | | | |_| || |_/ / |__ \ `--.| |_| | | | | |   | | | |
  | | |  _  ||    /|  __| `--. \  _  | | | | |   | | | |
  | | | | | || |\ \| |___/\__/ / | | \ \_/ / |___| |/ / 
  \_/ \_| |_/\_| \_\____/\____/\_| |_/\___/\_____/___/  
                                                        
                                                        
 ___________   _____ _____ ___________ _   _            
|  _  |  ___| |  ___|_   _|  ___| ___ \ \ | |           
| | | | |_    | |__   | | | |__ | |_/ /  \| |           
| | | |  _|   |  __|  | | |  __||    /| . ` |           
\ \_/ / |     | |___  | | | |___| |\ \| |\  |           
 \___/\_|     \____/  \_/ \____/\_| \_\_| \_/           
                                                        
""")
    input("\nPress enter to play\n")
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("""Researcher: Hi, you must be our new recruit. I have
been informed by my associates that you are the strongest
and most experienced adventurer in all of the southwest.""")
    input(">")
    print("""Researcher: Welcome to the flatlands! Right up ahead you
will depart from me and make your way through the grasslands, the first 
threshold to your long journey up ahead.""")
    input(">")
    yn = input("""Researcher: Before you go, however, you need to buy your supplies
from the shop. Did you get directed to grab your $100 from the
bank? (y/n): """)
    if yn.lower() == "y":
        print("Great! Here, I'll show you to the shop.")
        input(">")
    elif yn.lower() == "n":
        print(""""Researcher: Not a problem. Here's $80 to get you started,
not $100 but it will help so please pay me back later.""")
        money = 80
        print("You got $80")
    else:
        print("""Researcher: Not gonna give me a yes or no are you? Wow, what
a recruit you are.""")
    
    return money    

#-----------------------------------------------------------#
    
def shop(money):
    """Displays the shop and allows the player to buy supplies."""
    os.system('cls' if os.name == 'nt' else 'clear')
    choice = None
    weapons = []
    items = []

    while choice != 10:
    
        print("""
\nSHOP:
        
1. Dagger .................... $30
2. Shortsword  ............... $80
3. Longsword ................. $150
4. Bombs (x3) ................ $50
5. Bread (x3) ................ $15
6. Heal Potion ............... $25
7. Mega Noodles .............. $30
8. Big Steak ................. $50
#--------------------------------#
9. Item Info
10. Exit""")
        
        print("\nYour balance: $"""+str(money))
        choice = int(input("Enter a Number: "))
    
        if choice == 1:
            if money >= 30:
                print("\nYou got a Dagger")
                weapons.append("Dagger (30 dmg)")
                money -= 30
                input(">")
            else:
                print("You can't afford that.")
                input(">")
                
        if choice == 2:
            if money >= 80:
                print("\nYou got a Shortsword")
                weapons.append("Shortsword (50 dmg)")
                money -= 80
                input(">")
            else:
                print("You can't afford that.")
                input(">")
                
        if choice == 3:
            if money >= 150:
                print("\nYou got a Longsword")
                weapons.append("Longsword (80 dmg)")
                money -= 150
                input(">")
            else:
                print("You can't afford that.")
                input(">")
                
        if choice == 4:
            if money >= 50:
                print("\nYou got Bombs (x3)")
                items.append("Bomb (80 dmg)")
                items.append("Bomb (80 dmg)")
                items.append("Bomb (80 dmg)")
                money -= 50
                input(">")
            else:
                print("You can't afford that.")
                input(">")
                
        if choice == 5:
            if money >= 15:
                print("\nYou got a Bread (x3)")
                items.append("Bread (20 hp)")
                items.append("Bread (20 hp)")
                items.append("Bread (20 hp)")
                money -= 15
                input(">")
            else:
                print("You can't afford that.")
                input(">")
                
        if choice == 6:
            if money >= 25:
                print("\nYou got a Heal Potion")
                items.append("Heal Potion (35 hp)")
                money -= 25
                input(">")
            else:
                print("You can't afford that.")
                input(">")
                
        if choice == 7:
            if money >= 30:
                print("\nYou got Mega Noodles")
                items.append("Mega Noodles (50 hp)")
                money -= 30
                input(">")
            else:
                print("You can't afford that.")
                input(">")
                
        if choice == 8:
            if money >= 50:
                print("\nYou got a Big Steak")
                items.append("Big Steak (80 hp)")
                money -= 50
                input(">")
            else:
                print("You can't afford that.")
                input(">")
                
        if choice == 9:
            print("""
1. Dagger ........... 30 dmg
2. Shortsword  ...... 50 dmg
3. Longsword ........ 80 dmg
4. Bombs (x3) ....... 80 dmg
5. Bread (x3) ....... 20 hp
6. Heal Potion ...... 35 hp
7. Mega Noodles ..... 50 hp
8. Big Steak ........ 80 hp
#---------------------------#""")
            input(">")
            
        if choice == 10:
            count = 0
            for i in weapons:
                if i == "Dagger (30 dmg)":
                    count += 1
                elif i == "Shortsword (50 dmg)":
                    count += 1
                elif i == "Longsword (80 dmg)":
                    count += 1
                elif i == "Fists (15 dmg)":
                    count += 1
            if count < 1: 
                weapons.append("Fists (15 dmg)")
            print("Come again!")
            input(">")
    
    return money, weapons, items
                
        
def intro2():
    print("""Researcher: Now that you are finished buying your supplies,
it's time to head out on your journey. Be careful my friend, stay safe.
Remember .""")
    input(">")
#     path = int(input("""\nPATHS:
# 1. Grasslands of Hope
# 2. Caverns of Chaos
# 3. Desolated Desert
# 4. Eye of the Storm
# 5. Magma Cavity

# Choice: """))
    print("""Researcher: Well, good luck on your journey my friend.
I'll hope to see you on the other side.""")
    input(">")

#--------------------------------------------------------------

def grasslands(money,weapons,items):
    """Plays the grassland area"""
    health = 100
    os.system('cls' if os.name == 'nt' else 'clear')
    print("THRESHOLD 1: GRASSLANDS")
    
    def battle(health,weapons,items,money,percent):
        enemy = random.randint(1,3)
        
        if percent != 100:
            if enemy == 1:
                enemyhealth = 90
                print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠻⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡀⠈⠛⢿⣿⣿⣁⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⠟⠛⠛⠿⡄⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡟⢡⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⠀⣀⣉⣤⣤⣤⡀⣤⣄⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠻⣿⣦⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢀⣠⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⣽⣿⣷⣄⠀⠀⠀⠀
    ⠀⠀⣾⡿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣷⣄⠀⠀
    ⠀⢀⣼⡀⠀⠀⠈⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⠃⠀
    ⠀⠘⠟⠁⠀⠀⠀⠀⢿⣿⣿⡿⠟⠋⠉⠉⠉⠙⢿⣿⣿⣿⡟⠁⠀⠀⢠⣿⡄⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢿⣿⣿⡦⠀⠙⠻⠟⠁⠀⠀⠀⠈⠛⠃⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
A slime has approached!""")
            
            elif enemy == 2:
                enemyhealth = 60
                print("""
        
                               (o)(o)
                              /     \
                             /       |
                            /   \  * |
              ________     /    /\__/
      _      /        \   /    /
     / \    /  ____    \_/    /
    //\ \  /  /    \         /
    V  \ \/  /      \       /
        \___/        \_____/
        
        
A worm has approached!""")
            
            elif enemy == 3:
                enemyhealth = 120
                print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⢴⢾⡙⢞⣷⢦⢤⠀⠀⠀⠀⠀
⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⣢⣜⡛⠘⣫⣄⣻⠀⠀⠀⠀⠀
⢠⠶⣼⣇⣵⡤⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡺⠍⢫⣶⢰⣍⠋⢽⠀⠀⠀⠀⠀
⣎⣴⣌⡛⢋⣴⣼⠀⠀⠀⠀⡖⢦⠀⠀⢀⣠⣤⣄⡀⠀⠀⠙⠛⠾⣡⢬⣻⠾⠚⠁⢀⡤⡀⠀
⣠⠞⣩⣶⣮⡙⢦⠀⠀⠀⠀⠁⣪⣴⣾⡿⠟⠛⠻⢿⣷⣦⣄⡀⠀⠈⠉⠀⠀⠀⡖⠚⠀⠓⢢
⠈⠚⣿⣇⣽⠙⠉⠀⣀⣤⣶⣿⠿⠛⠁⠀⠀⠀⠀⠀⠈⠙⠿⣿⣷⣦⣀⠀⠀⠀⠈⠹⣀⡟⠉
⠀⠀⠀⠀⠀⢀⣴⣾⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣶⡄⠀⠀⠈⠀⠀
⣠⣤⣤⡀⠀⢺⣿⠻⣷⣦⣔⠢⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⠿⢿⣿⠀⠀⠀⠀⠀
⣿⣏⣿⣿⠀⢸⣿⠀⠀⠉⠛⠿⣶⣭⡓⠤⣀⠀⠀⠀⢀⣠⣴⡾⠟⠋⠁⡆⢸⣿⠀⢀⡤⣄⠀
⠙⠛⠛⠃⠀⢸⣿⠀⠀⠀⠀⠀⠀⠙⠻⢷⣦⣭⣤⣶⠿⠋⠁⠀⠀⡄⠀⡇⢸⣿⠀⠘⠦⠞⠀
⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠲⡌⣿⡏⠀⠠⠀⠀⠀⣁⠤⠒⡇⢸⣿⠀⣴⣦⡀⠀
⠀⠀⣖⠙⡆⢸⣿⠀⠀⠀⠀⠀⠀⢀⠔⠁⡇⣿⡇⠀⠁⠠⡾⣴⡿⣿⣦⡄⢸⣿⠘⠧⠼⠇⠀
⠀⠀⠈⠉⠁⣼⣿⢀⡠⠖⠀⠀⢀⠥⣄⠀⡇⣿⡇⡇⠀⡼⡽⢿⣖⣣⣿⡇⢸⣿⠀⡖⢲⡄⠀
⠀⠀⠀⠀⠀⠸⣿⣦⣑⠢⢄⡀⠸⣀⣸⠀⡇⣿⡇⡇⢾⠞⢶⠎⣉⡿⢓⣡⣿⣿⠀⠉⠉⠁⠀
⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣦⣍⡓⠦⣀⠀⡇⣿⡇⡇⢀⡠⠔⣫⣵⣾⣿⣿⡿⠿⣿⣶⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣹⣿⣿⣷⣬⣙⠃⣿⡇⢓⣭⣶⣿⣿⣛⢹⣿⣯⠤⠀⢿⢻⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡴⢦⣿⣏⠀⣹⣿⠿⣿⣿⣿⡿⠟⠉⣸⣤⣼⠈⣿⣯⣓⣒⣪⣾⡿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠛⠋⠙⠿⠿⠿⠃⠀⠀⠀⠀⠀⠀⠘⠿⠽⠿⠀⠈⠛⠿⠿⠿⠋⠀⠀⠀

An ice cube slides forth!""")

        
        else:
            enemyhealth = 200
            print("""
              ,
      _,-'\   /|   .    .    /`.
  _,-'     \_/_|_  |\   |`. /   `._,--===--.__
 ^       _/"/  " \ : \__|_ /.   ,'    :.  :. .`-._
        // ^   /7 t'""    "`-._/ ,'\   :   :  :  .`.
        Y      L/ )\         ]],'   \  :   :  :   : `.
        |        /  `.n_n_n,','\_    \ ;   ;  ;   ;  _>
        |__    ,'     |  \`-'    `-.__\_______.==---'
       //  `"" \      |   \            \
       \|     |/      /    \            \
                     /     |             `.
                    /      |               ^
                   ^       |
                           ^
        
A boss (gi)ant has approached!""")
        
        
        while True:
            print("\nHealth:",health)
            print("""What would you like to use?
#-------------------------#
1. Weapons
2. Items
""")
            choice = input("Choice: ")
            if choice == "1": #WEAPONS
                
                count = 0
                print("\nWeapons List:\n")
                for i in weapons:
                    count += 1
                    print(str(count)+".",i)
                weapon = int(input("\nChosen Weapon: "))
                
                if weapons[weapon-1] == "Fists (15 dmg)":
                    enemyhealth -= 15
                    print("\nEnemy took 15 damage")
                    print("Enemy Health:",enemyhealth)
                    
                    if enemyhealth <= 0:
                        print("You defeated the enemy!")
                        if percent != 100:
                            gain = random.randint(10,20) #REGULAR GAIN
                        else:
                            gain = 50 #BOSS GAIN
                        print("You gained $"+str(gain))
                        money += gain
                        break
                
                elif weapons[weapon-1] == "Dagger (30 dmg)":
                    enemyhealth -= 30
                    print("\nEnemy took 30 damage")
                    print("Enemy Health:",enemyhealth)
                    
                    if enemyhealth <= 0:
                        print("You defeated the enemy!")
                        if percent != 100:
                            gain = random.randint(10,20) #REGULAR GAIN
                        else:
                            gain = 50 #BOSS GAIN
                        print("You gained $"+str(gain))
                        money += gain
                        break
                
                elif weapons[weapon-1] == "Shortsword (50 dmg)":
                    enemyhealth -= 50
                    print("\nEnemy took 50 damage")
                    print("Enemy Health:",enemyhealth)
                    
                    if enemyhealth <= 0:
                        print("You defeated the enemy!")
                        gain = random.randint(10,20)
                        print("You gained $"+str(gain))
                        money += gain
                        break
                    
                    print("Enemy is attacking!")
                    input(">")
                    
                    dmg = random.randint(20,40)
                    health -= dmg
                    print("You took",dmg,"damage")
                    print("Health:",health)
                    
                    if health <= 0:
                        print("\nYou died.")
                        print("Game over.")
                        exit()
                
            elif choice == "2": #ITEMS
            # 5. Bread (x3) ....... 15 hp
            # 6. Heal Potion ...... 35 hp
            # 7. Mega Noodles ..... 50 hp
            # 8. Big Steak ........ 80 hp
                count = 0
                print("Items List:\n")
                for i in items:
                    count += 1
                    print(str(count)+".",i)
                    
                if count == 0:
                    print("No items!")
                    input(">")
                    continue
                else:
                    item = int(input("\nChosen Item: "))
                
                if items[item-1] == "Bread (20 hp)":
                    items.pop(item-1)
                    if health - 15 >= 80:
                        health = 100
                    else:
                        health += 20
                    print("You gained 20 health")
                    print("Health:",health)
                    
                elif items[item-1] == "Heal Potion (35 hp)":
                    if health - 35 >= 65:
                        health = 100
                    else:
                        health += 35
                    print("You gained 35 health")
                    print("Health:",health)
                    
                elif items[item-1] == "Mega Noodles (50 hp)":
                    if health - 50 >= 50:
                        health = 100
                    else:
                        health += 50
                    print("You gained 50 health")
                    print("Health:",health)
                    
                elif items[item-1] == "Big Steak (80 hp)":
                    if health - 80 >= 20:
                        health = 100
                    else:
                        health += 80
                    print("You gained 80 health")
                    print("Health:",health)
            
                    
            print("\nEnemy is attacking!")
            input(">")
            
            
            if percent != 100:
                dmg = random.randint(10,20) #REGULAR ATTACK
            else:
                dmg = random.randint(20,40) #BOSS ATTACK
            
            health -= dmg
            print("You took",dmg,"damage")
            print("Health:",health)
            
            if health <= 0:
                print("\nYou died.")
                print("Game over.")
                exit()
        
          

        


        
        return health,items,money
    
    health = 100
    percent = 0
    
    while percent < 99:
    
        if percent == 0:
            print("""
        
🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 
🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦    
🛖 🟦 🟦 🤠 🟦 ⚠️ 🟦  ⚠️ 🟦  ⚠️ 🟦  ⚠️  🟦  ⚠️  🟦  💀     
🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩
Hint: You are the cowboy""")
    
        elif percent == 20:
            print("""
        
🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 
🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦    
🛖 🟦 🟦 ❌ 🟦 🤠 🟦  ⚠️ 🟦  ⚠️ 🟦  ⚠️  🟦  ⚠️  🟦  💀     
🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩
Hint: You are the cowboy""")

        elif percent == 40:
            print("""
        
🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 
🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦    
🛖 🟦 🟦 ❌ 🟦 ❌ 🟦  🤠 🟦  ⚠️ 🟦  ⚠️  🟦  ⚠️  🟦  💀     
🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩
Hint: You are the cowboy""")

        elif percent == 60:
            print("""
        
🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 
🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦    
🛖 🟦 🟦 ❌ 🟦 ❌ 🟦  ❌ 🟦  🤠 🟦  ⚠️  🟦  ⚠️  🟦  💀     
🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩
Hint: You are the cowboy""")

        elif percent == 80:
            print("""
        
🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 
🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦    
🛖 🟦 🟦 ❌ 🟦 ❌ 🟦  ❌ 🟦  ❌ 🟦  🤠  🟦  ⚠️  🟦  💀     
🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩
Hint: You are the cowboy""")

        elif percent == 100:
            print("""
        
🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 
🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦    
🛖 🟦 🟦 ❌ 🟦 ❌ 🟦  ❌ 🟦  ❌ 🟦  ❌  🟦  🤠  🟦  💀     
🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩
Hint: You are the cowboy""")

#         elif percent == 84:
#             print("""
        
# 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 
# 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦    
# 🛖 🟦 🟦 ❌ 🟦 ❌ 🟦  ❌ 🟦  ❌ 🟦  ❌  🟦 ❌ 🟦 🟦 🤠 💀             
# 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩 🟩
# Hint: You are the cowboy""")
            
        print("""Choices:

1. Continue Going
2. Check Stats
3. See Items
4. Look Around""")
        choice = int(input("\nMake a choice: "))
        run = 1
        
        while run != 0:
        
            if choice == 1:
                percent += 14
                health,items,money = battle(health,weapons,items,money,percent)
                run = 0
            elif choice == 2:
                print("\nHealth:",health)
                print("Money:",money)
                print(str(percent)+"% of the way")
                input(">")
                choice = int(input("\nMake a choice: "))
            elif choice == 3:
                count = 0
                print("\nWeapons:\n")
                for i in weapons:
                    count+=1
                    print(str(count)+".",i)
                count = 0
                print("\nItems:\n")
                for i in items:
                    count+=1
                    print(str(count)+".",i)
                input(">")
                choice = int(input("\nMake a choice: "))
            elif choice == 4:
                print("You looked around.")
                print("""
                
                .                  .-.    .  _   *     _   .
                      *          /   \     ((       _/ \       *    .
                     _    .   .--'\/\_ \     `      /    \  *    ___
                 *  / \_    _/ ^      \/\ __        /\/\  /\  __/   \ *
                  /    \  /    .'   _/  /  \  *' /    \/  \/ .`'\_/\   .
              .   /\/\  /\/ :' __  ^/  ^/    `--./.'  ^  `-.\ _    _:\ _
                 /    \/  \  _/  \-' __/.' ^ _   \_   .'\   _/ \ .  __/ \
              /\  .-   `. \/     \ / -.   _/ \ -. `_/   \ /    `._/  ^  \
              /  `-.__ ^   / .-'.--'    . /    `--./ .-'  `-.  `-. `.  -  `.
            @/        `.  / /      `-.   /  .-'   / .   .'   \    \  \  .-  \%
            @&8jgs@@%% @)&@&(88&@.-_=_-=_-=_-=_-=_.8@% &@&&8(8%@%8)(8@%8 8%@)%
            @88:::&(&8&&8:::::%&`.~-_~~-~~_~-~_~-~~=.'@(&%::::%@8&8)::&#@8::::
            `::::::8%@@%:::::@%&8:`.=~~-.~~-.~~=..~'8::::::::&@8:::::&8:::::'
             `::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.'""")
                input(">")
                choice = int(input("\nMake a choice: "))
                
    return money,weapons,items
#-----------------------------------------------------------------


def main():        
    money = intro()
    money, weapons, items = shop(money)
    
    intro2()


    money,weapons,items = grasslands(money,weapons,items)
    print("bals")
    

    
main()