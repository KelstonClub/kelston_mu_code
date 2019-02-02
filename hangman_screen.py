import turtle as t

NUMBER_TO_FAIL = 10

def draw_word(word_so_far):
    pass
    
def draw_hangman(failed_letters):
    pass
    
def draw(word_so_far, failed_letters):
    """Draw the word so far and the hangman

    (Might also draw the list of failed letters)
    Useful:
      reset -- starts again with a clear screen
      write -- writes text to the screen
    """
    t.reset()
    draw_word(word_so_far)
    draw_hangman(failed_letters)

t.speed(4)
t.pensize(6)
t.penup()
t.right(90)
t.forward(100)
t.pencolor("saddle brown")

t.pendown()
t.right(90)
t.forward(100)
t.right(90)
t.forward(200)

t.right(90)
t.forward(200)
t.left(180)
t.forward(150)
t.left(45)
t.forward(70)
t.right(180)
t.forward(70)

t.right(45)
t.forward(50)

t.pencolor("sandy brown")
t.right(90)
t.forward(50)

t.pencolor("firebrick3")
t.circle(10)
t.forward(55)
t.right(45)
t.forward(25)
t.left(180)
t.forward(25)
t.right(90)
t.forward(25)
t.left(180)
t.forward(25)
t.right(45)
t.forward(25)
t.right(90)
t.forward(25)
t.left(180)
t.forward(50)


def get_a_letter():
    """Prompt the user to enter a letter
    """
    #
    # HINT: turtle.textinput might help
    #
    return t.textinput("Hangman", "Set me one").upper()

def get_difficulty():
    """Return a number showing how difficult
    """
    return int(t.textinput("Hangman", "How difficult?"))
