import random
# Ask user to print
print("Welcome to Roll Dicer BY Aniket JOshi ;)🧡🧡")
user=str(input("Enter [R] to Roll a Dice:"))
roll=0
while (roll<15):

    if user=='R' or 'r':

        def DiceRoller():
            a=random.randint(1,6)
            print(a)
        Dice=DiceRoller()
        print("Thank you for using Roll Dice ")
        break
    else:
        print("Incorrect input !! Please use [R] to Roll")
