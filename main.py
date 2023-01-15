import pygame as pg
import sys


def terminate():
    pg.quit()
    sys.exit()


pg.init()
pg.display.set_caption("Doodle jump")

# Импортируется сдесь, так как в этих модулях действия могут происходить только после инициализации
import Game
from Config import *
from StatrScreen import start_screen


screen = pg.display.set_mode(SIZE)

start_screen(screen)
Game.play(screen)

terminate()
