import random
from Config import *


class Platform(pg.sprite.Sprite):

    def __init__(self, x, y, all_sprites):
        super().__init__(all_sprites)
        self.image = pg.image.load("images/platform.png")
        self.rect = self.image.get_rect()   # 85, 15
        self.rect.x = x
        self.rect.y = y

    def render(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        if self.rect.y >= HEIGHT:
            self.rect.y = -random.randrange(0, 100)
            self.rect.x = random.randrange(0, WIDTH - 85)

    def restart(self):
        self.rect.x = random.randrange(0, WIDTH - 85)
        self.rect.y = random.randrange(0, HEIGHT - 115, 15)
