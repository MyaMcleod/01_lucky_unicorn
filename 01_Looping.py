#Ask user if they have played before
show_instructions = input("Have you played before?").lower()

#if they say yes, output 'program  contiune'
if show_instructions == "yes" or show_instructions == "y", show_instructions == "Yes":
    print("Program continues!")

#if they say No, output 'program  contiune'
if show_instructions == "no" or show_instructions == "n", show_instructions == "No":
    print("Display the instructions!")

#if they say other, output 'Please answer the question'
elif show_instructions == "maybe":
    print("Please answer the question with yes or no!")

#if they say no, output 'display instructions'
else:
    print("Display the instructions!")
