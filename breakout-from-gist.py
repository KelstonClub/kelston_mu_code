WIDTH = 1000
HEIGHT = 570


class Ball(ZRect): pass
class Paddle(ZRect): pass
class LPaddle(ZRect): pass
class RPaddle(ZRect): pass
class Brick(ZRect): pass

##pygame.mixer.music.load(r'E:\david\Music\congratulations.mp3')
##pygame.mixer.music.play(-1)
#ball details:
# music.play("congratulations")

ball = Ball(WIDTH / 4, HEIGHT / 4, 20, 20)
ball.colour = "green"
ball.direction = 1, 1
ball.speed = 5

BAT_W = 150
BAT_H = 15
paddle = Paddle(WIDTH / 2, HEIGHT - BAT_H, BAT_W, BAT_H)
paddle.colour = "orange"

lpaddle = LPaddle(0, HEIGHT / 2, BAT_H, BAT_W)
lpaddle.colour = "blue"

rpaddle = RPaddle(WIDTH - BAT_H, HEIGHT / 2, BAT_H, BAT_W)
rpaddle.colour = "blue"

Num_Brick = 20
Brick_W = WIDTH / 10
Brick_H = Brick_W / 4
BRICK_COLOURS = ["purple", "lightgreen", "lightblue", "orange"]

bricks = []
for i in range(Num_Brick):
    row = (i // 10) + 1
#     print(row)
    brick = Brick(i * Brick_W, row * Brick_H, Brick_W, Brick_H)
    print(brick)
    brick.colour = BRICK_COLOURS[i % len(BRICK_COLOURS)]
    bricks.append(brick)

def draw():
    screen.clear()
    screen.draw.filled_rect(ball, ball.colour)
    screen.draw.filled_rect(paddle, paddle.colour)
    screen.draw.filled_rect(lpaddle,lpaddle.colour)
    screen.draw.filled_rect(rpaddle,rpaddle.colour)

    for brick in bricks:
        screen.draw.filled_rect(brick, brick.colour)

def on_mouse_move(pos):
    x, y = pos
    paddle.centerx = x
    lpaddle.centery = y
    #print(x, y)
    rpaddle.centery = y

def update():
    dx, dy = ball.direction
    ball.move_ip(ball.speed * dx, ball.speed * dy)

    if ball.colliderect(paddle):
        ball.direction = dx, -dy
    if ball.colliderect(lpaddle):
        ball.direction = -dx, dy
    if ball.colliderect(rpaddle):
        ball.direction = -dx, dy


    to_kill = ball.collidelist(bricks)
    if to_kill >= 0:
        bricks.pop(to_kill)
        ball.direction = dx, -dy

    if ball.right >= WIDTH or ball.left <= 0:
        ball.direction = -dx, dy

    #if paddle.right >= WIDTH or paddle.left <= 0:
    #    paddle.direction = -px, py
    #
    if ball.bottom >= HEIGHT or ball.top <= 0:
        ball.direction = dx, -dy

    if ball.bottom >= HEIGHT:
        exit()
    if ball.left <= 0:
        exit()
    if ball.right >= WIDTH:
        exit()

    if ball.top <= 0:
        ball.direction = dx, -dy


    if not bricks:
        exit()
