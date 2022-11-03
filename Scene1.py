from PyGine import Scene
from PyGine.Debug import PrintDebug

from MySecondObj import MySecondObj
from MyFirstOb import MyFirstOb
from PyGine import PyGinegame as Game
class maPremeiereScene(Scene) :

    def start(self):
        PrintDebug("my first scene is starting !")
        for i in range(10000) :
            Game.get().instanciate(MySecondObj())
        Game.get().instanciate(MyFirstOb())
    def update(self,dt):
        Game.get().surface.fill((80, 150, 100))