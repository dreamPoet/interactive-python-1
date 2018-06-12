event_driven programming
start -> initialite -> wait
wait for event; an event happen, begin a handler(deal with programme); finish handler and return to wait; -> end

Events: various
input: Button; Text box
keyboard: Key down; Key up
Mouse: Click; Drag
Timer


system hold an event queue;

set a different value for a global var in a function will not change the real value of this global var outside this function; however, we can use key word global to change the value of a global var:
num = 3
def fun():
    global num
    num = 6

use local var as much as possible only if you cannot


suggested structure:
    Globals (state)
    Helper functions
    Classes
    Define event handlers
    Create a frame
    Register event handlers
    Start frame & timers


For a frame:
control area; Status area; canvas


and precedence before or;