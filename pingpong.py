from pygame import *
from random import *

class GameSprite(sprite.Sprite):
    def __init__(self, pic_image, speed, x, y, p, q):
        super().__init__()
        self.image = transform.scale(image.load(pic_image), (p, q))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.p = p
        self.q = q
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def dwij1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >0:
            self.rect.y -= 5
        if keys_pressed[K_s]and self.rect.y <350:
            self.rect.y += 5
    def dwij2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >0:
            self.rect.y -= 5
        if keys_pressed[K_DOWN]and self.rect.y < 350:
            self.rect.y += 5
class Enemy(GameSprite):
    def zlo(self):
        if self.rect.x < 500:
            self.rect.x += self.speed
        if self.rect.x == 500:
            self.rect.x -= self.speed


win = display.set_mode((700, 500))
display.set_caption("Pingpong")
bk = transform.scale(image.load("fon.png"), (700, 500))


r1 = Player("r1.png", 5, 50, 180, 40, 150)
r2 = Player("r2.png", 5, 600, 180, 40, 150)
s1 = Enemy("ball.png", 200, 320, 180, 60, 60)

game = True

clock = time.Clock()
FPS = 60
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    win.blit(bk,(0,0))
    r1.reset()
    r1.dwij1()
    r2.reset()
    r2.dwij2()
    s1.reset()
    s1.zlo()


    display.update()          
    clock.tick(FPS)