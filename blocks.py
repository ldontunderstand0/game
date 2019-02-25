import pygame
from pygame import *
import pyganim

BACKGROUND_COLOR = "#00a693"
PLATFORM_WIDTH = 64
PLATFORM_HEIGHT = 64
PLATFORM_COLOR = "#FF6262"
COLOR =  "#888888"

ANIMATION_PEAK = [('Image/Traps/Peak3.png'),
                  ('Image/Traps/Peak2.png'),
                  ('Image/Traps/Peak1.png'),
                  ('Image/Traps/Peak2.png')]
ANIMATION_COIN = [('Image/Traps/Coin/coin_1.png'),
                  ('Image/Traps/Coin/coin_2.png'),
                  ('Image/Traps/Coin/coin_3.png'),
                  ('Image/Traps/Coin/coin_4.png')]


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = image.load("Image/Blocks/Block0.0.png")
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class BlockDie(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(x + 8, y + 32, PLATFORM_WIDTH, PLATFORM_HEIGHT)
        self.image = image.load("Image/Traps/Peak1.png")
        boltAnim = []
        for anim in ANIMATION_PEAK:
            boltAnim.append((anim, 0.3))
        self.boltAnim = pyganim.PygAnimation(boltAnim)
        self.boltAnim.play()

    def update(self):
        self.boltAnim.blit(self.image, (0, 0))


class Dirt1(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("Image/Blocks/Dirt1.png")


class Barrier(Platform):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


class Stairs(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT * 4))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT * 4)
        self.image = image.load("Image/Traps/Stairs/Stairs.png")


class Coin1(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(x, y, PLATFORM_WIDTH - 24, PLATFORM_HEIGHT - 12)
        self.image = image.load("Image/Traps/Coin/coin_1.png")


class Coin2(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(x, y, PLATFORM_WIDTH - 24, PLATFORM_HEIGHT - 12)
        self.image = image.load("Image/Traps/Coin/coin_1.png")


class Coin3(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(x, y, PLATFORM_WIDTH - 24, PLATFORM_HEIGHT - 12)
        self.image = image.load("Image/Traps/Coin/coin_1.png")


class Coin4(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(x, y, PLATFORM_WIDTH - 24, PLATFORM_HEIGHT - 12)
        self.image = image.load("Image/Traps/Coin/coin_1.png")


class Coin5(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(x, y, PLATFORM_WIDTH - 24, PLATFORM_HEIGHT - 12)
        self.image = image.load("Image/Traps/Coin/coin_1.png")


class Coin6(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(x, y, PLATFORM_WIDTH - 24, PLATFORM_HEIGHT - 12)
        self.image = image.load("Image/Traps/Coin/coin_1.png")


class Coin7(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(x, y, PLATFORM_WIDTH - 24, PLATFORM_HEIGHT - 12)
        self.image = image.load("Image/Traps/Coin/coin_1.png")


class Coin8(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(x, y, PLATFORM_WIDTH - 24, PLATFORM_HEIGHT - 12)
        self.image = image.load("Image/Traps/Coin/coin_1.png")


class Coin9(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(x, y, PLATFORM_WIDTH - 24, PLATFORM_HEIGHT - 12)
        self.image = image.load("Image/Traps/Coin/coin_1.png")


class Flag(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(x, y, 56, 52)
        self.image = image.load("Image/Traps/flag_3.png")


class Flag2(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(x, y, 56, 52)
        self.image = image.load("Image/Traps/flag_3.png")


class Flag3(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(x, y, 56, 52)
        self.image = image.load("Image/Traps/flag_3.png")
