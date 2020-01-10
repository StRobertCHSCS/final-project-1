

import arcade
import random

###

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Retro Ping Pong"

def fire_mode():
    pass

def cat_mode():
    pass

def multiball_mode():
    pass

def big_ball_mode():
    pass

def secret_wall():
    pass

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

    rectangle1.change_y = 5

    rectangle1.color = arcade.color.WHITE

    return rectangle1
def make_rectangle2():
    
    rectangle2 = Rectangle2()

    rectangle2.size = 14

    rectangle2.x = 1270
    rectangle2.y = 350

    rectangle2.change_y = 5

    rectangle2.color = arcade.color.WHITE

    return rectangle2

    

def make_ball():

    ball = Ball()

    # Size of the ball
    ball.size = 14
    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    ball.x = 640
    ball.y = 390

    # Speed and direction of rectangle
    ball.change_x = 8 or -8
    ball.change_y = 0

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

        
        # This command has to happen before we start drawing
        arcade.start_render()
        texture = arcade.load_texture("Images/background.png")
        arcade.draw_texture_rectangle(texture.width//2, texture.height//2, texture.width,texture.height, texture, 0)
        for ball in self.ball_list:
            arcade.draw_circle_filled(ball.x, ball.y, ball.size, ball.color)
       
        ball = make_ball()

        for rectangle1 in self.rectangle1_list:
            arcade.draw_rectangle_filled(rectangle1.x, rectangle1.y, rectangle1.size, 150,  rectangle1.color)
            #arcade.draw_rectangle_filled(rectangle1.x, rectangle1.y, rectangle1.size, 150,  rectangle1.color)
        for rectangle2 in self.rectangle2_list:
            arcade.draw_rectangle_filled(rectangle2.x, rectangle2.y, rectangle2.size, 150,  rectangle2.color)




    def on_update(self, delta_time):
        """ Movement and game logic """
        for ball in self.ball_list:
            ball.x += ball.change_x
            ball.y += ball.change_y



            if ball.y < ball.size:
                ball.change_y *= -1



            if ball.y > SCREEN_HEIGHT - ball.size:
                ball.change_y *= -1





def main():
    MyGame()
    arcade.run()
    texture = arcade.load_texture("Images/background.png")
    arcade.draw_texture_rectangle(texture.width//2, texture.height//2, texture.width,texture.height, texture, 0)
    arcade.set_background_color()


if __name__ == "__main__":
    main()