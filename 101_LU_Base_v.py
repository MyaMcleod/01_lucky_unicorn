#Ask user if they have played before
show_instructions = input("Have you played before?").lower()

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower().strip()
        if response == "yes" or response == "y":
            response = "yes"
            return  response

        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("Display the instructions!")


def instructions():
    print("*** How to play ***")
    print()
    print("The rules of the game go here!")
    print()
    return ""

played_before = yes_no ("Have you played "
                            " the game before?")
if played_before == "no":
        instructions()

print("Program Contuines")
