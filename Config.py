import pygame as pg
SIZE = WIDTH, HEIGHT = (600, 1000)
FPS = 60
font = pg.font.Font("minecraft-1-1.otf", 36)
game_over_font = pg.font.Font("minecraft-1-1.otf", 70)
restart_font = pg.font.Font("minecraft-1-1.otf", 15)
GRAVITY = 0.5
BUTTON_EVENT = pg.event.Event(pg.USEREVENT + 1)
