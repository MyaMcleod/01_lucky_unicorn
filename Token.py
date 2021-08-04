import random


token = ["Unicorn", "Horse", "Donkey", "Zebra"]


for item in range(0, 21):
    chosen: object = random.choice(token)
    print(chosen, end='\t')
