import random
word_list = ["ardvark", "baboon", "camel"]
lives = 6
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end_of_game = False
chosen_word = random.choice(word_list)

display = []
for x in chosen_word:
    display += "_"

print(display)
print(stages[lives])

while not end_of_game:
    guess = input("Guess a letter \n")
    right_count = 0

    for index, x in enumerate(chosen_word):
        if x == guess:
            display[index] = guess
            right_count += 1
        # else:

    if right_count == 0:
        lives -= 1
        
    print(display)
    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You Win!")
        print('''
  +---+
      |
      |
  O   |
 /|\  |
 / \  |
=========
''')
    
    if lives == 0:
        end_of_game = True
        print("You Lose!")
        print(stages[lives])


