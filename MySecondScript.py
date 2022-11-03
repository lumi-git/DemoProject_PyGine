import random

import pygame
from PyGine import Component
from PyGine.Debug import PrintDebug
from PyGine import *

class MySecondScript(Component) :
    def __init__(self,parent):
        super().__init__(parent)

    def start(self):
        self.parent.transform.position = Vector3(random.randint(0,1000),random.randint(0,600),0)
