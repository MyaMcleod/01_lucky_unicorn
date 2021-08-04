
error = "Please enter a whole number between 1 and 10\n"

valid = False
while not valid:
    try:
        response_1 = int(input("How much would you "
                             "like to play with?"))

        if 0 < response_1 <= 10:
            print("You have asked to play with ${}".format(response_1))
        else:
            print(error)

    except ValueError:
        print(error)
