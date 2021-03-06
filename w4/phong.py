# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

paddle_speed = 4
ball_vel = [0,0]
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    if direction == RIGHT:
        ball_vel[0] = random.randrange(2, 4)
        ball_vel[1] = -random.randrange(1, 2)
        
    if direction == LEFT:
        ball_vel[0] = -random.randrange(2, 4)
        ball_vel[1] = -random.randrange(1, 2)
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(LEFT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global direction
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_text(str(score1), [WIDTH / 4, 60] , 50 , "white")
    canvas.draw_text(str(score2), [3 * WIDTH / 4, 60] , 50 , "white")
    
    # update ball
    
    if ball_pos[1] < BALL_RADIUS or ball_pos[1] > HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'white', 'white')
    
    # update paddle's vertical position, keep paddle on the screen
    # LEFT: paddle1_pos
    if paddle1_pos - HALF_PAD_HEIGHT + paddle1_vel > 0 and paddle1_pos + HALF_PAD_HEIGHT + paddle1_vel < HEIGHT:
        paddle1_pos += paddle1_vel
    
    
    # RIGHT: paddle2_pos
    if paddle2_pos - HALF_PAD_HEIGHT + paddle2_vel > 0 and paddle2_pos + HALF_PAD_HEIGHT + paddle2_vel < HEIGHT:
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos - HALF_PAD_HEIGHT],[PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT],
                         [PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], [0, paddle1_pos + HALF_PAD_HEIGHT]],
                 1, "White", "White")
    canvas.draw_polygon([[WIDTH-PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT],[WIDTH, paddle2_pos - HALF_PAD_HEIGHT],
                         [WIDTH, paddle2_pos + HALF_PAD_HEIGHT], [WIDTH-PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT]],
                 1, "White", "White")
    
    
    
    # determine whether paddle and ball collide
    # LEFT paddle
    if ball_pos[0] < BALL_RADIUS + PAD_WIDTH: 
        if ball_pos[1] < paddle1_pos - HALF_PAD_HEIGHT or ball_pos[1] > paddle1_pos + HALF_PAD_HEIGHT:
            # Right get score
            score2 += 1
            spawn_ball(RIGHT)
        else:
            ball_vel[0] = - 1.1 * ball_vel[0]
            ball_vel[1] = 1.1 * ball_vel[1] 
    
    # RIGHT paddle
    if ball_pos[0] > WIDTH - BALL_RADIUS - PAD_WIDTH:
        if ball_pos[1] < paddle2_pos - HALF_PAD_HEIGHT  or ball_pos[1] > paddle2_pos + HALF_PAD_HEIGHT:
            score1 += 1
            spawn_ball(LEFT)
        else:
            ball_vel[0] = - 1.1 * ball_vel[0]
            ball_vel[1] = 1.1 * ball_vel[1] 
    
    # draw scores
    
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    #LEFT: paddle1_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= paddle_speed;
    if key == simplegui.KEY_MAP['s']:  
        paddle1_vel += paddle_speed;
    # RIGHT: paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel -= paddle_speed;
    if key == simplegui.KEY_MAP['down']:  
        paddle2_vel += paddle_speed;
    
    
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    

    #LEFT: paddle1_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel += paddle_speed;
    if key == simplegui.KEY_MAP['s']:  
        paddle1_vel -= paddle_speed;
    # RIGHT: paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel += paddle_speed;
    if key == simplegui.KEY_MAP['down']:  
        paddle2_vel -= paddle_speed;
        
        
def restart():
    global paddle1_pos, paddle2_pos
    global score1, score2
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2

    score1 = 0
    score2 = 0
    
    new_game()

    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart, 100)

# start frame
new_game()
frame.start()
