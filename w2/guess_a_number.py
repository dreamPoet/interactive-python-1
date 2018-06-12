# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

secret_number = 0 
range = 100;
guess_chances = 7;

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randrange(0,range)
    #print secret_number
    
    global guess_chances
    if (range == 100):
        guess_chances = 7
    elif(range == 1000):
        guess_chances = 10
    else:
        print "Error: wrong range"
    
    print 'New game start with range [0, ' + str(range) + ')'
    print 'Number of remaining guesses is', guess_chances
    print ''

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range
    range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range
    range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    guess_number = int(guess)
    print 'Guess was', guess

    global guess_chances
    guess_chances -= 1
    print 'Number of remaining guesses is', guess_chances
    
    if guess_chances == 0 and guess_number != secret_number:
        print 'Run out of Guess and the guess is not correct!'
        print ''
        new_game()
    elif guess_number > secret_number:
        print 'Lower'
        print ''
    elif guess_number < secret_number:
        print 'Higher'
        print ''
    else:
        print 'Correct'
        print ''
        new_game()
        
    
    
    

    
# create frame
frame = simplegui.create_frame('Guess a number', 200, 300)

# register event handlers for control elements and start frame
frame.add_input('Input a number', input_guess, 100 )
frame.add_button('Range is [0,100)', range100, 100)
frame.add_button('Range is [0,1000)', range1000, 100)
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
