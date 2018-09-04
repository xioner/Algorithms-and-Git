""" 
QUESTION 1: MAXIMUM NUMBER
Design an algorithm that finds the maximum positive integer input by a user.  
The user repeatedly inputs numbers until a negative value is entered.
 
Make sure that you write up the algorithm before starting to code.
Then implement the algorithm in Python. Put your algorihmic description as a comment in the program file. """
# **********************************
# We take input of user of integer numbers
# once we take a number we compare it to the next number we take in 
# Once a negative value is entered we stop, and print out the largest integer that was entered.
#


max_int = 0
while True :
    num_int = int(input("Enter a number: "))
    if num_int < 0:
        break
    max_int = max(num_int, max_int)

print("The maximum is", max_int)   # Do not change this line

