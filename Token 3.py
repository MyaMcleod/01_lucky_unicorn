import random

token = ["Unicorn", "Donkey", "Horse", "Zebra"]
STARTING_BALANCE = 100

balance = STARTING_BALANCE

for item in range(0,101):
    chosen = random.choice(token)


    if chosen == "Unicorn":
        balance += 4

    elif chosen == "Donkey":
        balance -= 1

    else:
        balance -= 0.5

print()
print("Starting Balance: ${}".format(STARTING_BALANCE))
print("Final Balance: ${}".format(balance))
