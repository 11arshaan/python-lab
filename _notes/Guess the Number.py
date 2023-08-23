import random
print("Welcome!\n")

def guessTheNumber():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    while difficulty != 'easy' and difficulty != 'hard':
        input("Invalid entry. Please enter 'easy' or 'hard': ")
    number = random.randint(1, 101)
    tries = 0
    guess = 0
    play = ""

    if difficulty == 'easy':
        tries = 10
    elif difficulty == 'hard':
        tries = 5

    
    print("""  ______                                                   __      __                        __    __                          __                           
 /      \                                                 |  \    |  \                      |  \  |  \                        |  \                          
|  $$$$$$\ __    __   ______    _______   _______        _| $$_   | $$____    ______        | $$\ | $$ __    __  ______ ____  | $$____    ______    ______  
| $$ __\$$|  \  |  \ /      \  /       \ /       \      |   $$ \  | $$    \  /      \       | $$$\| $$|  \  |  \|      \    \ | $$    \  /      \  /      \ 
| $$|    \| $$  | $$|  $$$$$$\|  $$$$$$$|  $$$$$$$       \$$$$$$  | $$$$$$$\|  $$$$$$\      | $$$$\ $$| $$  | $$| $$$$$$\$$$$\| $$$$$$$\|  $$$$$$\|  $$$$$$\
| $$ \$$$$| $$  | $$| $$    $$ \$$    \  \$$    \         | $$ __ | $$  | $$| $$    $$      | $$\$$ $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$    $$| $$   \$$
| $$__| $$| $$__/ $$| $$$$$$$$ _\$$$$$$\ _\$$$$$$\        | $$|  \| $$  | $$| $$$$$$$$      | $$ \$$$$| $$__/ $$| $$ | $$ | $$| $$__/ $$| $$$$$$$$| $$      
 \$$    $$ \$$    $$ \$$     \|       $$|       $$         \$$  $$| $$  | $$ \$$     \      | $$  \$$$ \$$    $$| $$ | $$ | $$| $$    $$ \$$     \| $$      
  \$$$$$$   \$$$$$$   \$$$$$$$ \$$$$$$$  \$$$$$$$           \$$$$  \$$   \$$  \$$$$$$$       \$$   \$$  \$$$$$$  \$$  \$$  \$$ \$$$$$$$   \$$$$$$$ \$$      
                                                                                                                                                            
                                                                                                                                                            
                                                                                                                                                            """)
    print("I'm thinking of a number between 1 and 100...")
    while tries > 0:
        guess = int(input("Guess a number: "))
        if guess == number:
            print("Correct! You win!")
            play = input("Play again? Enter 'y' to play or 'n' to exit")
            while play != 'y' and play != 'n':
                input("Invalid entry. Enter 'y' to play or 'n' to exit")
            if play == 'y':
                tries = 0
                guess = 0 
                guessTheNumber()
            else:
                quit()
        else:
            tries -= 1
            if guess > number:
                print("Too high.")
            if guess < number:
                print("Too low.")
    

    play = input("Game over. Play again? Enter 'y' to play or 'n' to exit: ")
    while play != 'y' and play != 'n':
            input("Invalid entry. Enter 'y' to play or 'n' to exit")
    if play == 'y':
        tries = 0
        guess = 0 
        guessTheNumber()
    else:
        quit()

guessTheNumber()
