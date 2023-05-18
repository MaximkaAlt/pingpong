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


font.init()
font = font.Font(None, 50)

win = display.set_mode((700, 500))
display.set_caption("Pingpong")
bk = transform.scale(image.load("fon.png"), (700, 500))


r1 = Player("r1.png", 5, 50, 180, 70, 150)
r2 = Player("r2.png", 5, 600, 180, 70, 150)
s1 = Player("ball.png", 3, 320, 180, 60, 60)
speed_x = 7
speed_y = 7
game = True



a= 0
b= 0

clock = time.Clock()
FPS = 60
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    win.blit(bk,(0,0))
    r2.reset()
    r1.reset()
    s1.reset()
    if finish != True:
        r1.dwij1()
        r2.dwij2()
        s1.rect.x+= speed_x
        s1.rect.y+= speed_y
    if s1.rect.y> 450 or s1.rect.y <0:
        speed_y*= -1
    if s1.rect.x> 650 :
        speed_x*= -1
        a+=1
    if s1.rect.x <0:
        speed_x*= -1
        b+= 1  
    if sprite.collide_rect(r1, s1) or sprite.collide_rect(r2, s1):
        speed_x*=-1
    if a > 2:
        win1 = font.render("Second player lose", True, (0, 0, 0))
        win.blit(win1, (210, 240))
        finish = True
        a = 3
    if b > 2:
        win1 = font.render("First player lose", True, (0, 0, 0))
        win.blit(win1, (210, 230))
        finish = True
        b = 3
    win2 = font.render("First:", True, (0,0,0))
    win.blit(win2, (10, 10))
    win4 = font.render(str(b), True, (0,0,0))
    win.blit(win4, (100, 10))
    win3 = font.render("Second:", True, (0,0,0))
    win.blit(win3, (10, 60))
    win5 = font.render(str(a), True, (0,0,0))
    win.blit(win5, (150, 60))
    display.update()           
    clock.tick(FPS)


            