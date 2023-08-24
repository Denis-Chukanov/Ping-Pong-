from random import randint

import pygame
import time
pygame.init()

win_width, win_height = 700, 500

window = pygame.display.set_mode((win_width, win_height))
FPS = 60
clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, image, speed):
        super().__init__()
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.transform.scale(image, (w, h))
        self.speed = speed
    
    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, x, y, w, h, image, speed,):
        super().__init__( x, y, w, h, image, speed) 

    def move(self, up, down):
        k = pygame.key.get_pressed()
        if k[up] and self.rect.y >= 0:
            self.rect.y -= 5
        if k[down] and (win_width - self.rect.y) >= self.rect.w:
            self.rect.x y += 5

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    pygame.display.update()
    clock.tick(FPS)