import turtle
import random
import time

    
def init_alex():
    """defining the turtle in here hopefully will make it so Take_turns can see alex and in turn user_move cant see the turtle"""
    alex = turtle.Turtle()
    alex.shape("turtle")
    alex.pencolor('Blue')
    alex.fillcolor("Blue")
    return alex
def init_alice():
    """defining the turtle in here hopefully will make it so Take_turns can see alice and in turn alice_move cant see the turtle"""
    alice = turtle.Turtle()
    alice.shape("turtle")
    alice.pencolor("Red")
    alice.fillcolor("Red")
    return alice
def use_turtles(alex,alice):
    """A function that allows you to call each turtle without recreating the turtle each time"""
    alex = alex
    alice = alice
    return [alex,alice]
    
def startpoint(turtles, window): #calling window_height_width just window for sanity
    """Function that carries out the movement of each turtle to a random location in the canvas at the start of each game"""
    alex = turtles[0]
    alice = turtles[1]
    max_limit = ((window//2) - 10) # this was it won't land exactly on the edge or outside the window
    alex.up()
    alex.setpos((random.randint(0,max_limit)),(random.randint(0,max_limit)))
    alex.down()
    alice.up()
    alice.setpos((random.randint(0,max_limit)),(random.randint(0,max_limit)))
    alice.down()
    return turtles


def user_move(alex, alice):
    """Function for defining what should happen during the players (alex's) move"""
    op = 0
    while op == 0:
        #old useless code unless you can prompt by string inputs, just using for debugging
        direction = input('prompt:')
        if (('w') or ('W')) is direction:
            alex.fd(30)
            op = 1
            print('forward')
        if (('s') or ('S')) is direction:
            alex.fd(-30)
            op = 1
            print('backward')
        if (('a') or ('A')) is direction:
            alex.lt(45)
            op = 1
            print('left')
        if (('d') or ('D')) is direction:
            alex.rt(45)
            op = 1
            print('right')
        if ('cheat') in direction:
            alex.setpos(alice.pos())
            print('cheater')
            op = 1
        if op == 0:
            op=0
            print('invalid input')
        if op == 2:
            pass

def Alice_move(alice, alex):
    """This will be the function that executes alices move after the player"""
    numb = (random.uniform(1,6))//1
    if alex.pos() == alice.pos():
        pass
    if numb == 1:
        alice.lt(45)
    if numb==2:
        alice.rt(45)
    else:
        alice.fd(30)
    pass

def Take_Turns(turtles):
    """The function that calls each players turns to take place while the game hasn't been won"""
    jeff = turtle.Turtle()
    jeff.up()
    jeff.hideturtle()
    jeff.setpos(-240,220)
    
    win = False
    alex= turtles[0]
    alice= turtles[1]
    jeff.write(('The Distance: ', ((alex.distance(alice,alice)) // 1)), True, align="left")
    while not win:
        user_move(alex, alice)
        Alice_move(alice, alex)
        jeff.clear()
        jeff.write(('The Distance: ', ((alex.distance(alice,alice)) // 1)), True, align="left")
        if ((alex.distance(alice,alice)) // 1) < 100:
            win = True
            jeff.clear()
            jeff.write("You Win")
            time.sleep(3)
            turtle.clearscreen()
            main()


def main():
    window_height_width = 500
    turtle.Screen().setup(window_height_width,window_height_width)
    Take_Turns(startpoint(use_turtles(init_alex(), init_alice()), window_height_width))
    
main()
