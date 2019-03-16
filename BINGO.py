import random
import time
import tkinter

master = tkinter.Tk()
screen = tkinter.Canvas(master, width=800, height=500, bg='white')  
screen.pack()

text = [0] * 5
alive = True
counter = 0
my_numbers = [0] * 5
bingo_num = 0
"""
set up a row with different sections
list of random numbers to fill sections
while alive:
    generate random numbers
    if random number = to any number in list
    then add to counter
else
    loop back again until there are enough guessed numbers to window_height
"""

def draw_grid():
    screen.create_rectangle(150, 240, 650, 320, width=5, fill='white')
    screen.create_rectangle(350, 50, 450, 100, width=5, fill='white')      
    for i in range(len(my_numbers)-1):
        screen.create_line((i*100)+250, 240, (i*100)+250, 320)

def random_num():
    for i in range(len(my_numbers)):
        my_numbers[i] = random.randint(1, 20)
        #print(my_numbers[i])

def write_numbers():
    #print("works")
    for i in range(len(my_numbers)):
        onwards = (i+2) * 100
        text[i] = screen.create_text(onwards, 280, text = my_numbers[i])  

def bingo_number():
    bingo_num = random.randint(1, 20)
    bintext = screen.create_text(400, 75, text = bingo_num)
    #bintext.delete()   doesnt work
    print(bingo_num)
    return bingo_num
    
def check_numbers(bing):
    for i in range(len(my_numbers)):
        if bing == my_numbers[i]:
            my_numbers[1] = 0.01
            #print("BINGO")
            
draw_grid()
random_num()
write_numbers()
bingo_number()
def looping():
    write_numbers()
    bing = bingo_number()
    check_numbers(bing)
    print("hello")
    button.after(1000, looping)
button = tkinter.Button(screen)
screen.create_window(10, 10, window=button)
button.after(1000, looping)
#write_numbers()
print("hello")

screen.mainloop()