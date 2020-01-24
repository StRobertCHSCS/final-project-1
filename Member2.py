"""
Bounce balls on the screen.
Spawn a new ball for each mouse-click.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.bouncing_balls
"""
import arcade
import random
 
###
 
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Retro Ping Pong"
Count_1 = 0
Count_2 = 0
up_pressed = False
down_pressed = False
up_2pressed = False
down_2pressed = False
game_mode = 0
MOVEMENT_SPEED = 10
 
arcade_mode = random.randrange(1, 5)
 
def Title_Screen():
    texture = arcade.load_texture("Images/Title Screen.png")
    if game_mode == 0:
        arcade.draw_texture_rectangle(texture.width//2, texture.height//2, texture.width,texture.height, texture, 0)
 
 
 
def fire_mode():
    arcade.draw_rectangle_outline(640, 360, 500, 500, arcade.color.ORANGE, 10)
 
 
class Ball:
 
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.size = 0
        self.color = None
class Rectangle1:
    
    def __init__(self):
        self.x = 0 
        self.y = 0
        self.change_x = 0 
        self.change_y = 0
        self.size = 0
        self.color = None
 
class Rectangle2:
    def __init__(self):
        self.x = 0 
        self.y = 0
        self.change_x = 0 
        self.change_y = 0
        self.size = 0
        self.color = None
    
def make_rectangle1():
    
    rectangle1 = Rectangle1()
 
    rectangle1.size = 14
 
    rectangle1.x = 10
    rectangle1.y = 350
 
    rectangle1.change_y = 0
 
    rectangle1.color = arcade.color.WHITE
 
    return rectangle1
def make_rectangle2():
    
    rectangle2 = Rectangle2()
 
    rectangle2.size = 14
 
    rectangle2.x = 1270
    rectangle2.y = 350
 
    rectangle2.change_y = 0
 
    rectangle2.color = arcade.color.WHITE
 
    return rectangle2
 
    
 
def make_ball():
    global Count_1
    global Count_2
    ball = Ball()
 
    # Size of the ball
    ball.size = 14
    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    ball.x = 640
    ball.y = 360
 
    # Speed and direction of rectangle
    if Count_1 >= Count_2:
        ball.change_x = random.randrange(10,20)
        ball.change_y = random.randrange(10,20)
    if Count_2 > Count_1:
        ball.change_x = random.randrange(-10,-20)
        ball.change_y = random.randrange(-10,-20)
    # Color
    ball.color = arcade.color.WHITE
 
    return ball
 
 
class MyGame(arcade.Window):
    """ Main application class. """
 
 
def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        self.ball_list = []
        ball = make_ball()
        self.ball_list.append(ball)
 
        self.rectangle1_list = []
        rectangle1 = make_rectangle1()
        self.rectangle1_list.append(rectangle1)
 
        self.rectangle2_list = []
        rectangle2 = make_rectangle2()
        self.rectangle2_list.append(rectangle2)
 
 
 
 
 
 
     
 
    def on_draw(self):
        """
        Render the screen.
        """
        global Count_1, Count_2
        
        # This command has to happen before we start drawing
        arcade.start_render()
        texture = arcade.load_texture("Images/background.png")
        arcade.draw_texture_rectangle(texture.width//2, texture.height//2, texture.width,texture.height, texture, 0)
        for ball in self.ball_list:
            arcade.draw_circle_filled(ball.x, ball.y, ball.size, ball.color)
       
        ball = make_ball()
 
        for rectangle1 in self.rectangle1_list:
            arcade.draw_rectangle_filled(rectangle1.x, rectangle1.y, rectangle1.size, 150,  rectangle1.color)
 
        rectangle1 = make_rectangle1()
            
        for rectangle2 in self.rectangle2_list:
            arcade.draw_rectangle_filled(rectangle2.x, rectangle2.y, rectangle2.size, 150,  rectangle2.color)
        
        rectangle2 = make_rectangle2()
 
 
 
        #def make_score_board():
        Player_1 = "{}" .format(Count_1)
        Player_2 = "{}" .format(Count_2)
        arcade.draw_text(Player_1, 590, 660, arcade.color.WHITE, 30)
        arcade.draw_text(Player_2, 690, 660, arcade.color.WHITE, 30)
 
    def on_update(self, delta_time):
 
        """ Movement and game logic """
        global Count_1, Count_2
        for ball in self.ball_list:
            ball.x += ball.change_x
            ball.y += ball.change_y
 
 
 
            if ball.y < ball.size:
                ball.change_y *= -1
 
 
 
            if ball.y > SCREEN_HEIGHT - ball.size:
                ball.change_y *= -1
            if ball.x >= 1300 and Count_1 <= 6:
                ball.x = 640
                ball.y = 360
                Count_1 += 1
 
            if ball.x <= -20 and Count_2 <= 6:
                ball.x = 640
                ball.y = 360
                Count_2 += 1
 
            for rectangle2 in self.rectangle2_list:
                if ball.x > rectangle2.x-10 and ball.y < rectangle2.y + 75 and ball.y > rectangle2.y - 75:
                    ball.change_x = random.randrange(-10,-20)
                    ball.change_y = random.randrange(-10,-20)
                    ball.change_x *= -1
                    ball.change_y *= -1
  
            for rectangle1 in self.rectangle1_list:
                if ball.x < rectangle1.x+10 and ball.y < rectangle1.y + 75 and ball.y > rectangle1.y - 75: 
                    ball.change_x = random.randrange(10,20)
                    ball.change_y = random.randrange(10,20)
                    ball.change_x *= -1
                    ball.change_y *= -1
                    
    
 
 
 
    
                
        for rectangle2 in self.rectangle2_list:
 
            if up_pressed == True:
                rectangle2.y += 5
 
            if down_pressed == True:
                rectangle2.y -= 5
        for rectangle1 in self.rectangle1_list:
            if down_2pressed == True:
                rectangle1.y -= 5
    
            if up_2pressed == True:
                rectangle1.y += 5
        for ball in self.ball_list:
            for rectangle1 in self.rectangle1_list:
                if ball.size <= rectangle1.x and ball.y <= rectangle1.y + 75 and ball.y >= rectangle1.y - 75:
                   
                    ball.change_y *= -1
            for rectangle2 in self.rectangle2_list:
                if ball.size >= rectangle2.x and ball.y <= rectangle2.y + 75 and ball.y >= rectangle2.y - 75:
                    
                    ball.change_y*=-1
        
                    
        
 
 
 
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        global up_pressed, down_pressed, up_2pressed, down_2pressed
        if key == arcade.key.UP:
            up_pressed = True
        elif key == arcade.key.DOWN:
            down_pressed = True
        elif key == arcade.key.W:
            up_2pressed = True
        elif key == arcade.key.S:
            down_2pressed = True
 
 
    def on_mouse_press(x, y, button, modifiers):
        
        # Need to check all four limits of the button.
        if game_mode == 0:
            if (x > 496 and x < 810  and y > 306 and y < 371 ):
                game_mode = 1
            elif(x > 460 and x < 805  and y > 135 and y < 220 ):
                game_mode = 2
 
 
            
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        global up_pressed, down_pressed, up_2pressed, down_2pressed
        if key == arcade.key.UP:
            up_pressed = False
        elif key == arcade.key.DOWN:
            down_pressed = False
        elif key == arcade.key.W:
            up_2pressed = False
        elif key == arcade.key.S:
            down_2pressed = False
            
            
 
 
 
def main():
    MyGame()
    arcade.run()
    texture = arcade.load_texture("Images/background.png")
    arcade.draw_texture_rectangle(texture.width//2, texture.height//2, texture.width,texture.height, texture, 0)
    arcade.set_background_color()
 
 
if __name__ == "__main__":
    main()

