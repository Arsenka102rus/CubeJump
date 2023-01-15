from Config import *
from GUI import Button


def start_screen(surface):
    surface.fill((71, 60, 51))

    button = Button((200, 700), "Start")
    gui_sprites = pg.sprite.Group()
    gui_sprites.add(button)

    while True:
        mouse_click = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONUP:
                mouse_click = True
            if event.type == pg.USEREVENT + 1:
                return

        gui_sprites.update(pg.mouse.get_pos(), mouse_click)
        gui_sprites.draw(surface)
        pg.display.update()
