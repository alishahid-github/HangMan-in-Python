"""
Hangman
"""
# start 8.a
listOfWords = [
    'APPLE', 'BILBO', 'CHORUSED', 'DISIMAGINE',
    'ENSURING', 'FORMALISING', 'GLITCHES', 'HARMINE',
    'INDENTATION', 'JACKED', 'KALPACS', 'LAUNDRY',
    'MASKED', 'NETTED', 'OXFORD', 'PARODY', 'QUOTIENTS',
    'RACERS', 'SADNESS', 'THYREOID', 'UNDUE', 'VENT', 'WEDGED',
    'XERIC', 'YOUTHHOOD', 'ZIFFS'
]

import random as r

print("Random word is: " + r.choice(listOfWords))


# end 8.a

def inertAtString(index, string, value):
    l = list(string)
    l[index]= str(value)
    res = ""
    for i in l:
        res += i
    return res


# start 8.b
def HangMan(guess_word):
    guessed_letters = []
    count = 0
    display_word = ""
    print("You have to guess a word which have {0} letters in it.".format(len(guess_word)))
    for i in guess_word:
        display_word += '_'
        print('_', end=' ')

    is_found = False

    while (not is_found):
        l = input("\nGuess your letter: ")
        if l in guessed_letters:
            print("You already guessed that!")
            pass
        elif l in guess_word:

            for k in range(len(guess_word)):
                if guess_word[k] == l:
                    display_word = inertAtString(k, display_word, l)
                    print(display_word[k] + ' ', end='')
                    count += 1
                else:
                    print(display_word[k] + ' ', end='')

            guessed_letters.append(l)
        else:
            print("Incorrect!")

        if count == len(guess_word):
            is_found = True

    print("\nYou guessed that word!")


is_want=input("Do you want to play again Yes or No: ")
Yes=False

if is_want == 'Yes' or is_want == 'yes' or is_want == 'y' or is_want == 'Y':
    Yes=True
else:
    Yes = False

while(Yes):
        print("\n>>> Welcome to HangMan!")
        guess_word = r.choice(listOfWords)
        HangMan(guess_word)
        is_want = input("Do you want to play again Yes or No: ")
        if is_want == 'Yes' or is_want == 'yes' or is_want == 'y' or is_want == 'Y':
            Yes = True
        else:
            Yes = False


print("\nGame Ended")
# start 8.b

