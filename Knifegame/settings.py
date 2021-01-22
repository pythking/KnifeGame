#settings
import os
import pygame as pg
vec = pg.math.Vector2


Title = "Knife game"
screen_width = 800
screen_height = 600
FPS = 100
game_font = "arial"

#player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.10
PLAYER_GRAV = 0.5
JUMP_HEIGHT = -10
h = 50 #platform height

#start platforms
PLATFORM_LIST1 = [(0, screen_height-h, screen_width, h), \
                 (300, 450, 150, h),
                 ]

#colors
sky_blue = (0,128,255)
black = (0,0,0)
bg_color = black
red = (255,0,0)
grey = (30,30,30)
blue = (0,0,255)
light_blue = (100, 100, 255)

#set up assets folders (sprite image)
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "png")
