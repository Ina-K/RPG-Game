import random  # used to generate random number for an attack hp


class Person:
    def __init__(self, name, hp, mp, atk, magic):
        self.maxhp = hp  # HP of character when it's full
        self.hp = hp    # HP during the game will change, but the max HP should stay the same
        self.maxmp = mp  # Same like HP
        self.mp = mp
        self.atk_high = atk + 10
        self.atk_low = atk - 10
        self.action = ["Physical Attack", "Magic"]
        self.name = name

    def stats(self):
        print(self.name)
        print(f"{self.hp}/{self.maxhp}")
        pritn(f"{self.mp}/{self.maxmp}")

    def generate_atk_damage(self):
        # this function will return a random number
        dmg = random.randint(self.atk_low, self.atk_high)
        return dmg

    def take_damage(self, dmg):
        self.hp = self.hp - dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def choose_action(self):
        index = 1
        print("ACTIONS: ")

        for element in self.action:
            print(f"{index}:{element}")
            index = index + 1

    def reduce_mp(self, used_mp):
        self.mp = self.mp - used_mp
        if self.mp < used_mp:
            print("Not enough Mana")

        return self.mp

    # def choose_magic(self):
    #     index = 1
    #     print("ACTIONS: ")

    #     for element in self.magic:

            # for element in self.action
            # print("{}, {}".format(index, element))
            # index = index + 1
            # you can also use tupple
            # for index, value in self.action:
            #             print(f"{index}, {value}")
            #             index = index + 1
