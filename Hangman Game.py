import time
import random

name = input("Enter you Name-")
print()
print("Hello", name)
print("The game is about to begin------")
time.sleep(1)
print("----------HANGMAN----------")


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january", "border", "image", "film",
                      "promise", "kids", "lungs", "doll", "rhyme", "damage", "plants", 'blow', 'petite', 'division', 'sneaky', 'yoke', 'utter', 'introduce', 'nappy', 'suggest', 'stiff', 'subtract', 'screw', 'attach', 'aggressive', 'explain', 'placid', 'lively', 'way', 'launch', 'tray']
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = "_"*length

    already_guessed = []
    play_game = ""


def play_loop():
    global play_game
    play_game = input("Play Again -- y=yes, n=no")
    while play_game not in {"y", "Y", "n", "N"}:
        play_game = input("Play Again -- y=yes, n=no")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("----------PLAY AGAIN----------")
        exit()


def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word:  " +
                  display+" Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("----------Invalid Input, Try a letter----------")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index+1:]
        display = display[:index]+guess+display[index+1:]
        print(display+"\n")
    elif guess in already_guessed:
        print("----------Try other letter----------")
    else:
        count += 1
        if count == 1:
            print("----------WRONG GUESS----------")
            print("Guess Remaining", limit-count)
        elif count == 2:
            print("----------WRONG GUESS----------")
            print("Guess Remaining", limit-count)
        elif count == 3:
            print("----------WRONG GUESS----------")
            print("Guess Remaining", limit-count)
        elif count == 4:
            print("----------WRONG GUESS----------")
            print("Guess Remaining", limit-count)
        elif count == 5:
            print("----------WRONG GUESS----------")
            print("Guess Remaining", limit-count)
            print("----------GAME OVER----------")
            print("Word was - ", already_guessed, word)
            play_loop()
    if word == "_"*length:
        print("---------YOU WON----------")
        play_loop()
    elif count != limit:
        hangman()


main()
hangman()
