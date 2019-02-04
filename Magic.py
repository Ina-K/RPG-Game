class Magic:
    """
    this Magic has name , mp cost, damage, type
    """
    def __init__(self, name, mp_cost, damage, magic_type):
        self.name = name
        self.mp:cost = mp_cost
        self.damage = damage
        self.magic_type = magic_type
        self.high_damage = damage + 15
        self.low_damage = damage - 15

    def generate_magic_damage(self):
        dmg = random, rand
