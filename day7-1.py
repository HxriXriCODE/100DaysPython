word_list = ["aardvark", "baboon", "camel"]
import random

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
chosen_word = random.choice(word_list)
print(chosen_word)
guess=str(input("Enter Your Guess")).lower()
n=0
word=int(len(chosen_word))
for i in range(0,word):
    if chosen_word[n]==guess:
        print("Right")
    else:
        print("Wrong")
    n+=1

