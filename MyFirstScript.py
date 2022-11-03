import pygame
from PyGine import Component
from PyGine.Debug import PrintDebug
from PyGine import *

class MyFirstScript(Component) :
    def start(self):
        PrintDebug("my first script is starting !")

    def update(self,dt):

        self.parent.transform.position.x +=1*dt*PyGine.KeyListener.getPressed(pygame.K_d)
        self.parent.transform.position.x -= 1 * dt * PyGine.KeyListener.getPressed(pygame.K_q)
        self.parent.transform.position.y += 1 * dt * PyGine.KeyListener.getPressed(pygame.K_s)
        self.parent.transform.position.y -= 1 * dt * PyGine.KeyListener.getPressed(pygame.K_z)

