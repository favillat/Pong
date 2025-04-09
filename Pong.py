import pygame as pg
from Settings import settings
from Player import player
from Ball import ball
import random
import sys

#Creating Instances Of Classes
settings = settings()

#Setting Up
pg.init()
wall_bounce_Sound = pg.mixer.Sound("C:/Users/villa/Downloads/Personal Coding Projects/Pong-20250217T192137Z-001/Pong/SFX/Bounce_wall.wav")
paddle_bounce_Sound = pg.mixer.Sound("C:/Users/villa/Downloads/Personal Coding Projects/Pong-20250217T192137Z-001/Pong/SFX/Bounce_paddle.wav")
death_Sound = pg.mixer.Sound("C:/Users/villa/Downloads/Personal Coding Projects/Pong-20250217T192137Z-001/Pong/SFX/death.wav")
button_Sound = pg.mixer.Sound("C:/Users/villa/Downloads/Personal Coding Projects/Pong-20250217T192137Z-001/Pong/SFX/button_press.wav")

win = pg.display.set_mode((settings.screenWidth,settings.screenHeight))
pg.display.set_caption("Scuffed Pong!")
clock = pg.time.Clock()

player1 = player(1,win)
player2 = player(2,win)
ball = ball()

smolFont = pg.font.Font("C:/Users/villa/Downloads/Personal Coding Projects/Pong-20250217T192137Z-001/Pong/Fonts/arcadeclassic/joystix.monospace.ttf",24)
font = pg.font.Font("C:/Users/villa/Downloads/Personal Coding Projects/Pong-20250217T192137Z-001/Pong/Fonts/arcadeclassic/joystix.monospace.ttf",38)
bigFont = pg.font.Font("C:/Users/villa/Downloads/Personal Coding Projects/Pong-20250217T192137Z-001/Pong/Fonts/arcadeclassic/joystix.monospace.ttf",60)
medFont = pg.font.Font("C:/Users/villa/Downloads/Personal Coding Projects/Pong-20250217T192137Z-001/Pong/Fonts/arcadeclassic/joystix.monospace.ttf",45)


def mainMenue():
    while True:
        win.fill((10,10,10))
        mousePos = pg.mouse.get_pos()
        startButtonBorder = pg.draw.rect(win,(245,245,245),[settings.screenWidth/2-300/2,settings.screenHeight/2-100,300,100],4,50)
        
        if startButtonBorder.collidepoint(mousePos):
            win.fill((10,10,10))
            startText = medFont.render("START",True,(255,255,255))
            startTextShadow = medFont.render("START",True,(100,100,100))

            startextrect = startText.get_rect()
            win.blit(startTextShadow,( (settings.screenWidth/2 - startextrect.width/2 ) , (settings.screenHeight/2-85)+3.5))
            win.blit(startText,( (settings.screenWidth/2 - startextrect.width/2 ) , (settings.screenHeight/2-85)))
            startButtonBorder = pg.draw.rect(win,(100,100,100),[((settings.screenWidth/2-300/2)-5)+2,((settings.screenHeight/2-100)-5)+4,310,110],4,100)
            startButtonBorder = pg.draw.rect(win,(255,255,255),[(settings.screenWidth/2-300/2)-5,(settings.screenHeight/2-100)-5,310,110],4,100)
        else:
            startButtonBorder = pg.draw.rect(win,(245,245,245),[settings.screenWidth/2-300/2,settings.screenHeight/2-100,300,100],4,50)
            startText = font.render("START",True,(245,245,245))
            startextrect = startText.get_rect()
            win.blit(startText,( (settings.screenWidth/2-300/2) + startextrect.width/2 , (settings.screenHeight/2-100) + startextrect.height/2))

        Title = bigFont.render("!Scuffed Pong!",True,(255,255,255))
        TitleRect = Title.get_rect()
        TitleShadow = bigFont.render("!Scuffed Pong!",True,(100,100,100))
        win.blit(TitleShadow,( settings.screenWidth/2-TitleRect.width/2 , 65))
        win.blit(Title,( settings.screenWidth/2-TitleRect.width/2 , 60 ))

        pg.display.update()
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if keys[pg.K_ESCAPE] or event.type == pg.QUIT:
                pg.quit() 
                running = False
                sys.exit() 
            if event.type == pg.MOUSEBUTTONDOWN and startButtonBorder.collidepoint(mousePos) :
                pg.mixer.Sound.play(button_Sound)
                mainLoop()
                
#Main Game Loop
def mainLoop():
    running = True
    started = False
    yVel = 0
    xVel = 0
    p1Score = player1.score
    p2Score = player2.score
    playerSpeed = 7
    p1Wins=False
    def blit(surface,pos):
            win.blit(surface,pos)
    def drawDottedLine(lines,sep,width,height):
        for i in range(lines):
            if height >= sep:
                i*= (sep*2)
            else:
                i*=sep
            whiteLine = pg.draw.rect(win,player1.color,[449,i,width,height])
    def reset():
        started=False
        player1.reset()
        player2.reset()
        ball.reset(win)
    def die(p1win):
        player1.reset()
        player2.reset()
        ball.reset(win)
        pg.mixer.Sound.play(death_Sound)
        deathScreen(p1win)

    while running:
        #Drawings
        win.fill((10,10,10))
        player1.drawPlayer()
        player2.drawPlayer()
        if started:             
            drawDottedLine(60,30,2,15)
        ball.drawBall(win)
        topLine = pg.draw.rect(win,player1.color,[0,0,settings.screenWidth,5])
        bottomLine = pg.draw.rect(win,player1.color,[0,settings.screenHeight-5,settings.screenWidth,5])
        p2Line = pg.Rect(850,player2.p2Pos[1],3,100)
        p1Line = pg.Rect(50,player1.p1Pos[1],3,100)
        p1WinsLine = pg.Rect(settings.screenWidth-1,0,1,settings.screenHeight)
        p2WinsLine = pg.Rect(0,0,1,settings.screenHeight)

        #Bounces Off Walls
        if ball.ballPos[1] <= (5):
            pg.mixer.Sound.play(wall_bounce_Sound)
            yVel = -yVel
        elif ball.ballPos[1] >= ((settings.screenHeight-5)-(ball.ballRadius*2)):
            pg.mixer.Sound.play(wall_bounce_Sound)
            yVel = -yVel
        elif(ball.ballPos[0]<=0):
            p2Score += 1
            reset()
        elif(ball.ballPos[0] >= settings.screenWidth-ball.ballRadius):
            p1Score += 1
            reset()

        elif (p1Score >= 5):
            die(True)
        elif (p2Score >=5):
            deathScreen(False)
            
        #Bounces Off Paddles
        if ball.ball.colliderect(p1Line):
            pg.mixer.Sound.play(paddle_bounce_Sound)
            xVel = -xVel
            xVel -= ball.increase
        if ball.ball.colliderect(p2Line): 
            pg.mixer.Sound.play(paddle_bounce_Sound)
            xVel= -xVel
            xVel += ball.increase

        ball.moveBall(xVel,yVel)
            
        #Handles Text
        p1ScoreText=font.render(f"{p1Score}",True,(255,255,255))
        p2ScoreText=font.render(f"{p2Score}",True,(255,255,255))
        spaceToStartText = font.render(f"Press SPACE To Start",True,(255,255,255))

        textSize1 = p1ScoreText.get_rect()
        textSize2 = p2ScoreText.get_rect()
        spaceToStartTextRect = spaceToStartText.get_rect()

        if not started:
            spaceToStartTextBlit = blit(spaceToStartText,((settings.screenWidth/2-spaceToStartTextRect.width/2),400))
        else:
            p1ScoreBlit = blit(p1ScoreText,(((settings.screenWidth/2)-textSize1.width)-50,100))
            p2ScoreBlit = blit(p2ScoreText,((settings.screenWidth/2)+50,100))

        #Limits Frame Rate And Updates Screen
        clock.tick(60)
        pg.display.update()
        
        #Checks Events
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit() 
                running = False
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit() 
                    running = False
                    sys.exit()
        if keys[pg.K_w] and not keys[pg.K_s]:
            player1.movePlayer(playerSpeed)
        if keys[pg.K_s] and not keys[pg.K_w]:
            player1.movePlayer(-playerSpeed)
        if keys[pg.K_DOWN] and not keys[pg.K_UP]:
            player2.movePlayer(-playerSpeed)
        if keys[pg.K_UP] and not keys[pg.K_DOWN]:
            player2.movePlayer(playerSpeed) 
        if keys[pg.K_SPACE] and xVel == 0 and yVel == 0 and not started:
            started = True
            vels = [-4,4]
            xVel = vels[random.randint(0,1)]
            yVel = 2

def deathScreen(p1Wins):
    dead = True
    while dead:
        win.fill((255,255,255))
        if p1Wins:
            f = bigFont.render(f"!!Player 1 Wins!!",True,(0,0,0))
            f_rect = f.get_rect()
        elif not p1Wins:
            f = bigFont.render(f"!!Player 2 Wins!!",True,(0,0,0))
            f_rect = f.get_rect()
        else:
            f = bigFont.render(f"IDK How That Happened!",True,(0,0,0))
            f_rect = f.get_rect()

        r = smolFont.render("--Press R To Try Again--",True,(0,0,0))
        r_rect = r.get_rect()

        m = smolFont.render("--Press M To Go To The Main Menue--",True,(0,0,0))
        m_rect = m.get_rect()

        win.blit(f,(settings.screenWidth/2-f_rect.width/2,settings.screenHeight/2-f_rect.height/2))
        win.blit(r,(settings.screenWidth/2-r_rect.width/2,(settings.screenHeight/2+r_rect.height*2)))
        win.blit(m,(settings.screenWidth/2-m_rect.width/2,(settings.screenHeight/2+m_rect.height*3.5)))

        pg.display.update()
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if keys[pg.K_ESCAPE] or event.type == pg.QUIT:
                pg.quit() 
                running = False
                sys.exit()
            if keys[pg.K_r]:
                mainLoop()
            if keys[pg.K_m]:
                mainMenue() 

mainMenue()

