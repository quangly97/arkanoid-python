# Arkanoid Game
<div style="width:360px;max-width:100%;"><div style="height:0;padding-bottom:111.39%;position:relative;"><iframe width="360" height="401" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameBorder="0" src="https://imgflip.com/embed/49mwvu"></iframe></div><p><a href="https://imgflip.com/gif/49mwvu">via Imgflip</a></p></div>

## Brief
An arkanoid game implemented with python and its pygame library.

## Classes
* Paddle
    * __init__(self, color, width, height)
    * move_left(self, distance)
    * move_right(self, distance)
* Ball
    * __init__(self, color, width, height)
    * move(self)
    * bounce(self)
    * reset(self)
* Block
    * __init__(self, color, width, height)
    * set_life(self)

## Technologies Used
* Python
* Git
* Github
* pygame

## Sample Code
```
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
```
