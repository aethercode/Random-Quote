print("loading...")

import random

verb = ("Tickles", "Eats", "Munches", "Punches", "Twists", "Shoots", "Beats", "Bends", "Bites", "Blows", "Breaks", "Builds", "Burns", "Catches", "Cuts", "Digs", "Dive", "Draws", "Dreams", "Feels", "Fights", "Freezes", "Grows", "Hangs", "Hears", "Hides", "Hurts", "Throws")
noun = ("School", "Face", "Arm", "Mouth", "Head", "Nose", "Foot", "People", "History", "Art", "World", "Map", "Family", "Government", "Health", "System", "Computer", "Music", "Person", "Method", "Food", "Bird", "Literature", "Problem", "Software", "Knowledge", "Brain", "Economy", "Oven", "Friends")

def generate():
   return "That really "+random.choice(verb)+" my "+random.choice(noun)+"."
def generator():
   i = (input())

   if i=="generate":
      print(generate())
   elif i=="lmao":
      print("I know right im so random")

   if i!="bye":
      generator()
   else:
      print("Bye!")


def generateList(amt):
   loop = 0
   while loop <= amt:
      print(str(loop)+": "+generate())
      loop += 1

print("done!")
print("run generator() to start the generator, then type 'generate' to get a sentence. while in generate mode, type 'bye' to leave that mode. to generate a list exit generate mode if you're in it, then type generateList() with the amount you want inside the parentheses")
