import pygame
from pygame import *
import pyganim
import blocks

JUMP_POWER = 7
GRAVITY = 0.3
MOVE_SPEED = 7
WIDTH = 72
HEIGHT = 90
COLOR = "#888888"

ANIMATION_DELAY = 0.08
ANIMATION_RIGHT = [('Image\Hero\Run\Hero_run_right1.png'),
            ('Image\Hero\Run\Hero_run_right2.png'),
            ('Image\Hero\Run\Hero_run_right3.png'),
            ('Image\Hero\Run\Hero_run_right4.png'),
            ('Image\Hero\Run\Hero_run_right5.png'),
            ('Image\Hero\Run\Hero_run_right6.png')]
ANIMATION_LEFT = [('Image\Hero\Run\Hero_run_left1.png'),
            ('Image\Hero\Run\Hero_run_left2.png'),
            ('Image\Hero\Run\Hero_run_left3.png'),
            ('Image\Hero\Run\Hero_run_left4.png'),
            ('Image\Hero\Run\Hero_run_left5.png'),
            ('Image\Hero\Run\Hero_run_left6.png')]
ANIMATION_JUMP_LEFT = [('Image\Hero\Jump\Hero_jump_left3.png', 0.1)]
ANIMATION_JUMP_RIGHT = [('Image\Hero\Jump\Hero_jump_right3.png', 0.1)]
ANIMATION_JUMP = [('Image\Hero\Idle\Hero_idle1.png', 0.1)]
ANIMATION_STAY = [('Image\Hero\Idle\Hero_idle1.png'),
            ('Image\Hero\Idle\Hero_idle2.png'),
            ('Image\Hero\Idle\Hero_idle3.png'),
            ('Image\Hero\Idle\Hero_idle4.png')]
ANIMATION_ATTACK_RIGHT = [('Image\Hero\Attack\Hero_attack_right1.png'),
                          ('Image\Hero\Attack\Hero_attack_right2.png'),
                          ('Image\Hero\Attack\Hero_attack_right3.png'),
                          ('Image\Hero\Attack\Hero_attack_right4.png'),
                          ('Image\Hero\Attack\Hero_attack_right5.png'),
                          ('Image\Hero\Attack\Hero_attack_right6.png')]
ANIMATION_ATTACK_LEFT = [('Image\Hero\Attack\Hero_attack_left1.png'),
                          ('Image\Hero\Attack\Hero_attack_left2.png'),
                          ('Image\Hero\Attack\Hero_attack_left3.png'),
                          ('Image\Hero\Attack\Hero_attack_left4.png'),
                          ('Image\Hero\Attack\Hero_attack_left5.png'),
                          ('Image\Hero\Attack\Hero_attack_left6.png')]
ANIMATION_LADDER = [('Image\Hero\Ladder\Adventurer-ladder-climb-00.png'),
            ('Image\Hero\Ladder\Adventurer-ladder-climb-01.png'),
            ('Image\Hero\Ladder\Adventurer-ladder-climb-02.png'),
            ('Image\Hero\Ladder\Adventurer-ladder-climb-03.png')]


class Player(sprite.Sprite):
    def __init__(self, x, y, screen, level):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.startX = x
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.yvel = 0
        self.onGround = False
        self.image.set_colorkey(Color(COLOR))
        self.onStairs = False
        self.live = 10
        self.screen = screen
        self.C = 0
        self.c1 = False
        self.c2 = False
        self.c3 = False
        self.c4 = False
        self.c5 = False
        self.c6 = False
        self.c7 = False
        self.c8 = False
        self.c9 = False
        self.level = level
        self.l1 = True
        self.l2 = True
        self.l3 = True

        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY + 0.03))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()

        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY + 0.03))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        boltAnim = []
        for anim in ANIMATION_STAY:
            boltAnim.append((anim, ANIMATION_DELAY + 0.1))
        self.boltAnimStay = pyganim.PygAnimation(boltAnim)
        self.boltAnimStay.play()

        boltAnim = []
        for anim in ANIMATION_LADDER:
            boltAnim.append((anim, ANIMATION_DELAY + 0.1))
        self.boltAnimLadder = pyganim.PygAnimation(boltAnim)
        self.boltAnimLadder.play()

        boltAnim = []
        for anim in ANIMATION_ATTACK_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY + 0.04))
        self.boltAnimAttackRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimAttackRight.play()

        boltAnim = []
        for anim in ANIMATION_ATTACK_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY + 0.04))
        self.boltAnimAttackLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimAttackLeft.play()

        self.boltAnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()

        self.boltAnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()

        self.boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play()

    def update(self, left, right, up, w_up, s_down, platforms):

        intro_text = ["Live: " + str(self.live)]
        self.font = pygame.font.Font('C:\\WINDOWS\\Fonts\\impact.ttf', 30)
        text_coord = 30
        for line in intro_text:
            string_rendered = self.font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 30
            text_coord += intro_rect.height
            self.screen.blit(string_rendered, intro_rect)

        intro_text = ["Level: " + str(self.level + 1)]
        text_coord = 30
        for line in intro_text:
            string_rendered = self.font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 140
            text_coord += intro_rect.height
            self.screen.blit(string_rendered, intro_rect)

        intro_text = ["Coins: " + str(self.C)]
        text_coord = 30
        for line in intro_text:
            string_rendered = self.font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 250
            text_coord += intro_rect.height
            self.screen.blit(string_rendered, intro_rect)

        if self.onStairs:
            self.image.fill(Color(COLOR))
            self.boltAnimLadder.blit(self.image, (0, 0))
            if w_up:
                self.yvel = -MOVE_SPEED + 3
            if s_down:
                self.yvel = MOVE_SPEED - 3

        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER
            self.image.fill(Color(COLOR))
            self.boltAnimJump.blit(self.image, (0, 0))

        if left:
            if self.onStairs:
                self.xvel = -3
            else:
                self.xvel = -MOVE_SPEED
            self.image.fill(Color(COLOR))
            if up:
                self.boltAnimJumpLeft.blit(self.image, (0, 0))
            else:
                self.boltAnimLeft.blit(self.image, (0, 0))

        if right:
            if self.onStairs:
                self.xvel = 3
            else:
                self.xvel = MOVE_SPEED
            self.image.fill(Color(COLOR))
            if up:
                self.boltAnimJumpRight.blit(self.image, (0, 0))
            else:
                self.boltAnimRight.blit(self.image, (0, 0))

        if not (left or right):
            self.xvel = 0
            if not up:
                self.image.fill(Color(COLOR))
                self.boltAnimStay.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False
        self.onStairs = False

        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)

        return self.C, self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8, self.c9, self.level, self.live

    def collide(self, xvel, yvel, platforms):

        for p in platforms:
            if sprite.collide_rect(self, p):

                if isinstance(p, blocks.Stairs):
                    self.onStairs = True

                elif isinstance(p, blocks.Flag):
                    if self.l1:
                        self.level += 1
                        self.l1 = False

                elif isinstance(p, blocks.Flag2):
                    if self.l2:
                        self.level += 1
                        self.l2 = False

                elif isinstance(p, blocks.Flag3):
                    if self.l3:
                        self.level += 1
                        self.l3 = False

                elif isinstance(p, blocks.Coin1):
                    if not self.c1:
                        self.C += 1
                        self.c1 = True

                elif isinstance(p, blocks.Coin2):
                    if not self.c2:
                        self.C += 1
                        self.c2 = True

                elif isinstance(p, blocks.Coin3):
                    if not self.c3:
                        self.C += 1
                        self.c3 = True

                elif isinstance(p, blocks.Coin4):
                    if not self.c4:
                        self.C += 1
                        self.c4 = True

                elif isinstance(p, blocks.Coin5):
                    if not self.c5:
                        self.C += 1
                        self.c5 = True

                elif isinstance(p, blocks.Coin6):
                    if not self.c6:
                        self.C += 1
                        self.c6 = True

                elif isinstance(p, blocks.Coin7):
                    if not self.c7:
                        self.C += 1
                        self.c7 = True

                elif isinstance(p, blocks.Coin8):
                    if not self.c8:
                        self.C += 1
                        self.c8 = True

                elif isinstance(p, blocks.Coin9):
                    if not self.c9:
                        self.C += 1
                        self.c9 = True

                elif xvel > 0:
                    self.rect.right = p.rect.left

                elif xvel < 0:
                    self.rect.left = p.rect.right

                elif yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0

                elif yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0

                if isinstance(p, blocks.BlockDie):
                    self.die()

    def die(self):
        time.wait(360)
        self.live -= 1
        self.teleporting(self.startX, self.startY)

    def teleporting(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY
