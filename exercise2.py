#Author: Edward
#Purpose: Roulette Wheel

import random

pocket= int(input("Select a pocket between 0-36: ")) #defining the variable
if pocket == 0:
    print(f"You selected pocket {pocket}, this is a green pocket.") #this states that 0 is a green pocket
elif 1 <= pocket <= 18:
    print(f"You selected pocket {pocket}, this is a red pocket.")
elif 19 <= pocket <= 36:
    print(f"You selected pocket {pocket}, this is a black pocket.")
else:
    print("The pocket you selected is out of our range") #error message if not between 0 and 36

winning_pocket = (random.randrange(0,36)) #picking a random pocket number
if pocket == winning_pocket: #if pocket is the same as number - you win, otherwise you lose
    print("Congratulations, this is the winning pocket!")
else:
    print("Unfortunately, this is not the winning pocket, better luck next time.")