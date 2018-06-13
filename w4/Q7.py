# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui

position = [10, 20]


# Handler to draw on canvas
def draw(canvas):
    position[0] += 3
    position[1] += 0.7
    canvas.draw_point(position, 'black')
    canvas.draw_polygon([[50,50], [180,50], [180,140], [50,140]], 10, 'red')


# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_canvas_background('white')
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
