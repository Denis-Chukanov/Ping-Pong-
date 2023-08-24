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



game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    pygame.display.update()
    clock.tick(FPS)