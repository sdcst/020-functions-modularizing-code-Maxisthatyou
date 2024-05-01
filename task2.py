"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
import random

def title():
    print("This is a number guessing game. Player will enter a number and try to guess the number the computer chooses between 1 and 100.")

def game():
    x = random.randint(0, 100)
    for i in range(100):
        y = int(input("Please enter an integer between 0 and 100> "))
        if 0 <= y <= 100:
            if x == y:
                print("You've guessed correctly!")
                break
            elif x > y:
                print("The number you've entered is too small, try again.")
            elif x < y:
                print("The number you've entered is too big, try again.")
        else:
            print("Invalid value, try a number between 0 and 100.")

title()
game()