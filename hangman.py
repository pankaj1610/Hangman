# importing modules
import random
import time


#global variable

with open("word.txt","r") as f_word:
    secret_word = list(f_word.read().split("\n"))
    secret_word = list(filter(lambda x:len(x)>5,secret_word))

word_choice = random.choice(secret_word)
word_length=len(word_choice)
turn=word_length+1
word_form=["*" for i in range(word_length) ]

#welcome message

print("Welcome to Hangman Game.")
print()
#ask for user name
user_name=input("What is your name?")

#Greeting message to user
print("Hello "+user_name)

print("Lets play the game...")
#processing for 1 second
time.sleep(1)

#computer is guessing the word

print("Guessing the word......")
#processing for 2 second
time.sleep(2)

for item in word_form:
    print(item, end=" ")
print()

print(F"\nYou have {turn} chance to guess the word.")


def hangman():
    """This is the main game loop.

        Args:
            user_word:it asks user to enter a letter as string until the secret word is guessed.
        return:
              It will show a message to the user if user guesses the correct word or does not.
        """
    global turn
    while turn>0:
        user_word = input("\nGuess the letter\n").lower()

        if user_word not in word_choice:
            print("Wrong guess!")
            for word in word_form:
                print(word,end=" ")
            turn-=1
            if turn == 0:
                print ( "\nOops!You lose the game." )
                print ( f"\nSecret word was {word_choice}." )
                break
            print ( F"\nYou have {turn} chance left." )
            continue

        for i in range(word_length):
            if user_word == word_choice[i]:
                word_form[i] = user_word
            print(word_form[i],end = " ")
            if i == word_length:
                break
        print(f"\n{user_word} is present in the word.")    
        #comparing updated wordform with word_choice
        if word_form==list(word_choice):
            print("\nCongratulation.\nYou guessed the correct word.")
            break

        turn -= 1
        if turn == 0:
            print("\nOops!You lose the game.")
            print(f"\nSecret word was {word_choice}.")
            break
        print(f"\nYou have {turn} guess left.")


hangman()
