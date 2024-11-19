# Name: Eddie Hogan
# Class: PROG12974 1249_83349, fall 2024
# Assignment: Assignment 1
# Date: October 1, 2024
# Program: assignment1_Hogan.py
# Description: The goal of this program is to take 2 numbers and find 
# their common factors.

# Declares the variable done, when done = true the loop ends.
done = False

# This while statment repeats the whole program if the user chooses to.
while(done == False):

    # This block of code get the first input and checks if it valid
    # if the input is not valid then the program asks for input again.
    first_input = ""

    # Repeats until a valid value is entered.
    while first_input == "":

        # Gets input and trys to turn it into a interger.
        holding_value = int(input("Enter the first positive integer: "))

        # Checks if the value is valid.
        if holding_value > 0:

            # If the value is valid it gets set as the permanent value.
            first_input = holding_value

            # Prints an error if the value is zero or not positive.
        else:
            print("Error: number must be positive. ")
    # End of get first value code.

    # This block of code get the second input and checks if it valid
    # if the input is not valid then the program asks for input again.
    second_input = ""

    # Repeats until a valid value is entered.
    while second_input == "":

        # Gets a value and trys to turn it into a interger.
        holding_value = int(input("Enter the second positive integer: "))

        # Checks value.
        if holding_value > 0:

            # If the input is valid this code makes the value permanent.
            second_input = holding_value

            # Prints an error if the value is not valid.
        else:
            print("Error: number must be positive. ")
    # End of get second value code.

    # This code checks if the value are the same, the first value is 
    # greater then the second, or if the second value is greater then
    # the first one. This code also set smaller_input to the lower of the 2 
    # values.
    # This code assumes that the smaller input is the second input then changes
    # the smaller input if needed.
    smaller_input = second_input

    # If both values are the same this code prints a message.
    if first_input == second_input:
        print("The two numbers are equal")
        
    # If the first input is larger then this code prints a message.
    elif first_input > second_input:
        print(first_input, "is greater then", second_input) 

    # If the second input is larger then this code prints a message and sets 
    # the smaller input to first input.
    else:
        print(first_input, "is less then", second_input) 
        smaller_input = first_input 
    # End of greater then less than code
        
    # Tests dividing from 1 upwards until it reaches the lower number.
    output = ""
    for loops in range(1, (smaller_input+1)):
            if (first_input % loops == 0 and second_input % loops == 0):
                output = output + f" {loops}"

    # Prints the factors
    print("Common factors of", first_input, "and", second_input, "are:" + \
        output)

    # This code finds if the user would like to use the program again.
    end_loop_done = False

    while (end_loop_done == False):
        end_string = input("Play again (Y/N or y/n): ")

        if ("n" == end_string or "N" == end_string):
            done, end_loop_done = True, True # Ends program and loop.

        elif ("y" == end_string or "Y" == end_string):
            end_loop_done = True # Ends loop but not program.
            
        else:
            print("Error: choice must be Y/N or y/n") # Repeats if not y/n.
    # End of check if user would like to play again code.