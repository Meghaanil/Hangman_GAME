from hangman_pics import hangman
import random
print("\n----HANGMAN GAME_GUESS THE CITY----\n\n")
print('''
Rules to guess the word:

1.Input single letter in one turn.
2.Don't use repeated letters.
3.Turns will be decremented after every guess.
''')
print("Guess the City..")
def guess_word():
    word = random.choice(words)
    
    return word

def is_present(letter):
    if letter.lower() in word.lower():
        return letter.lower()
    else:
        return False

def fill_blank(letter):
    global display_dash,word
    display_dash = list(display_dash)
    for i,l in enumerate(word):
        if letter == l:
            display_dash[i]=letter
    print("".join(display_dash))

def make_hangman():
    global chances
    chances += 1 
    print(hangman[chances])

def check_letter(user_choice): # when user enters single letter
    letter = is_present(user_choice)
    if letter:
        fill_blank(letter)
    else:
        make_hangman()

def check_word(user_choice): # when user enters full word
    if user_choice.lower() == word.lower():
        return True
    else:
        return False


#initial setup
chances = 0
is_win = False
with open("city.txt","r") as f:
    words=f.read().splitlines()
word=random.choice(words).lower()
word = guess_word()
display_dash = ('_ '*len(word))
print(display_dash)
print(hangman[0])


#main loop

while chances <= 5 and not is_win:
    user_choice = input("Enter Your Guess: ")
    if len(user_choice)==1:
        check_letter(user_choice)
    else:
        is_win = check_word(user_choice)
        break

    if '_' not in display_dash:
        is_win = True    


if is_win:
    print("Hey!...You WIN")
    print(f"You found the word! It is {word}.")
else:
    print("Oops...You LOST")
    print(f"Word was {word}.\nBetter luck next time! Hope You Do Well...")
