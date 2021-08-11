import random
tokens = ["Horse", "Horse", "Horse", "Zebra", "Zebra", "Zebra", "Unicorn", "Donkey", "Donkey", "Donkey"]

STARTING_BALANCE = 100
balance = STARTING_BALANCE

for item in range(0, 10):
    chosen_num = random.randint(0, 100)


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
print()
print("Starting balance: ${.:2f}".format(STARTING_BALANCE))
