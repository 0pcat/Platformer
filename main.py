import pygame as pg
import sys
from scripts.entities import PhysicsEntity
from scripts.utils import load_image, load_images
from scripts.tilemap import Tilemap

#Constants
width = 640
height = 480
fps = 60


#Screen Setup
class Game:
    def __init__(self):
        pg.init()

        pg.display.set_caption("Basic Platformer")
        self.screen = pg.display.set_mode((width, height))
        self.clock = pg.time.Clock()
        self.display = pg.Surface((320, 240))

        self.movement = [False, False]
        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player.png')
        }

        self.tilemap = Tilemap(self, tiles_size=16)
    def run(self):
        #Game Loop
        while True:
            self.display.fill((14,219,248))

            self.tilemap.render(self.display)

            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_a:
                        self.movement[0] = True
                    if event.key == pg.K_d:
                        self.movement[1] = True
                    if event.key == pg.K_SPACE:
                        self.player.velocity[1] = -3

                if event.type == pg.KEYUP:
                    if event.key == pg.K_a:
                        self.movement[0] = False
                    if event.key == pg.K_d:
                        self.movement[1] = False

            self.screen.blit(pg.transform.scale(self.display, self.screen.get_size()), (0,0))
            self.clock.tick(fps)
            pg.display.update()

Game().run()