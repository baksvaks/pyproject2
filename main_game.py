import pygame
from random import randint
import json

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos):
        self.rc = randint(1, 3)
        if self.rc == 1:
            color = "blue"
        elif self.rc == 2:
            color = "red"
        else:
            color = "purple"
        super().__init__(all_sprites)
        self.r = 7
        self.image = pygame.Surface((2 * self.r, 2 * self.r), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color(color), (self.r, self.r), self.r)
        self.rect = pygame.Rect(pos[0], pos[1], 2 * self.r, 2 * self.r)
        self.vx = randint(-15, 15)
        self.vy = randint(-15, 15)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horiz):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vert):
            self.vx = -self.vx

class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:
            self.add(vert)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horiz)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)
class MainGame:
    def __init__(self):
        pygame.init()
        size = w, h = 600, 600
        screen = pygame.display.set_mode(size)
        fps = pygame.time.Clock()
        all_sprites = pygame.sprite.Group()
        vert = pygame.sprite.Group()
        horiz = pygame.sprite.Group()
        u = Border(5, 5, w - 5, 5)
        l = Border(5, 5, 5, h - 5)
        r = Border(w - 5, 5, w - 5, h - 5)
        d = Border(5, h - 5, w - 5, h - 5)
        run = True
        while run:
            screen.fill(pygame.Color('white'))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if (event.type == pygame.MOUSEBUTTONDOWN and
                        ((event.pos[0] > 20 and event.pos[1] > 20) and (
                                event.pos[0] < w - 20 and event.pos[1] < h - 20))):
                    Ball(event.pos)
                    print(event.pos)
            all_sprites.draw(screen)
            all_sprites.update()
            pygame.display.flip()
            fps.tick(30)
        pygame.quit()

if __name__ == '__main__':
    with open('size.json') as sizef:
        data = json.load(sizef)
        for key, value in data.items():
            w, h = int(value[0]), int(value[1])
    if w > 1000:
        w = 1000
    if h > 1000:
        h = 1000
    if w < 100:
        w = 100
    if h < 100:
        h = 100
    size = w, h
    pygame.init()
    screen = pygame.display.set_mode(size)
    fps = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    vert = pygame.sprite.Group()
    horiz = pygame.sprite.Group()
    u = Border(5, 5, w - 5, 5)
    l = Border(5, 5, 5, h - 5)
    r = Border(w - 5, 5, w - 5, h - 5)
    d = Border(5, h - 5, w - 5, h - 5)
    run = True
    while run:
        screen.fill(pygame.Color('white'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if (event.type == pygame.MOUSEBUTTONDOWN and
                    ((event.pos[0] > 20 and event.pos[1] > 20) and (event.pos[0] < w - 20 and event.pos[1] < h - 20))):
                Ball(event.pos)
                print(event.pos)
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        fps.tick(30)
    pygame.quit()