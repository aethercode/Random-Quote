import random

clock = 0
verb = ("Tickles", "Eats", "Munches", "Punches", "Twists", "Shoots", "Beats", "Bends", "Bites", "Blows", "Breaks", "Builds", "Burns", "Catches", "Cuts", "Digs", "Dive", "Draws", "Dreams", "Feels", "Fights", "Freezes", "Grows", "Hangs", "Hears", "Hides", "Hurts", "Throws")
noun = ("School", "Face", "Arm", "Mouth", "Head", "Nose", "Foot", "People", "History", "Art", "World", "Map", "Family", "Government", "Health", "System", "Computer", "Music", "Person", "Method", "Food", "Bird", "Literature", "Problem", "Software", "Knowledge", "Brain", "Economy", "Oven", "Friends")


while (clock==0):
    
   e = (input())

   if e=="generate":
      print("That really ", random.choice(verb), " my ", random.choice(noun), ".")
   if e=="lmao":
       print("I know right im so random")
   if e=="bye":
       clock = clock + 1
