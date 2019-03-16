WIDTH = 640
HEIGHT = 480

class Ball(ZRect): pass
class Paddle(ZRect): pass
class Brick(ZRect): pass
#ball details:

ball = Ball(WIDTH / 2, HEIGHT / 2, 30, 30)
ball.colour = "green"
ball.direction = 1, 1
ball.speed = 5

BAT_W = 150
BAT_H = 15
paddle = Paddle(WIDTH / 2, HEIGHT - BAT_H, BAT_W, BAT_H)
paddle.colour = "orange"

SL_paddle = Paddle(0, HEIGHT / 2, BAT_H, BAT_W)
SL_paddle.colour = "blue"

SR_paddle = Paddle(WIDTH - BAT_H, HEIGHT / 2, BAT_H, BAT_W)
SR_paddle.colour = "blue"

Num_Brick = 8
Brick_W = WIDTH / 8
Brick_H = Brick_W / 4
BRICK_COLOURS = ["purple", "lightgreen", "lightblue", "orange"]

bricks = []
for i in range(Num_Brick):
    brick = Brick(i * Brick_W, 0, Brick_W, Brick_H)
    brick.colour = BRICK_COLOURS[i % len(BRICK_COLOURS)]
    bricks.append(brick)

def draw():
    screen.clear()
    screen.draw.filled_rect(ball, ball.colour)
    screen.draw.filled_rect(paddle, paddle.colour)
    screen.draw.filled_rect(SL_paddle,SL_paddle.colour)
    screen.draw.filled_rect(SR_paddle,SR_paddle.colour)

    for brick in bricks:
        screen.draw.filled_rect(brick, brick.colour)

def on_mouse_move(pos):
    x, y = pos
    paddle.centerx = x * (WIDTH / HEIGHT)
    SL_paddle.centrey = y
    #SR_paddle.centrey = y

def update():
    dx, dy = ball.direction
    ball.move_ip(ball.speed * dx, ball.speed * dy)

    if ball.colliderect(paddle):
        ball.direction = dx, -dy

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

    if ball.top <= 0:
        ball.direction = dx, -dy

    if not bricks:
        exit()




