import random

def roundWinner(user,computer):
    if user != computer:
        if user == 'rock':
            if computer == 'paper':
                return 2
            else:
                return 1
        elif user == 'paper':
            if computer == 'scissors':
                return 2
            else:
                return 1
        else:
            if computer == 'rock':
                   return 2
            else:
                return 1
    else:
        return 0

def displayStats(total):
    comp = 0
    users = 0
    tie = 0
    for key, value in total.items():
        if value == 2:
            comp += 1
        elif value == 1:
            users += 1
        else:
            tie += 1
    print("Played ", len(total), "number of rounds.")
    print("User won {} times, Computer won {} times, and it was a tie {} times.".format(users, comp, tie))


choices = ["rock", "paper", "scissors"]
computerChoice = random.choice(choices)
userChoice = str(input("Please choose rock, paper, or scissors or exit to end game: "))
stats = {}
round = 1

while userChoice != "end":
    winner = roundWinner(userChoice, computerChoice)
    if winner == 2:
        print("Computer Wins!")
    elif winner == 1:
        print("User Wins!")
    else:
        print("It's a tie.")
    stats[round] = winner
    round += 1
    userChoice = str(input("Please choose rock, paper, or scissors or exit to end game: "))
    computerChoice = random.choice(choices)



displayStats(stats)


