from bot import Bot

bot = Bot(raw_input("Gimme a name! : ")) 

bot.say("What is your name?")

user = User(raw_input("You:"))

bot.meet(user)

while True:
        bot.turn()
        user.turn()
