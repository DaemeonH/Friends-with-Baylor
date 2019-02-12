##import sys
##import os
##
##def resource_path(relative_path):
##    """ Get absolute path to resource, works for dev and for PyInstaller """
##    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
##    return os.path.join(base_path, relative_path)


import time
import pygame
from pygame import*
from graphics import*
from intro import*
import intro
pygame.mixer.init()
pauseTime = 2

def title_screen():
    global win
    win = GraphWin("Friends with Baylor", 800, 550)
    win.setBackground("red4")

    baylor = Image(Point(400, 260), "baylor_red_bkgrnd.gif")
    baylor.draw(win)
    
    title = "Friends with Baylor"
    draw_title = Text(Point(400, 50), title)
    draw_title.setFace("courier")
    draw_title.setTextColor("black")
    draw_title.setSize(36)
    draw_title.setStyle("bold italic")
    draw_title.draw(win)
    pygame.mixer.music.load("Edward_Shallow_-_01_-_The_Infinite_Railroad.mp3") 
    pygame.mixer.music.play(-1,0.0)

    by = "DaemeoNation Games"
    draw_by = Text(Point(400, 440), by)
    draw_by.setFace("courier")
    draw_by.setTextColor("orange2")
    draw_by.setSize(18)
    draw_by.setStyle("bold italic")
    draw_by.draw(win)

    start = "Click To Start"
    draw_title = Text(Point(400, 500), start)
    draw_title.setFace("courier")
    draw_title.setTextColor("black")
    draw_title.setSize(12)
    draw_title.setStyle("bold italic")
    draw_title.draw(win)
    
    clickPoint = win.getMouse()
    clear(win)
    #pygame.mixer.music.stop()
    #i know i can fade out the music instead of kill it
    #time.sleep(1)
    #win.close()

def intro_screen():
    win.setBackground("gray4")
    baylor = Image(Point(400, 260), "the-dark-forest-ART2.gif")
    baylor.draw(win)
    str1 = "You travel alone through a dark forest."
    str2 = "On the path ahead,..."
    str3 = "you see a man in leather armor approach."
    str4 = "He carries a large axe!"
    intro_strings = [str1, str2, str3, str4]
    for idx, val in enumerate(intro_strings):
        intro = Text(Point(400, 475), intro_strings[idx])
        intro.setFace("courier")
        intro.setTextColor("red")
        intro.setSize(18)
        intro.setStyle("bold italic")
        intro.draw(win)
        time.sleep(pauseTime)
        intro.undraw()
    clear(win)
    
def intro_screen2():
    win.setBackground("gray3")
    woodsman = Image(Point(400, 260), "woodsman.gif")
    woodsman.draw(win)
    str1 = "Hail, fair traveller!"
    str2 = "I have but one simple question for you."
    str3 = "Are you friends with Baylor?"
    intro_strings2 = [str1, str2, str3]
    for idx, val in enumerate(intro_strings2):
        intro2 = Text(Point(400, 475), intro_strings2[idx])
        intro2.setFace("courier")
        intro2.setTextColor("green4")
        intro2.setSize(18)
        intro2.setStyle("bold italic")
        intro2.draw(win)
        time.sleep(pauseTime)
        intro2.undraw()
    yes_or_no()

def hesitate():
    win.setBackground("gray3")
    woodsman = Image(Point(400, 260), "woodsman.gif")
    woodsman.draw(win)
    str8 = "You hesitate, so I ask again."
    str9 = "Are...you...friends...with...Baylor?"
    intro_strings4 = [str8, str9]
    for idx, val in enumerate(intro_strings4):
        intro4 = Text(Point(400, 475), intro_strings4[idx])
        intro4.setFace("courier")
        intro4.setTextColor("green4")
        intro4.setSize(18)
        intro4.setStyle("bold italic")
        intro4.draw(win)
        time.sleep(pauseTime)
        intro4.undraw()
    yes_or_no()

def yes_or_no():
    str4 = "Answer- 1. 'Yes'" 
    str5 = "       2. 'No'"
    str6 = "                            or 3. 'Who in the HELL is Baylor?'"
    str7 = "         Please enter a 1, 2, or 3." 
    intro_strings3 = [str4, str5, str6, str7]
    textpos_y = 400
    for idx, val in enumerate(intro_strings3):
        intro3 = Text(Point(150, textpos_y), intro_strings3[idx])
        intro3.setFace("courier")
        intro3.setTextColor("red4")
        intro3.setSize(18)
        intro3.setStyle("bold italic")
        intro3.draw(win)
        textpos_y = textpos_y + 30
    answer = Entry(Point(450, 490), 4)
    answer.draw(win)
    inputStr = win.getKey()
    clear(win)
    try:
        int_answer = int(inputStr)
        if int_answer < 1 or int_answer > 3:
            hesitate()
        if int_answer >= 1 and int_answer <=4:
            if int_answer == 1:
                friend()
            if int_answer == 2:
                no_friend()
            if int_answer == 3:
                who()
    except ValueError:
        hesitate()
    
def no_friend():
    win.setBackground("gray3")
    woodsman = Image(Point(400, 260), "woodsman.gif")
    woodsman.draw(win)
    str10 = "Well... A bad situation for you, my friend."
    str11 = "As my lord and master has ordered..."
    str12 = "All who do not serve Baylor must die!"
    intro_strings5 = [str10, str11, str12]
    for idx, val in enumerate(intro_strings5):
        intro5 = Text(Point(400, 475), intro_strings5[idx])
        intro5.setFace("courier")
        intro5.setTextColor("green4")
        intro5.setSize(18)
        intro5.setStyle("bold italic")
        intro5.draw(win)
        time.sleep(pauseTime)
        intro5.undraw()

def friend():
    win.setBackground("gray3")
    woodsman = Image(Point(400, 260), "woodsman.gif")
    woodsman.draw(win)
    str13 = "Followers of Baylor are a scourge upon this land."
    str14 = "All who serve Baylor must DIE!"
    intro_strings6 = [str13, str14]
    for idx, val in enumerate(intro_strings6):
        intro6 = Text(Point(400, 475), intro_strings6[idx])
        intro6.setFace("courier")
        intro6.setTextColor("green4")
        intro6.setSize(18)
        intro6.setStyle("bold italic")
        intro6.draw(win)
        time.sleep(pauseTime)
        intro6.undraw()

def who():
    win.setBackground("gray3")
    woodsman = Image(Point(400, 260), "woodsman.gif")
    woodsman.draw(win)
    str15 = "You have not heard of the great and powerful Baylor??"
    str16 = "A pity for you."
    str17 = "You will make an excellent sacrifice!"
    str18 = "Prepare to DIE!"

    intro_strings7 = [str15, str16, str17, str18]
    for idx, val in enumerate(intro_strings7):
        intro7 = Text(Point(400, 475), intro_strings7[idx])
        intro7.setFace("courier")
        intro7.setTextColor("green4")
        intro7.setSize(18)
        intro7.setStyle("bold italic")
        intro7.draw(win)
        time.sleep(pauseTime) 
        intro7.undraw()

def clear(win):
    for item in win.items[:]:
        item.undraw()
        #win = GraphWin(..., autoflush=False)
    win.update()

def forest_battle():
    global foe1
    clear(win)
    win.setBackground("gray2")
    forest1 = Image(Point(400, 250), "forest-map1.gif")
    forest1.draw(win)
    foe1 = Image(Point(400, 280), "woodsmanfoe.png")
    foe1.draw(win)
    player_move(win)



def player_move(win):
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

def checkPos(): #checks the position of the player and prohibits movement through foes
    play_center = player.getAnchor()
    foeC = foe1.getAnchor()
    foeH = foe1.getHeight()
    foeW = foe1.getWidth()
    playH = player.getHeight()
    playW = player.getWidth()
    print(play_center)
    print(foeC)
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

##def movement(win):
##    player = Image(Point(450, 500), "knight.png")
##    player.draw(win)
##    dx, dy = 10, 10
##
##    while True:
##        k = win.checkKey()
##        if k == 'Left':
##            player.move(-dx, 0)
##        elif k == 'Right':
##            player.move(dx, 0)
##        elif k == "Up":
##            player.move(0, -dy)
##        elif k == "Down":
##            player.move(0, dy)
##        elif k == 'period':
##            break
##    win.close()  
    
def main():
    title_screen()
    intro_screen()
    intro_screen2()
    forest_battle()
  
main()
