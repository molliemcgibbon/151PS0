#====================================================
# Filename: Karel_Painting.py
# 
# Your name: Mollie McGibbon
# Who did you work with (if anyone)?: N/A
# Estimate for time spent (in hrs)?: 1.5 hours
#====================================================

# I've just laid out a basic starting function below, but remember that you
# absolutely should define more helping functions to decompose the problem
# into smaller pieces! Here I'm leaving those pieces (and helper functions)
# up to you to design and name as you see fit

import karel

def main():
    """ Function to cause Karel to paint 3 sides of its house and then go indoors. """
    # You can add your code below
    paint_north_wall()
    paint_west_or_south_wall()
    paint_west_or_south_wall()
    enter_house()

def paint_north_wall():
    """ Function to make Karel paint the north-facing wall of his house. """
    while not_facing_west(): # Loop to make Karel face the correct way before starting to put beepers
        turn_left()
    while left_is_blocked():
        put_beeper() # Always assuming infinite beepers available
        move()
    if left_is_clear(): 
        if front_is_clear():
            turn_left() # Reorients Karel before beginning to paint the west-facing wall

def paint_west_or_south_wall():
    """ Funtion to make Karel paint the west-facing or south-facing wall of his house. 
    The commands are the same for these two walls, so this function just needs to be 
    included twice in a row in def main(): """
    move() # So that Karel is next to the wall
    while left_is_blocked(): 
        put_beeper()
        move()
    if left_is_clear():
        if front_is_clear():
            turn_left()  # Reorients Karel so that it will start on the next wall of the house

def enter_house():
    """ Function to make Karel enter the doorway on the east-facing wall and go into the house. """
    move()
    while left_is_blocked():
        move()
    if left_is_clear():
        turn_left()
    move()
