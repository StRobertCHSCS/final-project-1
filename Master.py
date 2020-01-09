"""
Bounce balls on the screen.
Spawn a new ball for each mouse-click.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.bouncing_balls
"""

import arcade
import random


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Bouncing Balls Example"

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
class Rectangle:
    
    def __init__(self):
        self.x = 0 
        self.y = 0
        self.change_x = 0 
        self.change_y = 0
        self.size = 0
        self.color = None

def make_rectangle():
    
    rectangle = Rectangle()

    rectangle.size = 14

    rectangle.x = 10
    rectangle.y = 350

    rectangle.change_y = 5

    rectangle.color = arcade.color.WHITE

    return rectangle

def make_ball():

    ball = Ball()

    # Size of the ball
    ball.size = 14
    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    ball.x = 700
    ball.y = 400

    # Speed and direction of rectangle
    ball.change_x = 5
    ball.change_y = 5

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
        self.rectangle_list = []
        rectangle = make_rectangle()
        self.rectangle_list.append(rectangle)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        for ball in self.ball_list:
            arcade.draw_circle_filled(ball.x, ball.y, ball.size, ball.color)
       
        ball = make_ball()

        for rectangle in self.rectangle_list:
            arcade.draw_rectangle_filled(rectangle.x, rectangle.y, rectangle.size,100,  rectangle.color)



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


if __name__ == "__main__":
    main()