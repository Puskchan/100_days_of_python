import random

logo = """ 
   _____                       _______ _            _   _                 _               
  / ____|                     |__   __| |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                          
"""

print(logo)
print("I'm thinking of a number between 1 - 100")

def compare(num,user_guess):
    #Function to Compare the random number with the users guess
    if num > user_guess:
        return "Too low"
    elif num < user_guess:
        return "Too high"
    else:
        return f"You got it! The asnwer was {number}" #This is the only case you win

number = random.randint(1,100) #For choosing a random integer from 1 -100

difficulty = input("Choose a difficulty. Type 'easy'/'hard': ") #The difficulty

if difficulty == "easy":
    lives = 10 #In easy mode 10 lives are given
else:
    lives = 5 #In hard mode 5 lives are given
    
while lives>0:
    #The game will run until all your lives come down to 0
    print(f"You have {lives} attempts left.")
    guess = int(input("Guess the number: ")) #User guess
    comparision = compare(number,guess) #Call the function
    print(comparision)
    if comparision == "Too high" or comparision == "Too low":
        lives -= 1 #Deduct life when the user guesses wrong
    else:
        lives = -1 #Set lives to -1 to get out of the loop

if lives == 0:
    #Just to inform the user that he/she lost the game
    print("You lost! Try again.")