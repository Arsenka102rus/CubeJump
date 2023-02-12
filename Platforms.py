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
            self.rect.y = self.rect.y - HEIGHT
            self.rect.x = random.randrange(0, WIDTH - 85)

    def restart(self):
        self.rect.x = random.randrange(0, WIDTH - 85)


class HorizontalPlatform(Platform):

    def __init__(self, x, y, all_sprites):
        super().__init__(x, y, all_sprites)
        self.speed = 5

    def update(self):
        if self.rect.y >= HEIGHT:
            self.rect.y = self.rect.y - HEIGHT
            self.rect.x = random.randrange(0, WIDTH - 85)
        self.rect.x += self.speed
        if self.rect.right > WIDTH:
            self.speed = -5
        elif self.rect.x < 0:
            self.speed = 5


class BreakingPlatform(Platform):

    def __init__(self, x, y, all_sprites):
        super().__init__(x, y, all_sprites)
        self.falling = False
        self.fall_speed = 10

    def update(self):
        if self.rect.y >= HEIGHT:
            self.falling = False
            self.fall_speed = 10
            self.rect.y = self.rect.y - HEIGHT
            self.rect.x = random.randrange(0, WIDTH - 85)
        if self.falling:
            self.rect.y += self.fall_speed
            self.fall_speed += 1


class TeleportingPlatform(Platform):

    def __init__(self, x, y, all_sprites):
        super().__init__(x, y, all_sprites)

    def update(self):
        if self.rect.y >= HEIGHT:
            self.rect.y = self.rect.y - HEIGHT
            self.rect.x = random.randrange(0, WIDTH - 85)

    def teleport(self):
        self.rect.y = random.randrange(0, HEIGHT)
        self.rect.x = random.randrange(0, WIDTH)
