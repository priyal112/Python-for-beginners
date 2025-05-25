import pygame

#initialize
pygame.init()

#colours
White = (255, 255, 255) #numbers for creating colours
Darkblue = (36, 90, 190)
Lightblue = (0, 176, 240)
Red = (255, 0, 0)

#create bricks

#rect is the class which is used for creating rectangle
bricks1 = [pygame.Rect(10+i*100, 60, 80, 30) for i in range(6)] # rect(x, y, width, hight)
bricks2 = [pygame.Rect(10+i*100, 100, 80, 30) for i in range(6)]
bricks3 = [pygame.Rect(10+i*100, 140, 80, 30) for i in range(6)]

# brick draw on screen

def draw_brick(bricks):
    for i in bricks:
        pygame.draw.rect(screen, Red, i)

score = 0
velocity = [1,1]
size = (600, 600)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("My bricks game")

paddle = pygame.Rect(100, 550, 200, 10)

ball = pygame.Rect(50, 250, 10, 10)

gameContinue = True

while gameContinue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameContinue = False

    screen.fill(Darkblue)

    pygame.draw.rect(screen, Lightblue, paddle)

    font = pygame.font.Font(None, 34)  #for scorce
    text = font.render("SCORE "+ str(score), 1, White)

    screen.blit(text, (20,10))


# paddle move
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if paddle.x < 540:
                paddle.x = paddle.x + 5

        if event.key == pygame.K_LEFT:
            if paddle.x > 0:
                paddle.x = paddle.x - 5
    
    # creating bricks
    draw_brick(bricks1)
    draw_brick(bricks2)
    draw_brick(bricks3)

    #paddle movement
    ball.x = ball.x + velocity[0]
    ball.y = ball.y + velocity[1]

    if ball.x > 590 or ball.x < 0:
        velocity[0] == - velocity[0]

    if ball.y <=3:
        velocity[1] == - velocity[1]

    if paddle.collidepoint(ball.x, ball.y):
        velocity[1] == - velocity[1]

    if ball.y >= 590:
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", 1, Red)
        screen.blit(text, (150, 350))
        pygame.display.flip()

        pygame.time.wait(2000)

        break;
    pygame.draw.rect(screen, White, ball)

    for i in bricks1:
        if i.collidepoint(ball.x, ball.y):
            bricks1.remove(i)
            velocity[0] == - velocity[0]
            velocity[1] == - velocity[1]
            score = score + 1  

    for i in bricks2:
        if i.collidepoint(ball.x, ball.y):
            bricks2.remove(i)
            velocity[0] == - velocity[0]
            velocity[1] == - velocity[1]
            score = score + 1  

    for i in bricks3:
        if i.collidepoint(ball.x, ball.y):
            bricks3.remove(i)
            velocity[0] == - velocity[0]
            velocity[1] == - velocity[1]
            score = score + 1  

    if score == 18:
        font = pygame.font.Font(None, 74)
        text = font.render("You Won", 1, Red)
        screen.blit(text, (150, 350))
        pygame.display.flip()

        pygame.time.wait(3000)

        break;

    pygame.time.wait(1)
    pygame.display.flip()

pygame.quit()
