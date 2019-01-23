# from Awake.primitives.action import PassiveBlock, ActionBlock
import random

class Block:
    def __init__(self, x, y, display_text, contents):
        self.contents = set(contents)
        self.location = (x, y)
        self.display_text = display_text

    def interact(self, input_string):
        if self.is_interactive:
            pass


class ShipBlock(Block):
    def __init__(self, location):
        display_text = "BIG SHIP! SMOKE!!"
        super().__init__(location, display_text, set())

class ForestBlock(Block):
    def __init__(self, location, contents):
        no_item_text = "You are in a forest."
        item_text_1 = "You are in a forest. There is a {item} propped against a tree.".format(item=contents)
        item_text_2 = "You are in a forest. There is a {item} buried under leaves.".format(item=contents)
        super().__init__(location, random.choice(item_text_1, item_text_2) if contents else no_item_text, contents)


