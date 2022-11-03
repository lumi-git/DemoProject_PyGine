from PyGine import Scene
from PyGine.Debug import PrintDebug

from MyFirstOb import MyFirstOb
from PyGine import PyGinegame as Game
class maPremeiereScene(Scene) :

    def start(self):
        PrintDebug("my first scene is starting !")
        self.addGameObject(MyFirstOb())

    def update(self,dt):
        Game.get().surface.fill((0, 0, 0))