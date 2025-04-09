import pygame as pg

class settings():
    def __init__(self):
        self.screenWidth = 900
        self.screenHeight = 600

        self.playerHeight = 100
        self.playerWidth = 25
        self.playerColor = (250,250,255)
        self.playerSpeed = 10

        self.ballRadius = 7
        self.ballSpeed = 2
        self.ballSpeedIncrease=0.5