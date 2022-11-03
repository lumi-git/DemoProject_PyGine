import random

import pygame
from PyGine import Component
from PyGine.Debug import PrintDebug
from PyGine import *

class MySecondScript(Component) :

    def earlyStart(self):
        PrintDebug("my second script is starting !")
        self.parent.transform.position = Vector3(random.randint(100,200),random.randint(100,200),0)
