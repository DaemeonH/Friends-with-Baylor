from graphics import *

win = GraphWin("My Test", 400, 400)
foe1 = Image(Point(200, 200), "woodsmanfoe.png")
foe1.draw(win)

def player_move():
    global play_center
    global player
    global k
    player = Image(Point(200, 350), "knight.png")
    player.draw(win)

    
    dx, dy = 5, 5

    while True:
        k = win.checkKey()
        if k == 'Left':
            player.move(-dx, 0)
            checkPos()
        elif k == 'Right':
            player.move(dx, 0)
            checkPos()
        elif k == "Up":
            player.move(0, -dy)
            checkPos()
        elif k == "Down":
            player.move(0, dy)
            checkPos()
        elif k == 'period':
            break

    win.close()

def checkPos(): #checks the position of the player and prohibits movement through barriers/foes
    play_center = player.getAnchor()
    foeC = foe1.getAnchor()
    foeH = foe1.getHeight()
    foeW = foe1.getWidth()
    playH = player.getHeight()
    playW = player.getWidth()
    print(play_center.x)
    print(foeC.x - foeW/2 - playW/4)
    if play_center.y == (foeC.y + foeH/2) and \
       play_center.x >= (foeC.x - foeW/2 - playW/4) and \
       play_center.x <= (foeC.x + foeW/2 + playW/4 ):
        while True:
            k = win.checkKey()
            if k == "Up":
                player.move(0, 0)
                print("don't")
                #player.getAnchor()
                win.checkKey()
            elif k == "Down":
                break
    if play_center.y == (foeC.y - foeH/2 - playH/4) and \
       play_center.x >= (foeC.x - foeW/2 - playW/4) and \
       play_center.x <= (foeC.x + foeW/2 + playW/4):
            while True:
                k = win.checkKey()
                if k == "Down":
                    player.move(0, 0)
                    print("don't")
                    #player.getAnchor()
                    win.checkKey()
                elif k == "Up":
                    break 
    if play_center.x == (foeC.x - foeW/2 - playW/4) and \
       play_center.y >= (foeC.y - foeH/2 - playH/4) and \
       play_center.y <= (foeC.y + foeH/2 + playH/4):
            while True:
                k = win.checkKey()
                if k == "Right":
                    player.move(0, 0)
                    print("don't")
                    #player.getAnchor()
                    win.checkKey()
                elif k == "Left":
                    break        
    if play_center.x == (foeC.x + foeW/2 + playW/4) and \
       play_center.y >= (foeC.y - foeH/2 - playH/4) and \
       play_center.y <= (foeC.y + foeH/2 + playH/4):
            while True:
                k = win.checkKey()
                if k == "Left":
                    player.move(0, 0)
                    print("don't")
                    #player.getAnchor()
                    win.checkKey()
                elif k == "Right":
                    break     




def main():
    player_move()


main()
