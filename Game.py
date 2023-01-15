import random
from Config import *
import pygame as pg
from Doodler import Doodler
from Platform import Platform


def game_over_message(surface, doodler_score):
    game_over_text1 = game_over_font.render(f'GAME OVER', True, 'black')
    score_text2 = font.render(f'YOUR SCORE: {doodler_score}', True, 'black')
    press_space_text3 = restart_font.render(f'Press space to restart', True, 'black')
    pg.draw.rect(surface, (171, 194, 112), (0, 350, WIDTH, 240))
    surface.blit(game_over_text1, ((WIDTH - game_over_text1.get_width()) // 2, 400))
    surface.blit(score_text2, ((WIDTH - score_text2.get_width()) // 2, 500))
    surface.blit(press_space_text3, ((WIDTH - press_space_text3.get_width()) // 2, 950))


def create_platforms(platform_group, sprites_group):
    platform_group.add(Platform(255, 985, sprites_group))
    for _ in range(10):
        platform_group.add(Platform(random.randrange(0, WIDTH - 85),
                                    random.randrange(0, HEIGHT - 115, 15), sprites_group))


def restart(doodler, platforms: pg.sprite.Group):
    doodler.restart()
    for platform in platforms:
        platform.restart()
    platforms.sprites()[0].rect.x = 255
    platforms.sprites()[0].rect.y = 985


def play(screen):
    clock = pg.time.Clock()
    all_sprites = pg.sprite.Group()
    platforms = pg.sprite.Group()
    doodler = Doodler(WIDTH // 2 - 50, HEIGHT - 115, all_sprites)
    create_platforms(platforms, all_sprites)
    score = max_doodler_y = game_over = 0

    # Main loop
    while True:
        screen.fill('white')

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and game_over:
                restart(doodler, platforms)
                score = max_doodler_y = game_over = 0

        platforms.draw(screen)
        platforms.update()

        doodler.move(pg.key.get_pressed())
        doodler.update(platforms)
        doodler.render(screen)

        # Camera
        if doodler.jump_power < 0 and doodler.rect.y < HEIGHT // 3:
            while doodler.rect.y < HEIGHT // 3:
                max_doodler_y -= 1
                for sprite in all_sprites.sprites():
                    sprite.rect.y += 1

        # Update score
        if doodler.jump_power == 0 and HEIGHT - doodler.rect.y > max_doodler_y:
            score += HEIGHT - doodler.rect.y - max_doodler_y
            max_doodler_y = HEIGHT - doodler.rect.y

        # Show score
        score_label = font.render(f"Score: {score}", True, 'black')
        screen.blit(score_label, (10, 10))

        # Game over check
        if doodler.rect.y > HEIGHT:
            game_over = True

        if game_over:
            game_over_message(screen, score)

        pg.display.update()
        clock.tick(FPS)
