import random


token = ["Unicorn", "Horse", "Donkey", "Zebra"]
balance = 100

for item in range(0, 21):
    chosen = random.choice(token)

  if chosen == "Unicorn":
      balance += 4
  elif: chosen == "Donkey":
      balance -= 1
  else:
      balance -= 0.5



    print("Token: {} , Balence: ${}".format(chosen, balance))
