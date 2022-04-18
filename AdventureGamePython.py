import time
import random


items = []


def printpause(string):
    print(string)
    time.sleep(3)


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        printpause(f'Sorry, I dont understand "{option}"\n'
                   'please try again')


def question1():
    response = valid_input("'1' let me into the castle, it's cold out here\n"
                           "'2' what equipment?\n", ['1', '2'])


def question2():
    response = valid_input("'1' take the dagger and head towards the cave\n"
                           "'2' this guy has you mistaken for someone else\n",
                           ['1', '2'])
    if response == '1':
        printpause("you head towards the cave full of resolve")
        cave()
    else:
        printpause("go find somewhere else to sleep where")
        printpause("they don't give you chores (gameover)")
        gameover()


def question3():
    response = valid_input("'1' first path\n"
                           "'2' second path\n"
                           "'3' third path\n", ['1', '2', '3'])
    if response == '1':
        printpause("you walk further into the cave and find a torch")
        printpause("you pick up the torch!")
        printpause("maybe you can use this somewhere else in the cave")
        items.append("torch")
        cave()
    elif response == '2':
        printpause("there is a giant ape in your way!")
        printpause("the ape takes the dagger from you and beats you up")
        printpause("that ape taught you a lesson for sure")
        printpause("you head back to the entrance of the cave")
        cave()
    else:
        if "torch" in items:
            printpause("there is a sword on the ground...")
            printpause("you pick it up!")
            printpause("you make your way deeper into the cave")
            items.append("sword")
            deepcave()
        else:
            printpause("it is very dark in here\n"
                       "you cant see anything and turn back")
            cave()


def question4():
    response = valid_input("'1' or '2'\n", ['1', '2'])
    if response == '1':
        printpause("your sword makes you feel brave enough")
        printpause("to fight whatever is making that noise!")
        printpause("you see a hideous greasy demon with jaws as wide")
        printpause("as your legs and breath as foul as... something foul!")
        printpause("you aren't that brave, maybe rethink your options")
        deepcave()
    else:
        printpause("you grit your teeth and march down the path to your right")
        printpause("you find a gnome working hard at a furnace")
        printpause("past him is a huge door with chains and a lock")


def question5():
    response = valid_input("'1' ask the gnome what he's making\n"
                           "'2' ask the gnome about the door\n", ['1', '2'])
    if response == '1':
        printpause("he tells you he is looking for")
        printpause("good metal to forge a key to rescue the king")
    else:
        printpause("he is behind this door, I'm making a key for it")


def question6():
    response = valid_input("'1' pick up the king and run out\n"
                           "'2' talk to the beast\n", ['1', '2'])
    if '1' in response:
        printpause("you struggle to lift the king...")
        printpause("you throw him over your shoulders and try to run out")
        printpause("...but he has had too many kingly feasts")
        printpause("you both fall over")
        printpause("maybe try talking to the monster")
        bossfight()
    if '2' in response:
        printpause("He is surprisingly well spoken")
        printpause("'I have kingnapped your monarch, peasant'")
        printpause("'unfornately I have a crippling")
        printpause("addiction to gambling.'")
        printpause("'I will allow you to liberate him...")
        printpause("if you play me in a game of chance.'")


def question7():
    response = valid_input("'1' play the game\n"
                           "'2' turn around and leave, this isn't worth it\n",
                           ['1', '2'])
    if '1' in response:
        printpause("you will roll 2 die, if the total is over 6 you win")
        printpause("get ready... hereee it goeeeees")
        printpause("...")
        diceroll()
    if '2' in response:
        gameover()


def diceroll():
    total = random.randint(1, 6) + random.randint(1, 6)
    print("you rolled ", + total, "!")
    if total >= 6:
        printpause("you rescue the king and get to sleep in the guest room")
        printpause("at the castle tonight")
        printpause("thank you for playing!!")
    if total < 6:
        printpause("you didn't roll high enough, try again?")
        response = input("'yes' or 'no'\n")
        if "yes" in response:
            diceroll()
        if "no" in response:
            gameover()


def win():
    printpause("you rescue the king and get to sleep in the guest room")
    printpause("at the castle tonight")
    printpause("thank you for playing!!")


def gameover():
    printpause("game over")
    response = valid_input("would you like to play again?\n"
                           "'yes' or 'no'\n", ['yes', 'no'])
    if "yes" in response:
        start()
    if "no" in response:
        printpause("thank you for playing!")


def start():
    items = []
    printpause("you stumble out of a cave")
    printpause("it is a cold rainy night, you see a path to a castle")
    printpause("you walk to the gate of the castle")
    printpause("a guard approaches and asks you where all your equipment went")
    question1()
    printpause("the guard says you were sent to rescue the king from the")
    printpause("castle, you went into the cave to rescue him two days ago")
    printpause("the guard offers you a small dagger to defend yourself")
    question2()


def cave():
    printpause("there are many paths here")
    printpause("the first path is dimly lit but brighter than the others")
    printpause("there is a tall menacing shadow further down the second path")
    printpause("three is pitch black, choose this one when you can see better")
    question3()


def deepcave():
    printpause("there is chilling growling noise coming from the left")
    printpause("there is an intense heat coming from the right")
    question4()
    printpause("...the gnome is choosing to ignore you ")
    question5()
    printpause("...hey that sword you have is just the kind of metal I need")
    printpause("to make a key and rescue the king")
    printpause("you give the gnome your sword and")
    printpause("use the key he gives you to open the door")
    bossfight()


def bossfight():
    printpause("you see the king tied up by a shaggy beast with sharp fangs")
    question6()
    question7()


start()
