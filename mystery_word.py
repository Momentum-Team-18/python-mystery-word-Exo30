import sys
import random

def choose_word(filename, evil):
    doc = open(filename, "r")
    text = doc.read().split("\n")
    if(evil == True):
        word = random.choice(text)
        return word
    if (len(text) > 1 and text[1] == ''):
        return text[0]
    else:
        print("What difficulty do you want to play on?     ")
        print("")
        difficulty = input("easy, med, hard, random, or EVIL       ")
        if (difficulty == "easy"):
            words = list(filter(lambda x: len(x) <= 4, text))
            word = random.choice(words)
            return word
        if (difficulty == "med"):
            words = list(filter(lambda x: len(x) > 4 and len(x) <= 8, text))
            word = random.choice(words)
            return word
        if (difficulty == "hard"):
            words = list(filter(lambda x: len(x) > 8, text))
            word = random.choice(words)
            return word
        if (difficulty == "EVIL"):
            return "EVIL ACTIVATE"
        if(difficulty == "random"):
            word = random.choice(text)
            return word
        else:
            print("Invalid option please choose again")
            return
            choose_word(filename)

def play_game(display, word, guesses, guessed, answer, evil, filename):
    print("*****************************************************")
    print("*****************************************************")
    print("")
    print(display)
    print("")
    print("You have " + str(guesses) + " guesses remaining!!!")
    print(guessed)
    print("")
    char = input("Guess a letter! ")
    if (char.isalpha() == False):
        print("Please only guess letters!")
    elif(len(char) > 1):
        print("Please only guess one letter at a time!")
    elif (guessed.find(char) != -1):
        print("You've already guessed " + char + "! Please try again!")
    elif char in word:
        print(char + " is CORRECT!!!!")
        guessed += char + ' '
        while char in word:
            position = word.find(char)
            display = display[:position] + char + display[position + 1:]
            word = word[:position] + '_' + word[position +1:]
        if display == answer:
            print("YOU WIN!!!!!")
            print("The word was " + answer)
            return
    else:
        print(char + " is Wrong!!!!")
        guesses -= 1
        guessed += char + ' '
        if(guesses == 0):
            print("")
            print("You're out of Guesses!! You Lose!!")
            print("The word was " + answer)
            print("")
            return
        if(evil == True):
            guessed = " "
            word = choose_word(filename, evil)
            display = '_'*len(word)
            answer = word
    play_game(display, word, guesses, guessed, answer, evil, filename)

def init_game(filename):
    evil = False
    word = choose_word(filename, evil)
    if (word == "EVIL ACTIVATE"):
        evil = True
        word = choose_word(filename, evil)
    print(evil)
    display = '_'*len(word)
    guesses = 8
    guessed = ''
    answer = word
    print("*****************************************************")
    print("Let\'s play a guessing game!!!")
    print("")
    print("The word has " + str(len(word)) + " letters!! You have " + str(guesses) + " to get it right!!!!")
    play_game(display, word, guesses, guessed, answer, evil, filename)
    again = input("Would you like to play again? ")
    print("")
    if (again == 'yes' or again == 'y' or again =='Yes' or again == 'YES' or again == 'Y'):
        print("YES! Let's go again!")
        init_game(filename)
    else:
        print("Aw! Ok! See you later!")

filename = sys.argv[1]
if __name__ == "__main__":
    init_game(filename)
