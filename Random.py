import random

clock = 0
verb = ("Tickles", "Eats", "Munches", "Punches", "Twists", "Shoots")
noun = ("School", "Face", "Arm", "Mouth", "Head", "Nose", "Foot")


while (clock==0):
    
   e = (input())

   if e=="generate":
      print("That really ", random.choice(verb), " my ", random.choice(noun), ".")
   if e=="lmao":
       print("I know right im so random")
   if e=="bye":
       clock = clock + 1
