# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui

value = 5

# Handler to draw on canvas
def keydown(key):
    global value
    value *= 2 
    
    
def keyup(key):
    global value
    value -= 3
    
def draw(canvas):
    canvas.draw_text(str(value), [150, 100], 25, 'white')
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# Start the frame animation
frame.start()
