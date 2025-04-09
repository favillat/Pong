import pygame as pg
from Settings import settings
from Player import player

settings = settings()
player = player(1,None)

class ball():
    def __init__(self):
        self.ballRadius = settings.ballRadius
        self.speed = settings.ballSpeed
        self.increase = settings.ballSpeedIncrease
        self.ballPos = [(settings.screenWidth/2)-((self.ballRadius*2)/2),(settings.screenHeight/2)-((self.ballRadius*2)/2)]
        
    def drawBall(self,win):
        self.ball = pg.draw.ellipse(win,player.color,[self.ballPos[0],self.ballPos[1],self.ballRadius*2,self.ballRadius*2])
    
    def moveBall(self,xVel,yVel):
        self.ballPos[0] -= xVel
        self.ballPos[1] -= yVel
    
    def reset(self,win):
        self.ballPos = [(settings.screenWidth/2)-((self.ballRadius*2)/2),(settings.screenHeight/2)-((self.ballRadius*2)/2)]

        
            
