# Author: Raunak Bhojwani
# Monday 6 October 2014
# Lab 1 - Pong
# This program is designed to open a new window, in which a game of Atari Pong will begin. The game should accommodate two 
# players. They should use the keys A&Z or K&M to control the paddles at either end of the window. The ball should accelerate
# as time goes on, making it more difficult for each player. The ball should also change color each time it has been struck
# by a paddle. If a player misses the ball, the game is over. In order to restart, the space bar must be pressed. If you would
# like to quit the game, you should press the q-key.

# Import functions that will be called in this file
from cs1lib import *
from random import uniform


# Define variables that will remain constant throughout the duration of the program
WINDOW_SIZE = 400
PADDLE_HEIGHT = 80
PADDLE_WIDTH = 20
PADDLE_MOVE = 10                # The amount the paddle moves per iteration of the while-loop (if the key is pressed)
SLEEP_TIME = 0.02
RECTANGLE1_X = 0 
RECTANGLE2_X = WINDOW_SIZE - PADDLE_WIDTH
RADIUS = 4                      # Radius of the ball
ACCELERATION = 0.5              # The amount the speed of the ball increases by per paddle-hit
GAME_MESSAGE_X = 65
GAME_MESSAGE_Y = 200
    
# Begin by defining the main function
def pong():
    
    # Define state variables that will be updated inside the while-loop (NOTE: these are defined outside the while-loop)
    rectangle1_y = 0                                    # Position of Paddle1  
    rectangle2_y = WINDOW_SIZE - PADDLE_HEIGHT          # Position of Paddle2
    ball_x = WINDOW_SIZE/2                              # Position of ball (x)
    ball_y = WINDOW_SIZE/2                              # Position of ball (y)
    ball_x_speed = uniform(4, 6)                        # Speed of ball (x)
    ball_y_speed = uniform(4, 6)                        # Speed of ball (y)
    r = 0                                               # Amount of red in ball color
    g = 1                                               # Amount of green in ball color
    b = 0                                               # Amount of blue in ball color

# Begin the while-loop
    while not window_closed():
        
        # Set background color and call the clear() function inside while-loop. I have also added a background image to make
        # my game more appealing.
        set_clear_color(1, 1, 0)
        clear()
        background_img = load_image("oie_644258GQsvZ7KT.jpg")
        draw_image(background_img, 0, 0)
         
        # Drawing paddles (disable stroke so that the paddles do not have a border) I have included different images for each paddle
        # to add an aesthetic touch 
        
        disable_stroke()
        set_fill_color(0.5, 0, 0)
        
        # LEFT paddle
        draw_rectangle(RECTANGLE1_X, rectangle1_y, PADDLE_WIDTH, PADDLE_HEIGHT)     # NOTE: parameters passes are variables, not integers
        paddle1 = load_image("oie_ALjV3qW1ccRj.png")
        draw_image(paddle1, RECTANGLE1_X, rectangle1_y)
        
        # RIGHT paddle
        draw_rectangle(RECTANGLE2_X, rectangle2_y, PADDLE_WIDTH, PADDLE_HEIGHT)
        paddle2 = load_image("oie_alAH5qGcCZJJ.png")
        draw_image(paddle2, RECTANGLE2_X, rectangle2_y)
        
        # The first if-ladder. This if-ladder is in relation to the paddles moving, allowing the paddles to move upon
        # pressing A, Z, K or M but not allowing the leave the window. Examine the conditional statements for more detail.
        # NOTE: Inside each ladder, I update the state variable of the position of each paddle.
      
        if is_key_pressed("a") and rectangle1_y >= 0:
            rectangle1_y = rectangle1_y - PADDLE_MOVE
        
        if is_key_pressed("z") and rectangle1_y <= (WINDOW_SIZE - PADDLE_HEIGHT):
            rectangle1_y = rectangle1_y + PADDLE_MOVE
        
        if is_key_pressed("k") and rectangle2_y >= 0:
            rectangle2_y = rectangle2_y - PADDLE_MOVE
        
        if is_key_pressed("m") and rectangle2_y <= (WINDOW_SIZE - PADDLE_HEIGHT):
            rectangle2_y = rectangle2_y + PADDLE_MOVE
        
        # Draw the ball. NOTE: the parameters of the set_fill_color, and the draw_circle are state variables. This allows me 
        # change the color and the position of the ball in the program, allowing the ball to move.
        set_fill_color(r, g, b)
        draw_circle(ball_x, ball_y, RADIUS)
        
        # Updating state variables. This is where I tell the ball to move. Note how I have used ball speeds - they will be useful to
        # change the direction of the ball upon contact with a wall or a paddle
        ball_x = ball_x + ball_x_speed
        ball_y = ball_y + ball_y_speed     
        
        
        # The second if-ladder. This if-ladder is in relation to the position of the ball. Depending on the position of
        # the ball, the code below will tell the ball how to react. For example if it hits the top or bottom wall, the code will 
        # multiply its ball_y_speed by negative 1 (with an acceleration). Examine each if statement for more detail
            
        if ball_y <= RADIUS:                                                # Top Horizontal Wall
            ball_y_speed = (ball_y_speed - ACCELERATION) * -1
        
        if ball_y >= (WINDOW_SIZE - RADIUS):                                # Bottom Horizontal Wall
            ball_y_speed = (ball_y_speed + ACCELERATION) * -1
        
        if (ball_x < RADIUS) or (ball_x > (WINDOW_SIZE - RADIUS)):          # Either vertical wall (when the paddle misses)
            # This gets the ball to stop moving
            ball_x_speed = 0            
            ball_y_speed = 0
            
            #This shows the GAME OVER message
            enable_stroke()
            enable_smoothing()
            set_stroke_color(1, 1, 1)
            set_font_bold()
            set_font_size(40)
            draw_text("GAME OVER!", 90, 210)
        
        # This if statement checks if the ball is making contact with the RIGHT paddle. If it is, it will reverse the ball's x
        # direction and it will change its color to a random one too.
        if ((ball_x + RADIUS) >= RECTANGLE2_X) and ((rectangle2_y + PADDLE_HEIGHT) >= ball_y) and (ball_y >= rectangle2_y) and (ball_x + RADIUS) <= (WINDOW_SIZE -(PADDLE_WIDTH/2)):
            ball_x_speed = (ball_x_speed + ACCELERATION) * -1
            r = uniform(0.5, 1)
            b = uniform(0.5, 1)
            g = 0
        
        # This if statement checks if the ball is making contact with the LEFTpaddle. If it is, it will reverse the ball's x
        # direction and it will change its color to a random one too.
        if ((ball_x - RADIUS) <= PADDLE_WIDTH) and ((rectangle1_y + PADDLE_HEIGHT) >= ball_y) and (ball_y >= rectangle1_y) and ((ball_x - RADIUS) >= (PADDLE_WIDTH/2)):
            ball_x_speed = (ball_x_speed - ACCELERATION) * -1
            g = uniform(0.5, 1)
            b = uniform (0.5, 1)
            r = 0
        
        # This includes the function of the space bar. If the spacebar is pressed, the ball is returned to its starting 
        # position, the paddles are returned to their initial positions, the ball's speed is returned to its intial value
        # Along with this, a new game start message also appears.
        if get_last_keypress() == " ":
            
            # Reseting state variables
            ball_x = WINDOW_SIZE/2
            ball_y = WINDOW_SIZE/2
            rectangle1_y = 0
            rectangle2_y = WINDOW_SIZE - PADDLE_HEIGHT
            ball_x_speed = 4
            ball_y_speed = 4
            
            #Game Start Message
            enable_stroke()
            enable_smoothing()
            set_stroke_color(1, 1, 1)
            set_font_bold()
            set_font_size(20)
            draw_text("Press A, Z, K, or M to START!!", GAME_MESSAGE_X, GAME_MESSAGE_Y)
            
        
        # This includes the option of quitting the game by pressing 'q'
        if get_last_keypress() == "q":
            cs1_quit()
        
        # Request redraw and sleep
        request_redraw()
        sleep(SLEEP_TIME)
    
start_graphics(pong, "Pong!", WINDOW_SIZE, WINDOW_SIZE) # Running pong through start graphics
    