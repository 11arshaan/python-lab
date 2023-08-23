import random
cards = [11, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 10, 10, 10]

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
dealer = {
    "cards": [],
    "total": 0
}
user = {
    "cards": [],
    "total": 0
}


def randomCard():
    return cards[random.randint(0, len(cards)-1)]

def draw():
    if dealer['total'] < 21:
        dealer['cards'].append(randomCard())
        dealer['total'] = sum(dealer['cards'])
    user['cards'].append(randomCard())
    user['total'] = sum(user['cards'])

def drawUser():
    user['cards'].append(randomCard())
    user['total'] = sum(user['cards'])

def drawDealer():
    dealer['cards'].append(randomCard())
    dealer['total'] = sum(dealer['cards'])

def showCards():
    print(f"\n\nYou: {user['cards']}.  Total: {user['total']}")
    print(f"Dealer: {dealer['cards']}. Total: {dealer['total']}")
    
def choice():
    choice = input("Type 'y' to hit, type 'n' to hold: ")
    while choice != 'y' and choice != 'n':
        input("Invalid entry. Type 'y' to hit, type 'n' to hold: ")
    if choice == 'y':
        return True
    if choice == 'n':
        return False

def check21():
    if user['total'] > 21:
        print("Bust!")
        play = input("Play again? type 'y' to play again, type 'n' to exit: ")
        while play != 'y' and play != 'n':
            input("invalid entry. Please enter 'y' to play or 'n' to exit: ")
        if play == 'n': 
            quit()
        else: 
            resetCards()
            blackjack()
        
    if dealer['total'] > 21:
        print("Win!")
        play = input("Play again? type 'y' to play again, type 'n' to exit: ")
        while play != 'y' and play != 'n':
            input("invalid entry. Please enter 'y' to play or 'n' to exit: ")
        if play == 'n': 
            quit()
        else: 
            resetCards()
            blackjack()

def resetCards():
    dealer['cards'] = []
    dealer['total'] = 0
    user['cards'] = []
    user['total'] = 0

def checkWin():
    if (user['total'] > dealer['total']):
        print("Win!")
    if (dealer['total'] > user['total']):
        print("Lose!")
    if (dealer['total'] == user['total']):
        print("Draw!")
    

def blackjack():
    print(logo)
    input("Press enter to draw a card\n")
    draw()
    showCards()
    hit = choice()

    while hit:
        drawUser()
        showCards()
        check21()
        if dealer['total'] < user['total']:
            input("Dealer draws a card... press enter to continue.")
            drawDealer()
            showCards()
            check21()
        hit = choice()

    if not hit:
        if dealer['total'] > user['total']:
            play = input("\nLose! type 'y' to play again, type 'n' to exit: ")
            while play != 'y' and play != 'n':
                input("invalid entry. Please enter 'y' to play or 'n' to exit: ")

            if play == 'y':
                blackjack()
        else:
            while dealer['total'] < 17:
                input("Dealer draws a card...Press enter to continue")
                drawDealer()
                showCards()
                check21()
            
            checkWin()
            play = input("Play again? type 'y' to play again, type 'n' to exit: ")
            while play != 'y' and play != 'n':
                input("invalid entry. Please enter 'y' to play or 'n' to exit: ")
            if play =='n': 
                quit()
            else: 
                resetCards()
                blackjack()
        



play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while play != 'y' and play != 'n':
    input("invalid entry. Please enter 'y' to play or 'n' to exit: ")

if play == 'y':
    blackjack()