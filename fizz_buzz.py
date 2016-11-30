"""This fizzbuzz application will print
the integers from 1 to n+1 replacing any integer
divisible by 3 with 'fizz,' any integer divisible
by 5 with 'buzz,' and any integer divisible by both
with 'fizzbuzz.' The user will define the value of n
through command line input or user input after the
program loads. The program will check for both input
possibilities."""

import sys

# No command line input other than the script.py
if len(sys.argv) == 1:
    y = 1
    while y == 1: #This loop is to continue script 'till valid input is supplied
        try:
            n = int(input("Choose a limit for fizzbuzz ... "))
            y = 2
        except NameError:
            print("Please enter only numeric values.")

# Command line input is script.py plus one additional value
elif len(sys.argv) == 2:
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Please enter only numeric values as command line input. Program exiting...")
        quit()

# Command line input is script.py plus two or more additional values
else:
    print("You entered more than one value at the command\
 line please enter just one. Program exiting...")
    quit()

#This module assumes a valid value for n was ensured by the above code and prints fizzbuzz for n
print("Fizzbuzz counting up to {}.".format(n))
for x in range(1,n+1):
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    elif x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)