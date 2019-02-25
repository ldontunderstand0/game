import pygame
import os
from pygame import *
import pyganim
import blocks
import player

WIN_WIDTH = 1280
WIN_HEIGHT = 720
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#00a693"

PLATFORM_WIDTH = 64
PLATFORM_HEIGHT = 64

COIN1 = COIN2 = COIN3 = COIN4 = COIN5 = COIN6 = COIN7 = COIN8 = COIN9 = None
COINS = 0
BUTTON_VERIFY = False
PLAY_TIMES = 0
LEVEL = 0
START_X = 200
START_Y = 1000


def load_image(name, color_key=None):
    fullname = os.path.join('Image', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIN_WIDTH / 2, -t+WIN_HEIGHT / 2

    l = min(0, l)
    l = max(-(camera.width-WIN_WIDTH), l)
    t = max(-(camera.height-WIN_HEIGHT), t)
    t = min(0, t)

    return Rect(l, t, w, h)


def finish(screen):

    global BUTTON_VERIFY

    BUTTON_VERIFY = 2

    screen.fill((0, 0, 0))

    font = pygame.font.Font('C:\\WINDOWS\\Fonts\\impact.ttf', 100)
    text = font.render("YOU WON!", True, (255, 255, 255))
    screen.blit(text, [440, 75])

    c_x, c_y, c_wight, c_hight = (490, 420, 300, 90)
    font = pygame.font.Font('C:\\WINDOWS\\Fonts\\impact.ttf', 75)
    text = font.render("Continue", True, (255, 255, 255))
    screen.blit(text, [500, 420])
    pygame.draw.rect(screen, (255, 255, 255), (490, 420, 300, 90), 1)

    font = pygame.font.Font('C:\\WINDOWS\\Fonts\\impact.ttf', 100)
    text = font.render("Thanks for playing!", True, (255, 255, 255))
    screen.blit(text, [240, 175])

    pygame.display.flip()

    return c_x, c_y, c_wight + c_x, c_hight + c_y


def menu(screen):

    global BUTTON_VERIFY

    BUTTON_VERIFY = 0

    screen.fill((0, 0, 0))

    play_x, play_y, play_wight, play_hight = (560, 270, 160, 90)
    font = pygame.font.Font('C:\\WINDOWS\\Fonts\\impact.ttf', 75)
    text = font.render("PLAY", True, (255, 255, 255))
    screen.blit(text, [570, 270])
    pygame.draw.rect(screen, (255, 255, 255), (560, 270, 160, 90), 1)

    ex_x, ex_y, ex_wight, ex_hight = (560, 420, 160, 90)
    font = pygame.font.Font('C:\\WINDOWS\\Fonts\\impact.ttf', 75)
    text = font.render("EXIT", True, (255, 255, 255))
    screen.blit(text, [580, 420])
    pygame.draw.rect(screen, (255, 255, 255), (560, 420, 160, 90), 1)

    font = pygame.font.Font('C:\\WINDOWS\\Fonts\\impact.ttf', 100)
    text = font.render("DANGEROUS ADVENTURE", True, (255, 255, 255))
    screen.blit(text, [145, 75])

    pygame.display.flip()

    return play_x, play_y, play_wight + play_x, play_hight + play_y, ex_x, ex_y, ex_wight + ex_x, ex_hight + ex_y


def level_update(screen):

    global BUTTON_VERIFY, LEVEL, COINS

    BUTTON_VERIFY = 3

    screen.fill((0, 0, 0))

    font = pygame.font.Font('C:\\WINDOWS\\Fonts\\impact.ttf', 100)
    text = font.render("LEVEL {} COMPLITE!".format(LEVEL + 1), True, (255, 255, 255))
    screen.blit(text, [300, 75])

    c_x, c_y, c_wight, c_hight = (490, 420, 300, 90)
    font = pygame.font.Font('C:\\WINDOWS\\Fonts\\impact.ttf', 75)
    text = font.render("Continue", True, (255, 255, 255))
    screen.blit(text, [500, 420])
    pygame.draw.rect(screen, (255, 255, 255), (490, 420, 300, 90), 1)

    font = pygame.font.Font('C:\\WINDOWS\\Fonts\\impact.ttf', 100)
    text = font.render("Coins: {} / 3".format(COINS), True, (255, 255, 255))
    screen.blit(text, [420, 175])

    pygame.display.flip()

    return c_x, c_y, c_wight + c_x, c_hight + c_y


def gameover(screen):

    global BUTTON_VERIFY

    BUTTON_VERIFY = 4

    screen.fill((0, 0, 0))

    font = pygame.font.Font('C:\\WINDOWS\\Fonts\\impact.ttf', 100)
    text = font.render("GAMEOVER", True, (255, 255, 255))
    screen.blit(text, [440, 75])

    c_x, c_y, c_wight, c_hight = (520, 420, 275, 90)
    font = pygame.font.Font('C:\\WINDOWS\\Fonts\\impact.ttf', 75)
    text = font.render("RESTART", True, (255, 255, 255))
    screen.blit(text, [530, 420])
    pygame.draw.rect(screen, (255, 255, 255), (520, 420, 275, 90), 1)

    pygame.display.flip()

    return c_x, c_y, c_wight + c_x, c_hight + c_y


def levels(level_score, entities, platforms):

    global COIN1, COIN2, COIN3, COIN4, COIN5, COIN6, COIN7, COIN8, COIN9

    level = ['']
    level1 = [
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "x                                                                                                           x",
        "x                                                        s     k                                            x",
        "x           * c        ---                                    ---                                           x",
        "x         s----               s---      ---                                           s                     x",
        "x                                                 s   ---                                 ---               x",
        "x                                       s                                                                   x",
        "x                                                                       ---                                 x",
        "x         s                  ---s                                                     s                     x",
        "x                                        ---              ---                                               x",
        "x                                                                                                         f x",
        "x                   ---    s  *                                        s----           ---            ------x",
        "x         ---               -----                                                     s                     x",
        "x                                                              ---                                          x",
        "x                                                        ---          *                                     x",
        "x                      *   s                     s---                ---                                    x",
        "x                      ---                  ---                                                 n      ---  x",
        "x                                   ---      -                                                 ---      -   x",
        "x           *                        - *     -     - *                                          -     * - * x",
        "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"]
    level2 = [
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "x                                          g                                                      j         x",
        "x                                         ---   s                                                ---    s   x",
        "x                                                                                                           x",
        "x                                                          ---     ---     ---     ---     ---              x",
        "x                                                      m                                                    x",
        "x                                 s---          s                                                    ---s   x",
        "x                                                                                                           x",
        "x                                                       ---      ---      ---      ---      ---             x",
        "x                              s---                                                                         x",
        "x                                                                                                       s   x",
        "x                                                                                                           x",
        "x                                                                                                           x",
        "x           s                                                          s---                                 x",
        "x            ---      ---                                                                               s   x",
        "x                                                                                                           x",
        "x                                  h                                                                        x",
        "x                                  -      -      -      -      -      ---          -      -      -          x",
        "x         **************************************************************************************************x",
        "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"]
    level3 = [
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "x                                                                                                           x",
        "x       u                                                                                                   x",
        "x      ---    ---                                                                                           x",
        "x                     ---      ---                                                                          x",
        "x                                -b    ---      ---                                                      z  x",
        "x                                ---                    ---      ---                                        x",
        "x                                                                        ---      ---                       x",
        "x                                                                                         ---      ---   s  x",
        "x                                                                                                           x",
        "x                                                                                                           x",
        "x                                                                                                           x",
        "x                                                                                                           x",
        "x                                                                                        ---      ---       x",
        "x                                                                        ---     ---                        x",
        "x               s                                       ---      ---                                        x",
        "x                                      ---      ---                                                         x",
        "x                     ---      ---                                                                          x",
        "x                      -  *     -  *                                                                     v *x",
        "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"]

    level_time = [level1, level2, level3, level]

    for i in range(len(level_time)):
        if i == level_score:
            level = level_time[i]

    total_level_width = len(level[0]) * PLATFORM_WIDTH
    total_level_height = len(level) * PLATFORM_HEIGHT
    camera = Camera(camera_configure, total_level_width, total_level_height)

    y = 0
    x = -64
    for row in level:
        for col in row:
            if col == "-":
                pf = blocks.Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "*":
                bd = blocks.BlockDie(x, y)
                entities.add(bd)
                platforms.append(bd)
            if col == "1":
                pf = blocks.Dirt1(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "x":
                pf = blocks.Barrier(x, y - 64)
                entities.add(pf)
                platforms.append(pf)
            if col == "s":
                pf = blocks.Stairs(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "c":
                COIN1 = blocks.Coin1(x, y)
                entities.add(COIN1)
                platforms.append(COIN1)
            if col == "n":
                COIN2 = blocks.Coin2(x, y)
                entities.add(COIN2)
                platforms.append(COIN2)
            if col == "k":
                COIN3 = blocks.Coin3(x, y)
                entities.add(COIN3)
                platforms.append(COIN3)
            if col == "m":
                COIN4 = blocks.Coin4(x, y)
                entities.add(COIN4)
                platforms.append(COIN4)
            if col == "h":
                COIN5 = blocks.Coin5(x, y)
                entities.add(COIN5)
                platforms.append(COIN5)
            if col == "j":
                COIN6 = blocks.Coin6(x, y)
                entities.add(COIN6)
                platforms.append(COIN6)
            if col == "b":
                COIN7 = blocks.Coin7(x, y)
                entities.add(COIN7)
                platforms.append(COIN7)
            if col == "v":
                COIN8 = blocks.Coin8(x, y)
                entities.add(COIN8)
                platforms.append(COIN8)
            if col == "z":
                COIN9 = blocks.Coin9(x, y)
                entities.add(COIN9)
                platforms.append(COIN9)
            if col == "f":
                a = blocks.Flag(x, y)
                entities.add(a)
                platforms.append(a)
            if col == "g":
                a = blocks.Flag2(x, y)
                entities.add(a)
                platforms.append(a)
            if col == "u":
                a = blocks.Flag3(x, y)
                entities.add(a)
                platforms.append(a)
            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = -64

    return level, camera


def main():

    global BUTTON_VERIFY, PLAY_TIMES, LEVEL, START_X, START_Y, COIN1, COIN2, COIN3, COIN4, COIN5, COIN6, COINS

    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("Game")
    pygame.display.set_icon(pygame.image.load("Image\Ico\caesar.png"))
    timer = pygame.time.Clock()

    hero = None
    camera = None
    fon = pygame.transform.scale(load_image('Ico\cyberpunk-street.png'), (WIN_WIDTH + 300, WIN_HEIGHT))
    play_x, play_y, play_wight_x, play_hight_y, exit_x, exit_y, exit_wight_x, exit_hight_y = menu(screen)
    left = right = up = w_up = s_down = False
    c_x = c_y = c_wight_x = c_hight_y = None
    animatedEntities = pygame.sprite.Group()
    entities = pygame.sprite.Group()
    platforms = []
    tr1 = True
    tr2 = True

    running = True
    while running:

        timer.tick(60)

        for e in pygame.event.get():

            if e.type == QUIT:
                running = False

            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    x_button, y_button = e.pos
                    if exit_wight_x > x_button > exit_x and exit_hight_y > y_button > exit_y and BUTTON_VERIFY == 0:
                        running = False
                    if play_wight_x > x_button > play_x and play_hight_y > y_button > play_y and BUTTON_VERIFY == 0:
                        BUTTON_VERIFY = 1
                        screen.fill((0, 0, 0))
                        if PLAY_TIMES == 0:
                            animatedEntities = pygame.sprite.Group()
                            entities = pygame.sprite.Group()
                            platforms = []
                            hero = player.Player(START_X, START_Y, screen, LEVEL)
                            level, camera = levels(LEVEL, entities, platforms)
                            entities.add(hero)
                            PLAY_TIMES = 1
                    if BUTTON_VERIFY == 2 and c_wight_x > x_button > c_x and c_hight_y > y_button > c_y:
                        menu(screen)
                        PLAY_TIMES = 0
                        BUTTON_VERIFY = 0
                        LEVEL = 0
                    if BUTTON_VERIFY == 3 and c_wight_x > x_button > c_x and c_hight_y > y_button > c_y:
                        BUTTON_VERIFY = 1
                    if BUTTON_VERIFY == 4 and c_wight_x > x_button > c_x and c_hight_y > y_button > c_y:
                        menu(screen)
                        PLAY_TIMES = 0
                        BUTTON_VERIFY = 0
                        LEVEL = 0

            if e.type == pygame.MOUSEMOTION:
                x_button, y_button = e.pos
                if exit_wight_x > x_button > exit_x and exit_hight_y > y_button > exit_y and BUTTON_VERIFY == 0 and tr1:
                    menu(screen)
                    pygame.draw.polygon(screen, (255, 255, 255), [(530, 490), (530, 440), (555, 465)], 0)
                    tr1 = False
                    tr2 = True
                if play_wight_x > x_button > play_x and play_hight_y > y_button > play_y and BUTTON_VERIFY == 0 and tr2:
                    menu(screen)
                    pygame.draw.polygon(screen, (255, 255, 255), [(530, 340), (530, 290), (555, 315)], 0)
                    tr1 = True
                    tr2 = False

            if e.type == pygame.KEYDOWN and e.key == 27 and BUTTON_VERIFY == 1:
                pygame.mouse.set_visible(True)
                levels(-1, entities, platforms)
                menu(screen)

            if e.type == KEYDOWN and e.key == 119:
                w_up = True
            if e.type == KEYDOWN and e.key == 115:
                s_down = True
            if e.type == KEYUP and e.key == 119:
                w_up = False
            if e.type == KEYUP and e.key == 115:
                s_down = False
            if e.type == KEYDOWN and e.key == 97:
                left = True
            if e.type == KEYDOWN and e.key == 100:
                right = True
            if e.type == KEYUP and e.key == 100:
                right = False
            if e.type == KEYUP and e.key == 97:
                left = False
            if e.type == KEYDOWN and e.key == 32:
                up = True
            if e.type == KEYUP and e.key == 32:
                up = False

        if BUTTON_VERIFY == 1:
            pygame.mouse.set_visible(False)
            screen.blit(fon, (-100, 0))
            camera.update(hero)
            animatedEntities.update()
            for e in entities:
                screen.blit(e.image, camera.apply(e))
            coins, c1, c2, c3, c4, c5, c6, c7, c8, c9, lev, live = hero.update(left, right, up, w_up, s_down, platforms)
            COINS = coins
            if live == 0:
                pygame.mouse.set_visible(True)
                c_x, c_y, c_wight_x, c_hight_y = gameover(screen)
            if lev != LEVEL:
                if lev == 3:
                    pygame.mouse.set_visible(True)
                    c_x, c_y, c_wight_x, c_hight_y = finish(screen)
                else:
                    pygame.mouse.set_visible(True)
                    c_x, c_y, c_wight_x, c_hight_y = level_update(screen)
                LEVEL = lev
                levels(-1, entities, platforms)
                animatedEntities = pygame.sprite.Group()
                entities = pygame.sprite.Group()
                platforms = []
                hero = player.Player(START_X, START_Y, screen, LEVEL)
                entities.add(hero)
                level, camera = levels(LEVEL, entities, platforms)
            if c1:
                COIN1.kill()
            if c2:
                COIN2.kill()
            if c3:
                COIN3.kill()
            if c4:
                COIN4.kill()
            if c5:
                COIN5.kill()
            if c6:
                COIN6.kill()
            if c7:
                COIN7.kill()
            if c8:
                COIN8.kill()
            if c9:
                COIN9.kill()
        pygame.display.update()


main()
