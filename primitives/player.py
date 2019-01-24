class Player:
    def __init__(self):
        self.hp = 100
        self.stamina = 100
        self.location_x, self.location_y = world.starting_location
        self.inventory = set()
        self.victory = False

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_west(self):
        self.move(dx=-1, dy=0)


