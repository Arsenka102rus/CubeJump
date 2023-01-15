import pygame as pg
from Config import BUTTON_EVENT


class Button(pg.sprite.Sprite):
    FONT = pg.font.Font('minecraft-1-1.otf', 30)

    def __init__(self, position: tuple, text,
                 base_image_filename='base_button.png', hover_image_filename='hover_button.png'):
        super().__init__()

        self.text = self.FONT.render(text, True, 'black')

        self.base_image = pg.image.load(f"images/{base_image_filename}")
        self.base_image.blit(self.text, ((self.base_image.get_width() - self.text.get_width()) // 2,
                                         (self.base_image.get_height() - self.text.get_height()) // 2))
        self.hover_image = pg.image.load(f"images/{hover_image_filename}")
        self.hover_image.blit(self.text, ((self.hover_image.get_width() - self.text.get_width()) // 2,
                                          (self.hover_image.get_height() - self.text.get_height()) // 2))

        self.image = self.base_image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

    def update(self, mouse_pos: tuple, mouse_click: bool):
        if self.rect.collidepoint(*mouse_pos):
            if mouse_click:
                pg.event.post(BUTTON_EVENT)
            self.image = self.hover_image
        else:
            self.image = self.base_image
