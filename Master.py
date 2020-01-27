'''
-------------------------------------------------------------------------------
Name:		Retro_Ping_Pong.py
Purpose:	To recreate Retro Ping Pong

Author:	Tang. E, Chou. I

Created:	date in 26/01/2020
------------------------------------------------------------------------------
'''

import arcade
import random

###

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Retro Ping Pong"

#Score for Player 1
Count_1 = 0 
#Score for Player 2
Count_2 = 0  
#Allows player 1 to move paddle up
up_pressed = False 
 #Allows player 1 to move paddle down
down_pressed = False 
#Allows player 2 to move paddle up
up_2pressed = False 
#Allows player 2 to move paddle down
down_2pressed = False 
#When the ball is drawn
new_ball = False 
#How fast the ball moves
MOVEMENT_SPEED = 10  
#Determines normal pong or action pong
game_mode = 0  

class Ball:
    """Movement of the Ball"""
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.size = 0
        self.color = None
        
class Rectangle1:
    """Movement of the Player 1 Paddle"""
    def __init__(self):
        self.x = 0 
        self.y = 0
        self.change_x = 0 
        self.change_y = 0
        self.size = 0
        self.color = None

class Rectangle2:
    """Movement of the Player 2 Paddle"""
    def __init__(self):
        self.x = 0 
        self.y = 0
        self.change_x = 0 
        self.change_y = 0
        self.size = 0
        self.color = None
        
class Wall:
    def __init__(self):
        self.x = 0 
        self.y = 0
        self.size = 0
        self.color = None
    
def make_rectangle1():
    """Creates the Player 1 Paddle"""
    rectangle1 = Rectangle1()

    rectangle1.size = 14

    rectangle1.x = 10
    rectangle1.y = 350

    rectangle1.change_y = 0

    rectangle1.color = arcade.color.WHITE
    
    return rectangle1

def make_rectangle2():
    """Creates the Player 2 Paddle"""
    rectangle2 = Rectangle2()

    rectangle2.size = 14

    rectangle2.x = 1270
    rectangle2.y = 350

    rectangle2.change_y = 0

    rectangle2.color = arcade.color.WHITE

    return rectangle2

def make_wall():
    """Creates the Player 2 Paddle"""
    wall = Wall()

    wall.size = 20

    wall.x = 640
    wall.y = 360


    wall.color = arcade.color.WHITE

    return wall

    

def make_ball():
    """Places the ball in the center and shoots it in a random direction"""
    global MOVEMENT_SPEED
    global Count_1
    global Count_2
    global new_ball

    ball = Ball()

    # Size of the ball
    ball.size = 14
    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.

    ball.x = 640
    ball.y = 360

    # Speed and direction of rectangle
    if Count_1 >= Count_2:
        ball.change_x = (MOVEMENT_SPEED*100+1) / 100
        ball.change_y = (MOVEMENT_SPEED*100+1) / 100
    elif Count_2 > Count_1:
        ball.change_x = (-MOVEMENT_SPEED*100+1) / 100
        ball.change_y = (-MOVEMENT_SPEED*100+1) / 100


    # Color
    ball.color = arcade.color.WHITE

    return ball


class MyGame(arcade.Window):
    """ Main application class. """
    def Title_Screen():
        global game_mode
        title = arcade.load_texture("Images/Title Screen.png")
        if game_mode == 0:
            arcade.draw_texture_rectangle(title.width, title.height, title.width,title.height, title, 0)

 
    def __init__(self):
        """Creates the Background"""
        global new_ball
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        self.ball_list = []
        ball = make_ball()
       
        

        self.rectangle1_list = []
        rectangle1 = make_rectangle1()
        self.rectangle1_list.append(rectangle1)

        self.rectangle2_list = []
        rectangle2 = make_rectangle2()
        self.rectangle2_list.append(rectangle2)

        self.wall_list = []
        wall = make_wall()
        self.wall_list.append(wall)





     

    def on_draw(self):
        """
        Render the screen.
        """
        global Count_1, Count_2
        global game_mode, new_ball
        # This command has to happen before we start drawing
        arcade.start_render()
        
        title = arcade.load_texture("Images/Title Screen.png")
        if game_mode == 0:
            arcade.draw_texture_rectangle(title.width//2, title.height//2, title.width,title.height, title, 0)

        if game_mode == 1 or game_mode == 2:
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
        if game_mode ==2:
            for wall in self.wall_list:
                arcade.draw_rectangle_filled(640, 360, 20, 200, arcade.color.WHITE)
        if game_mode == 3:
            end1_screen = arcade.load_texture("Images/Player_1_Victory.png")
            arcade.draw_texture_rectangle(end1_screen.width//2, end1_screen.height//2, end1_screen.width,end1_screen.height, end1_screen, 0)
        if game_mode == 4:
            end2_screen = arcade.load_texture("Images/Player_2_Victory.png")
            arcade.draw_texture_rectangle(end2_screen.width//2, end2_screen.height//2, end2_screen.width,end2_screen.height, end2_screen, 0)


        if game_mode == 1 or game_mode == 2:
            #def make_score_board():
            Player_1 = "{}" .format(Count_1)
            Player_2 = "{}" .format(Count_2)
            arcade.draw_text(Player_1, 590, 660, arcade.color.WHITE, 30)
            arcade.draw_text(Player_2, 690, 660, arcade.color.WHITE, 30)
        if Count_1 == 7:
            game_mode = 3
        if Count_2 ==7:
            game_mode = 4












    def on_update(self, delta_time):
        """ Movement and game logic """
        global Count_1, Count_2,  MOVEMENT_SPEED, on_draw,up_2pressed, up_pressed, down_pressed, down_2pressed, game_mode, arcade_mode,

        if game_mode == 1 or game_mode == 2 :
            for ball in self.ball_list:

                ball.x += ball.change_x
                ball.y += ball.change_y



                if ball.y < ball.size:
                    ball.change_y *= -1



                if ball.y > SCREEN_HEIGHT - ball.size:
                    ball.change_y *= -1
                if ball.x >= 1300 and Count_1 <= 6:
                    self.ball_list.pop(0)
                    ball.x = 640
                    ball.y = 360
                    Count_1 += 1
                

                if ball.x <= -20 and Count_2 <= 6:
                    self.ball_list.pop(0)
                    ball.x = 640
                    ball.y = 360
                    Count_2 += 1
            

                for rectangle2 in self.rectangle2_list:
                    if ball.x > rectangle2.x-10 and ball.y < rectangle2.y + 77 and ball.y > rectangle2.y - 77:
                    
                        ball.change_x *= -1
                        ball.change_y *= -1
                        ball.change_y -= 1
                    if ball.x > rectangle2.x-5 and ball.y < rectangle2.y + 80 and ball.y > rectangle2.y - 80:
                        ball.change_x *= 1
                        ball.change_y *= 1
                    




  
                for rectangle1 in self.rectangle1_list:
                    if ball.x < rectangle1.x+10 and ball.y < rectangle1.y + 77 and ball.y > rectangle1.y - 77:
                    
                    
                        ball.change_x *= -1

                        ball.change_y *= -1
                        ball.change_y += 1
                    if ball.x > rectangle1.x+5 and ball.y < rectangle1.y + 80 and ball.y > rectangle1.y - 80:
                        ball.change_x *= 1
                        ball.change_y *= 1
            if game_mode == 2:
                for ball in self.ball_list:
                    for wall in self.wall_list:

                        if ball.x < wall.x+10 and ball.x > wall.x - 10 and ball.y < wall.y + 77 and ball.y > wall.y - 77:
                    
                    
                            ball.change_x *= -1
                            ball.change_y *= -1
                            ball.change_y += 1


            



            




    
                
            for rectangle2 in self.rectangle2_list:

                if up_pressed == True:
                    rectangle2.y += 10

                elif down_pressed == True:
                    rectangle2.y -= 10

            for rectangle1 in self.rectangle1_list:
                if down_2pressed == True:
                    rectangle1.y -= 10
    
                elif up_2pressed == True:
                    rectangle1.y += 10
       




            


        
                    
        



    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed"""
        global up_pressed, down_pressed, up_2pressed, down_2pressed, game_mode, new_ball
        if key == arcade.key.UP:
            up_pressed = True
        elif key == arcade.key.DOWN:
            down_pressed = True
        elif key == arcade.key.W:
            up_2pressed = True
        elif key == arcade.key.S:
            down_2pressed = True
        elif key == arcade.key.N:
            new_ball = True
        if game_mode == 0:
            if key == arcade.key.G:
                game_mode = 1
            elif key == arcade.key.H:
                game_mode = 2
        





            
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key"""
        global up_pressed, down_pressed, up_2pressed, down_2pressed, new_ball
        if key == arcade.key.UP:
            up_pressed = False
        elif key == arcade.key.DOWN:
            down_pressed = False
        elif key == arcade.key.W:
            up_2pressed = False
        elif key == arcade.key.S:
            down_2pressed = False
        elif key == arcade.key.N:
            new_ball = False
        
        if key == arcade.key.G:
            game_mode = 1
        elif key == arcade.key.H:
            game_mode = 2
            
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """
        if len(self.ball_list) == 0:
            ball = make_ball()
            self.ball_list.append(ball)
        
        

        
        
            
            



def main():
    MyGame()
    arcade.run()



if __name__ == "__main__":
    main()
