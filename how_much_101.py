def num_check(question,low,high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            response_1 = int(input("How much would you "
                                 "like to play with?"))

            if low < response_1 <= high:
                return response_1
            else:
                print(error)

        except ValueError:
            print(error)
