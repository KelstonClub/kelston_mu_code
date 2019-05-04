alien = Actor("alien")
alien2 = Actor("alien")
alien3 = Actor("alien")

alien.pos = 100, 56
alien.topright = 10, 10

alien2.pos = 175, 160

alien3.pos = 200, 220

WIDTH = 700
HEIGHT = 600

alien.i_want_to_draw = True
alien2.i_want_to_draw = True
alien3.i_want_to_draw = True

alien.speed = 2
alien2.speed = 5
alien3.speed = 3

aliens = [alien, alien2, alien3]

def draw():
    #print(i_want_to_draw_alien2)
    screen.fill((250,100,250))
    for something in aliens:
        if something.i_want_to_draw:
            something.draw()


def update():
    for alien in aliens:
        alien.left += alien.speed

    for alien in aliens:
        if alien.left > WIDTH:
            alien.i_want_to_draw = False

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("Collition")
    else:
        print("You missed")

