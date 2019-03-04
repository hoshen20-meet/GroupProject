import turtle
import random
import tkinter as tk
def Game():
    faces=["sadnizar-final.gif","happynizar-final.gif"]
    turtle.setup(1000,1000)
    player = turtle.Turtle()
    scoreCounter = turtle.Turtle()
    screen = turtle.Screen()
    screen.setup(1000,1000)
    screen.bgpic("DUCKBACKGROUND.gif")
    nizar_width=200
    nizar_height=67
    turtle.listen()
    global counter
    counter = 0
    #creating borderscounter
    title = turtle.Turtle()
    title.penup()
    title.goto(0,400)
    title.write("Catch the nizars!!", font=("Comic Sans MS",40),align="center")
    title.hideturtle()
    border = turtle.Turtle()
    border.speed(0)
    border.penup()
    border.goto(-400,-400)
    border.pendown()
    border.goto(-400,400)
    border.goto(400,400)

    border.goto(400,-400)

    border.goto(-400,-400)
    border.hideturtle()

    scoreCounter.penup()
    scoreCounter.hideturtle()
    scoreCounter.goto(370,400)

        #creating the recycle bin
    turtle.register_shape("nada-transparent.gif")
    turtle.register_shape('boaz-transparent.gif')
    player.penup()
    turtle.register_shape("mahmoud-final.gif")
    player.shape("mahmoud-final.gif")
    player.goto(0,-300)

            
    ######################3def StartGame():
    #for happy nizars
    def scoreup():
        global counter
        scoreCounter.clear()
        scoreCounter.penup()
        scoreCounter.hideturtle()
        scoreCounter.goto(370,400)
        counter=counter + 2
        scoreCounter.write("Score = " + str(counter), font=("Comic Sans MS",30),align="center")

    #for sad nizars //we need minus 1 counter
    def scoredown():
        global counter
        scoreCounter.clear()
        scoreCounter.penup()
        scoreCounter.hideturtle()
        scoreCounter.goto(370,400)
        counter=counter - 1
        scoreCounter.write("Score = " + str(counter), font=("Comic Sans MS",30),align="center")
        
        
        

    #making the player move

    def right():
        if player.xcor() > 280:
            player.setpos(280,-300)
        else:
            player.forward(80)

    def left():
        if player.xcor() < -280:
            player.setpos(-280,-300)
        else:
            player.back(80)
    turtle.onkeypress(right, "Right")

    turtle.onkeypress(left, "Left")    

    def falling_trash():
            global counter
            nizars = []
            trash = turtle.Turtle()
            
            trash.hideturtle()
            trash.setheading(270)
            trash.penup()

            
            #spawns trash/nizar's bootiful face
            nizars.append(trash.setpos(random_xpos,400))
            turtle.register_shape("happynizar-final.gif")
            turtle.register_shape("sadnizar-final.gif")
            trash.shape(random.choice(faces))
            trash.showturtle()
            
            while trash.pos()[1] > -299:
                leftside_nizar=trash.xcor()-100
                rightside_nizar=trash.xcor()+100
                topside_nizar=trash.ycor()+33.5
                player_width= 500
                trash.forward(5)
                #collision
            if topside_nizar <= -120 and rightside_nizar>=player.xcor()-250 and rightside_nizar<=player.xcor()+250 and leftside_nizar>= player.xcor()-250 and leftside_nizar<= player.xcor()+250:
                if trash.shape() == 'happynizar-final.gif':
                    scoreup()
                    print('ok')
                elif trash.shape() == 'sadnizar-final.gif':
                    scoredown()
                    print('not ok')

               # score+=1
                trash.hideturtle()

            if counter == 10:
                scoreCounter.goto(0,0)
                scoreCounter.color('blue')
                scoreCounter.write("YOU WON!!!", font=("Comic Sans MS",100),align="center")
                quit()
            if counter <= -2:
                scoreCounter.goto(0,0)
                scoreCounter.color('red')
                scoreCounter.write("YOU LOSE!!!", font=("Comic Sans MS",100),align="center")
                answer2 = input('would you like to restart?')
                if answer2 == 'yes':
                    turtle.clearscreen()
                    counter += 2
                    Game()
                    print('yes')
                    
            if trash.shape() == 'happynizar-final.gif' and trash.ycor() <= -100:
                scoredown()
                    
                    
                    
               

                
    #falling trash function
    while True:
        xpos = [-240, -160, 80, 0, 80, 160, 240]
        random_xpos = random.choice(xpos)
        random_xpos2 = random.choice(xpos)

        falling_trash()
        # make everything a function to make a replay button!!!
global running
running = False
answer = input('who would you like to play?')
while(running == False):
    if answer == 'nada':
        player.shape('nada-transparent.gif')
        answer = input('who would you like to play?')
    if answer == 'mahmoud':
        player.shape('mahmoud-final.gif')
        running == True
        break
    if answer == 'quit':
        quit()
    if answer == 'boaz':
        player.shape('boaz-transparent.gif')
        running == True
        break
    if answer != 'mahmoud' or 'nada' or 'boaz' or 'play':
        print('wrong value, please select nada / mahmoud / boaz/play')
    if answer == "play":
        Game()
        running == True
Game() 
turtle.mainloop()
