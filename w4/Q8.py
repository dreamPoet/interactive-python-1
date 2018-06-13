# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui

position = [50, 50]
interval = 0.1
v = [0.1, 0.1]
a = [0.1, 0.1]
f = [0.1, 0.1]

# Handler to draw on canvas
def draw(canvas):
    position[0] += interval * v[0]
    position[1] += interval * v[1]
    v[0] += interval * a[0]
    v[1] += interval * a[1]
    
    canvas.draw_circle(position, 5, 2, 'black')
    print position

def time_handle():
    a[0] += f[0]
    a[1] += f[1]

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_canvas_background('white')
frame.set_draw_handler(draw)

timer = simplegui.create_timer(1000, time_handle)

# Start the frame animation
frame.start()
timer.start()
