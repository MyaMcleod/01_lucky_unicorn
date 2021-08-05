import random

token = ["Unicorn", "Horse", "Horse", "Horse", "Zebra", "Zebra", "Zebra", "Donkey", "Donkey", "Donkey", ]
STARTING_BALANCE = 100

balance = STARTING_BALANCE

for item in range(0,500):
    chosen = random.choice(token)


    if chosen == "Unicorn":
        balance += 4

    elif chosen == "Donkey":
        balance -= 1

    else:
        balance -= 0.5

print()
print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))
