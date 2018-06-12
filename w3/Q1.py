# Mystery computation in Python
# Takes input n and computes output named result

import simplegui

# global state
max = 0;
num = 217

# helper functions

def find_next_item(current):
    if current % 2 == 0:
        return current / 2
    else:
        return current * 3 + 1

def find_seq():
    global num
    global max
    if num == 1:
        timer.stop()
        print max
    else:
        num = find_next_item(num)
        if num > max:
            max = num
            
        #print num
    
# register event handlers

timer = simplegui.create_timer(1000, find_seq)

# start program

#print num
timer.start()
