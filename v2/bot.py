import random

from data.bank import BANK
from data.emotes import EMOTES
from data.punctuation import PUNCTUATION

class Bot:
    def __init__(self, name="bot"):
        self.name = name
        self.bank = BANK
        self.emotes = EMOTES
        self.punctuation = PUNCTUATION

    def say(self):
        string = "\n" + self.name + ": "
        string += random.choice(self.bank)
        string += random.choice(self.punctuation) + " "
        string += random.choice(self.emotes)
        print string
