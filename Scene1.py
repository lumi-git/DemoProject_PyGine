from PyGine import Scene
from PyGine.Debug import PrintDebug

from monPremierObjet import monPremierObjet
from PyGine import PyGinegame as Game
class maPremeiereScene(Scene) :

    def start(self):
        PrintDebug("je start ma scene")
        self.addGameObject(monPremierObjet())

    def update(self,dt):
        Game.get().surface.fill((0, 0, 0))