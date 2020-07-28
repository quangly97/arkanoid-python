import pygame
from random import randint

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
GREEN = (0, 255, 0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, (0, 0, width, height))
        self.rect = self.image.get_rect()

    def move_left(self, distance):
        self.rect.x -= distance
        if self.rect.x <= 0:
            self.rect.x = 0

    def move_right(self, distance):
        self.rect.x += distance
        if self.rect.x >= 550:
            self.rect.x = 550

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, (0, 0, width, height))
        self.rect = self.image.get_rect()
        self.dx = randint(-8, 8)
        self.dy = randint(-8, 8)

    def bounce(self):
        self.dy *= -1
        self.dx = randint(-8, 8)

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def reset(self):
        self.rect.x = 320
        self.rect.y = 400

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, (0, 0, width, height))
        self.rect = self.image.get_rect()
        self.life = 1

    def set_life(self, life):
        self.life = life

width = 650
height = 700
size = (width, height)
screen = pygame.display.set_mode(size)
alive = 3
score = 0

paddle = Paddle(WHITE, 100, 10)
paddle.rect.x = 275
paddle.rect.y = 600
ball = Ball(WHITE, 10, 10)
ball.rect.x = 320
ball.rect.y = 400

blocks_list = pygame.sprite.Group()
x = 13
y = 6
BLOCK_WIDTH = 50
BLOCK_HEIGHT = 20
OFFSET = 80

for i in range(x):
    for j in range(y):
        if j == 0:
            block = Block(GREY, BLOCK_WIDTH, BLOCK_HEIGHT)
            block.set_life(2)
        elif j == 1:
            block = Block(RED, BLOCK_WIDTH, BLOCK_HEIGHT)
        elif j == 2:
            block = Block(YELLOW, BLOCK_WIDTH, BLOCK_HEIGHT)
        elif j == 3:
            block = Block(BLUE, BLOCK_WIDTH, BLOCK_HEIGHT)
        elif j == 4:
            block = Block(MAGENTA, BLOCK_WIDTH, BLOCK_HEIGHT)
        elif j == 5:
            block = Block(GREEN, BLOCK_WIDTH, BLOCK_HEIGHT)
        block.rect.x = i*BLOCK_WIDTH
        block.rect.y = j*BLOCK_HEIGHT + OFFSET
        blocks_list.add(block)

objects_list = pygame.sprite.Group()
objects_list.add(paddle)
objects_list.add(ball)

pygame.init()
clock = pygame.time.Clock()
my_font = pygame.font.SysFont("monospace", 40)

while alive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            paddle.move_left(30)
        elif keys[pygame.K_d]:
            paddle.move_right(30)

    ball.move()

    if ball.rect.x <= 0:
        ball.rect.x = 0
        ball.dx *= -1
    elif ball.rect.x >= 640:
        ball.rect.x = 640
        ball.dx *= -1

    if ball.rect.y <= 0:
        ball.rect.y = 0
        ball.dy *= -1
    elif ball.rect.y >= 690:
        ball.reset()
        alive -= 1
        ball.dy *= -1

    if pygame.sprite.collide_mask(ball, paddle):
        ball.bounce()

    block_collision = pygame.sprite.spritecollideany(ball, blocks_list)

    if block_collision:
        if block_collision.life > 1:
            block_collision.set_life(block_collision.life - 1)
        else:
            blocks_list.remove(block_collision)
        score += 1
        ball.bounce()

    objects_list.update()
    blocks_list.update()

    screen.fill(BLACK)

    label = my_font.render("Score: " + str(score), 1, RED)
    screen.blit(label, (0, 650))
    label = my_font.render("Lives: " + str(alive), 1, RED)
    screen.blit(label, (0, 0))

    objects_list.draw(screen)
    blocks_list.draw(screen)

    pygame.display.update()
    clock.tick(60)

    if alive == 0:
        pygame.time.delay(5000)
