from word import daily_word

def main():

    letters = ['A', 'B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    is_correct = False
    # word = daily_word()
    word = 'words'
    count = 0
    max_attempts = 5

    while not is_correct and count < max_attempts:
        guess = input('guess a 5 letter word:')
        if(len(guess) == 5):
            if(guess == word):
                is_correct = True
                break
            count = count + 1
            print(f"you have {max_attempts - count} attempts remaining~")
            for letter in guess:
                if str(letter).upper() in letters:
                    letters.remove(str(letter).upper())
            for i in range(5):
                if(guess[i] == word[i]):
                    print(guess[i], end="")
                else:
                    print("_", end="")
            print(f"\navailable letters: {letters}")
        else:
            print('must be a 5 letter word')
        
    
    if(is_correct is True):
        print("you win!")
        print(f"you got it with only {count + 1} attempts!")
    else:
        print("you suck")

if __name__ == "__main__":
    main()
