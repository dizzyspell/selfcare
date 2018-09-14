import random

BANK = ["you're cute", "you're valid", "you matter", "have a nice day", "you have great bones", "you are ~ U N S T O P P A B L E ~", "you're talented", "you're amazing", "you can do it", "wow", "i believe in you", "what a smartie", "your enemies shall crumble before you", "no one can stop you", "don't let anyone get you down", "you're the best", "you're gonna be okay", "you can do anything", "what an incredible [insert species here]", "lol", "you are the master of your own fate", "you know what they say", "love yourself", "get it", "you have the best laugh", "you light up the room - literally", "if cartoon bluebirds were real, a couple of 'em would be sitting on your shoulders singing right now", "you're strong", "you are brave", "braver than any us marine", "when you make up your mind, nothing stands in your way", "you could probably survive a zombie apocalypse", "you deserve a hug", "be proud of yourself", "you look great today", "i appreciate you", "you're wonderful", "you're one of a kind"]
EMOTES = [":3", ":)", ";)", ";3", "o.o", "^ ^", "^o^", "^u^", "^-^", "<3", "B]", ":D", ";D", "c:", "c;", ":}", ":o", "=]", "=)", ":')"]
PUNCTUATION = ["!", "!!", "!!!", ".", ".", "."]

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

b = Bot(raw_input("gimme a name: "))

while True:
    b.say()
    raw_input("\n\t\t[press enter for another]")
