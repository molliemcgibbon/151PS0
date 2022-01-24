#====================================================
# Filename: Karel_Newspaper.py
# 
# Your name: Mollie McGibbon
# Who did you work with (if anyone)?: N/A
# Estimate for time spent (in hrs)?: 0.5 hours (not including about 2 hours spent
# figuring out how to make Python to work on my computer.)
#====================================================

# I've just laid out a basic starting function below. 
# While this problem is fairly simple, you should still practice
# the good habit of writing helper functions to decompose the problem
# into smaller pieces. I have provided you with a template for the
# main function and then 3 helping functions as outlined in the pdf

import karel


def main():
    """ Function to cause Karel to retrieve the newspaper. """
    # You can add your sequence of commands below here!
    # Remember you can use the defined helper functions!
    move_to_newspaper()
    pick_up_paper()
    return_to_start()

def move_to_newspaper():
    """ Helping function to move Karel to the newspaper location. """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
   
def pick_up_paper():
    """ Helping function to have Karel pick up the newspaper. """
    # Yes, this will probably be VERY simple and short
    pick_beeper()

def return_to_start():
    """ Helping function to move Karel back to its starting position. """
    turn_left()
    turn_left()
    move()
    move()
    move()
    turn_right()
    move()
  
def turn_right():
    """ Helping function to have Karel turn right. """
    turn_left()
    turn_left()
    turn_left()
