from random import randint

import pygame
from time import time
pygame.init()

win_width, win_height = 700, 500
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Пинг-понг")
back = pygame.image.load('back.png')
back = pygame.transform.scale(back, (win_width, win_height))

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

class Ball(GameSprite):
    def __init__(self, x, y, w, h, image, speed, x_form, y_form):
        super().__init__(x, y, w, h, image, speed)
        self.x_form = x_form
        self.y_form = y_form
    
    def move(self):
        self.rect.x += self.x_form
        self.rect.y += self.y_form
        if self.rect.y >= 450 or self.rect.y <= 0:
            self.y_form *= -1
    
    def colide(self, item):
        if self.rect.colliderect(item.rect):
            return True
        else:
            return False
class Player(GameSprite):
    def __init__(self, x, y, w, h, image, speed):
        super().__init__( x, y, w, h, image, speed) 

    def move(self, up, down):
        k = pygame.key.get_pressed()
        if k[up] and self.rect.y >= 0:
            self.rect.y -= 5
        if k[down] and self.rect.y <= 400:
            self.rect.y += 5

start_time = time()

ball_pic = pygame.image.load('мяч.png')
ball = Ball(125, 212, 50, 50, ball_pic, 4, 4, 3)

player_pic = pygame.image.load('raketka.png')
player1 = Player(0, 212, 70, 100, player_pic, 4)
player2 = Player(630, 212, 70, 100, player_pic, 4)

player1_score = 0
player2_score = 0

font = pygame.font.SysFont('Arial', 30)
screen = 'menu'
game = True
while game:
    if screen == 'menu':
        new_lb =font.render ("Натисніть ENTER щоб почати", True, (255,0,0)) 
        window.blit(new_lb,(105,200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                screen = 'game'
    if screen == 'pause':
        new_lb =font.render ("Натисніть ENTER щоб продовжити", True, (255,0,0)) 
        window.blit(new_lb,(105,200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                screen = 'game'
    if screen == 'game':
        window.blit(back,(0,0))
        score = font.render('Score ' + str(player1_score) + ':' + str(player2_score), True, (255,0,0)) 
        window.blit(score,(300,0)) 
        ball.update()
        ball.move()
        player1.update()
        player1.move(pygame.K_w, pygame.K_s)
        player2.update()
        player2.move(pygame.K_p, pygame.K_l)
        timer = int(time() - start_time)
        game_time = font.render("Час:" + str(timer), True, (0,250,0))
        window.blit(game_time,(0,0))
        if ball.colide(player1) or ball.colide(player2):
            ball.x_form *= -1
        if ball.rect.x >= 700:
            player1_score += 1
            player1 = Player(0, 212, 70, 100, player_pic, 4)
            player2 = Player(630, 212, 70, 100, player_pic, 4)
            ball = Ball(175, 212, 50, 50, ball_pic, 4, 4, 3)
            screen = 'pause'
        if ball.rect.x <= 0:
            player2_score += 1
            player1 = Player(0, 212, 70, 100, player_pic, 4)
            player2 = Player(630, 212, 70, 100, player_pic, 4)
            ball = Ball(525, 212, 50, 50, ball_pic, 4, -4, 3)
            screen = 'pause'
        if player1_score == 3:
            screen = "over1"
        if player2_score == 3:
            screen = 'over2'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
    if screen == 'over1':
        window.blit(back,(0,0))
        game_over = font.render("Game Over", True, (255,0,0)) 
        window.blit(game_over,(250,50)) 
        new_lb =font.render ("Перемога за 1 гравцем!", True, (255,0,0)) 
        window.blit(new_lb,(155,125))
        new_lb =font.render ("Натисніть ENTER щоб почати знову", True, (255,0,0)) 
        window.blit(new_lb,(105,200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                player1 = Player(0, 212, 70, 100, player_pic, 4)
                player2 = Player(630, 212, 70, 100, player_pic, 4)
                ball = Ball(325, 212, 50, 50, ball_pic, 4, 4, 3)
                player1_score = 0
                player2_score = 0
                screen = 'game'

    if screen == 'over2':
        window.blit(back,(0,0))
        game_over = font.render("Game Over", True, (0,0,255)) 
        window.blit(game_over,(250,50)) 
        new_lb =font.render ("Перемога за 2 гравцем!", True, (0,0,255)) 
        window.blit(new_lb,(155,125))
        new_lb =font.render ("Натисніть ENTER щоб почати знову", True, (0,0,255)) 
        window.blit(new_lb,(105,200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                player1 = Player(0, 212, 70, 100, player_pic, 4)
                player2 = Player(630, 212, 70, 100, player_pic, 4)
                ball = Ball(125, 212, 50, 50, ball_pic, 4, 4, 3)
                player1_score = 0
                player2_score = 0
                game_time = 0
                start_time = time()
                screen = 'game'

    pygame.display.update()
    clock.tick(FPS)