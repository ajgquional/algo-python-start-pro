from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager

# file path fix
from pathlib import Path
land_txt = Path(__file__).with_name('land.txt')
land2_txt = Path(__file__).with_name('land2.txt')
land3_txt = Path(__file__).with_name('land3.txt')
# if the terminal directly points to the folder where the script is located, simply use the name of the text file as a string:
# land_txt = 'land.txt'
# land2_txt = 'land2.txt'
# land3_txt = 'land3.txt'

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        # lines below can be alternately commented/uncommented to see how each "land" looks like
        self.land.loadLand(land_txt)
        # self.land.loadLand(land2_txt)
        # self.land.loadLand(land3_txt)
        base.camLens.setFov(90)

game = Game()
game.run()
