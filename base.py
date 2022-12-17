import pygame
import os

class Base():
    # creates two imgs of base and they move like a treadmill, to give a sensation of moving base.
    # once one imgs get off screen, its position goes back to the start of the screen
    SPEED = 5

    def __init__(self, y, img):
        self.img = img
        self.width = img.get_width()

        self.y = y

        self.x1=0
        self.x2 = self.width

    def move(self, vel):
        self.x1 -= vel
        self.x2 -= vel

        if self.x1 + self.width < 0:
            self.x1 = self.width
        if self.x2 + self.width < 0:
            self.x2  = self.width

    def draw(self, win):
        win.blit(self.img, (self.x1, self.y))
        win.blit(self.img, (self.x2, self.y))