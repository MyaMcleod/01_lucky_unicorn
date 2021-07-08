#Ask user if they have played before
show_instructions = input("Have you played before?").lower()

#if they say yes, output 'program  contiune'
if show_instructions == "yes":
    print("Program continues!")

#if they say other, output 'Please answer the question'
if show_instructions == "maybe":
    print("Please answer the question with yes or no!")

#if they say np, output 'display instructions'
else:
    print("Display the instructions!")


