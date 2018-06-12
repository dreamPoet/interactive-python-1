# template for "Stopwatch: The Game"

import time
import simplegui

# define global variables
current_time = 0
stop_times = 0
success_times = 0
stopped = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
    
def format(t):
    A = 0
    BC = 0
    D = 0
    
    if t >= 600:
        A = int(t / 600)
        t = t - 600 * A
        
    if t >= 10:
        BC = int(t / 10)
        t = t - 10 * BC
    
    D = t
    
    result = str(A)
    
    if BC > 9:
        result = result + ':' + str(BC)
    else:
        result = result + ':0' + str(BC)
        
    result = result + '.' + str(D)
    
    return result    

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global stopped
    timer.start()
    stopped = False


def stop():
    global stopped
    global stop_times
    global success_times
    if not stopped:
        stop_times += 1
        timer.stop()
        stopped = True
    
    if current_time % 10 == 0:
        success_times += 1
    
    
def reset():
    timer.stop()
    global current_time
    current_time = 0
    
    global stop_times
    global success_times
    global stopped
    stopped = True
    stop_times = 0
    success_times = 0

    
    
# define event handler for timer with 0.1 sec interval
def time_handler():
    global current_time
    current_time +=1
    #print current_time

# define draw handler
def draw(canvas):
    width = frame.get_canvas_textwidth(format(current_time), 30)
    position_x = 300 / 2 - width / 2
    canvas.draw_text(format(current_time), [position_x,150], 30, 'white' )
    message = str(success_times) + '/' + str(stop_times)
    canvas.draw_text(message, [270,20], 15, 'white' )
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 300)
frame.set_draw_handler(draw)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
timer = simplegui.create_timer(100, time_handler)


# start frame
frame.start()

# Please remember to review the grading rubric
