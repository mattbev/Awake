class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return "{}\n=====\n{}\n".format(self.name, self.description)


# class Shovel(Item):
#     def __init__(self):
#         super().__init__(name="Shovel",
#                          description="A shovel, best used for digging.")
#
# class Hammer(Item):
#     def __init__(self):
#         super().__init__(name="Hammer",
#                          description="A hammer, .")


#------------------------------------------------------------------------------------------



class Weapon(Item):
    def __init__(self, name, description, damage):
        self.damage = damage
        super().__init__(name, description)

    def __str__(self):
        return "{}\n=====\n{}\nDamage: {}".format(self.name, self.description, self.damage)


class Scowl(Weapon):
    def __init__(self):
        super().__init__(name="Scowl",
                         description="Only kills self esteem.",
                         damage=0)

class Fist(Weapon):
    def __init__(self):
        super().__init__(name="Fist",
                         description="Your fist, a fist-sized rock-sized fist, suitable for bludgeoning.",
                         damage=3)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         damage=5)

class SharpenedStick(Weapon):
    def __init__(self):
        super().__init__(name="Sharpened Stick",
                         description="A pointed stick, sharp enough to pierce flesh.",
                         damage=10)

class MetalRod(Weapon):
    def __init__(self):
        super().__init__(name="Metal Rod",
                         description="A long metal rod, the metal type is unclear.",
                         damage=15)


class UtilityKnife(Weapon):
    def __init__(self):
        super().__init__(name="Utility Knife",
                         description="A utility knife, like the swiss army uses.",
                         damage=15)




#------------------------------------------------------------------------------------------




class Trap(Weapon):
    def __init__(self, name, description, damage, location):
        self.location = location
        super().__init__(name, description, damage)

        def __str__(self):
            return "{}\n=====\n{}\nDamage: {}\nLocation: {}".format(self.name, self.description, self.damage, self.location)

class Snare(Trap):
    def __init__(self, location):
        self.location = location
        super().__init__(name="Snare",
                         description="A snare, capable of entrapping small game.",
                         damage=0,
                         location = location)

class LegholdTrap(Trap):
    def __init__(self, location):
        self.location = location
        super().__init__(name="Rusty Leghold Trap",
                         description="A rusty leghold trap, a relic used for catching all but the largest of animals.",
                         damage=35,
                         location = location)

class FishTrap(Trap):
    def __init__(self, location):
        self.location = location
        super().__init__(name="Fish Trap",
                         description="Some type of fish trap, unlike any seen on Earth.",
                         damage=0,
                         location = location)


#------------------------------------------------------------------------------------------


