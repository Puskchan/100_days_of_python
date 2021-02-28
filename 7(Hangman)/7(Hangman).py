import random
from art import stages,logo
from words import wordlist


word = random.choice(wordlist)

blanks = []

lives = 6

for i in range(len(word)):
    blanks.append("_")


print(logo)
print("Let's start the game!\n")
for i in blanks:
    print(i,end=" ")
print("\n")

check = []

while lives>0:
    user_input_letter = input("Guess a letter: ").lower()

    for i in range(len(word)):
        if user_input_letter == word[i]:
            blanks[i] = word[i]

    if user_input_letter in check:
      print("You've already tried this letter!")

    check.append(user_input_letter)
    
    print("")
    for i in blanks:
        print(i,end=" ")

    print("\n")

    if user_input_letter not in word:    
        lives -= 1
        print("This letter is not in the word")
        print(stages[lives])

    
    if not "_" in blanks:
        print("You win!")


if lives == 0:
    print(f"You lost!, The word was '{word.upper()}'")

