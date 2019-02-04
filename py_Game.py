import random
from Persons import Person
from Magic import magic

print ("This is the instruction...")
#Magic
fire = Magic("Fire", 10, 30, "dark")
wind = Magic("Wind", 15, 50, "dark")
ice = Magic("Ice", 20, 70, "dark")

magic_list = [fire, wind, ice]

player = Person("Daniel", 500, 100, 50, magic_list) # or [fire, wind, ice] without a list above
enemy = Person("Vampire", 1000, 100, 20, magic_list)

player.stats()
enemy.stats()

print("----------")
running = True
while running:
    print(player.name)
    print("Choose your action: ")
    player.choose_action()
    try:
        #choice = input (">>>: ")
        choice = int(input(">>>: "))
    except ValueError:
        print("Choose a number !")
        continue
    action_index = choice - 1
    if action_index == 0:
        damage = player.generate_atk_damage()
        enemy.take_damage(damage)

        print ("You attacked {} and dealt {} damage".format(enemy.name, damage))

    if action_index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose your magic: "))
        magic_index = magic_choice - 1

        magic = main_player.magic[magic_index]
        magic_damage =generate_magic_damage
    else:
        print("Choose a correct number")
        continue

# ENEMY'S TURN
    enemy_choice = 0
    if enemy_choice == 0:
        enemy_damage = enemy.generate_atk_damage()
        player.take_damage(enemy_damage)

        print("{} attacked {} and dealt {} damage".format[enemy.name, player.name, enemy_damage ])


        player.stats()
        enemy.stats()

        if player.hp == 0:
            print("You lost")
            running = False
        if enemy.hp == 0:
            print("You won")
            running = False

    # Generate the amount of damage randomly in range of highest attack and lowest attack
    #def generate_atk_damage(self):
        # This method should return a damage value
        # The value is a random number between atk_low and atk_high

    # When player takes damage, HP will be decreased
    #def take_damage(self, dmg):
        # This method should return a new hp value after taken damage
        # new hp value is the current hp minus the dmg

    #def get_stats(self):
        # This method should print out the current stats
        # Name
        # Hp/MaxHP
        # Mp/MaxMP