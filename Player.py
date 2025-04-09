import pygame as pg
from Settings import settings

settings = settings()

class player():
    def __init__(self,n,win):
        self.n = n
        self.width = settings.playerWidth
        self.height = settings.playerHeight
        self.color = settings.playerColor
        self.speed = settings.playerSpeed
        self.score = 0
        self.p1Pos = [25,(settings.screenHeight/2)-(self.height/2)]
        self.p2Pos = [(settings.screenWidth-self.width)-25,(settings.screenHeight/2)-(self.height/2)]
        self.win = win if win is not None else pg.Surface((1,1))
        self.padding = 11
        self.speedIncrease = settings.ballSpeedIncrease/1.5

    def drawPlayer(self):
        if self.n == 1:
            self.p1=pg.draw.rect(self.win,self.color,[self.p1Pos[0],self.p1Pos[1],self.width,self.height])
        elif self.n == 2:
            self.p2=pg.draw.rect(self.win,self.color,[self.p2Pos[0],self.p2Pos[1],self.width,self.height])
        else:
            pass

    def movePlayer(self,speed):
        self.checkBounds()
        if self.n == 1:
            self.p1Pos[1] -= speed
        elif self.n == 2:
            self.p2Pos[1] -= speed

    def checkBounds(self):
        if self.n == 1:
            if self.p1Pos[1] <= (self.padding):
                self.p1Pos[1] = self.padding
            if self.p1Pos[1] >= (settings.screenHeight - self.height)-self.padding:
                self.p1Pos[1] = (settings.screenHeight - self.height)-self.padding
        elif self.n == 2:
            if self.p2Pos[1] <= self.padding:
                self.p2Pos[1] = self.padding
            if self.p2Pos[1] >= (settings.screenHeight - self.height)-self.padding:
                self.p2Pos[1] = (settings.screenHeight - self.height)-self.padding
        

    def reset(self):
        self.p1Pos = [25,(settings.screenHeight/2)-(self.height/2)]
        self.p2Pos = [(settings.screenWidth-self.width)-25,(settings.screenHeight/2)-(self.height/2)]


