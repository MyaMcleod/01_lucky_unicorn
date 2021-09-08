import random
# Ask user if they have played before


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower().strip()
        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print(instructions())


def instructions():
    print("*** How to play ***")
    print()
    print("Users pay an $1 per round at the start of the game.\n"
          "The game will then generate a token that is either a zebra, horse, donkey or unicorn.\n"
          "If the token is a unicorn, the user wins $5, if it is a zebra or horse, they win 50c and\n"
          "if it is a donkey then they don’t win anything.\n"
          "Users have a limit of $10 each session\n"
          "Game ends when there is no more money or user inputs 'xxx'.")
    print()
    return ""


def num_check(question,low,high):
    error = "Please enter a whole number between 1 and 10"

    valid = False
    while not valid:
        try:
            response_1 = int(input("How much would you like to play with?"))

            if low <= response_1 <= high:
                return response_1
            else:
                print(error)

        except ValueError:
            print(error)


def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""




# ** *Main routine ***

# initalise variable
balance = 0
rounds_played = 0

played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

print()

how_much = num_check("How much would you like to play with?", 1,10)
balance = how_much

play_again = input("Press <ENTER> to play...").lower()
while play_again == "":
    rounds_played += 1
    print("*** Rounds #{} ***".format(rounds_played))
    chosen_num = random.randint(1, 100)

    if 1 <= chosen_num <= 5:
        chosen = "Unicorn"
        prize_decoration = "!"
        balance += 4

    elif 6 <= chosen_num <= 36:
        chosen = "Donkey"
        prize_decoration = "D"
        balance -= 1
    else:
        if chosen_num % 2 == 0:
            prize_decoration = "H"
            chosen = "Horse"

        else:
            chosen = "Zebra"
            prize_decoration = "Z"
        balance -= 0.5

    outcome = ("You got {}, Balance: ${:.2f}".format(chosen, balance))

    statement_generator(outcome, prize_decoration)

    if balance < 1:
        play_again = "xxx"
        print("Sorry, you have run out of money.")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit. ")


