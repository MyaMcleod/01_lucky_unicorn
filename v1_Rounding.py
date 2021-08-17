import random

balance = 5

rounds_played = 0

play_again = input("Press <ENTER> to play...").lower()
while play_again == "":
    rounds_played += 1
    print("*** Rounds #{} ***".format(rounds_played))
    balance -= 1
    chosen_num = random.randint(1, 100)

    if 1 <= chosen_num <= 5:
        chosen = "Unicorn"
        balance += 4

    elif 6 <= chosen_num <= 36:
        chosen = "Donkey"
        balance -= 1
    else:
        if chosen_num % 2 == 0:
            chosen = "Horse"

        else:
            chosen = "Zebra"
        balance -= 0.5

    print("You got {}, Balance: ${:.2f}".format(chosen, balance))

    if balance < 1:
        play_again = "xxx"
        print("Sorry, you have run out of money.")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit. ")
