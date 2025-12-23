import pygame as pg
import sys
from scripts.entities import PhysicsEntity


#Constants
width = 640
height = 480
fps = 60


#Screen Setup
class Game:
    def __init__(self):
        pg.init()

        pg.display.set_caption("Basic Platformer")
        self.image.set_colorkey((0,0,0))

        self.image_pos = [160, 260]
        self.movement = [False, False]

        self.screen = pg.display.set_mode((width, height))

        self.clock = pg.time.Clock()

        self.collision_area = pg.Rect(50, 50, 300, 50)

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

    def run(self):
        #Game Loop
        while True:
            self.screen.fill((14,219,248))

            image_r = pg.Rect(self.image_pos[0], self.image_pos[1], self.image.get_width(), self.image.get_height())
            if image_r.colliderect(self.collision_area):
                pg.draw.rect(self.screen, (0, 100, 255), self.collision_area)
            else:
                pg.draw.rect(self.screen, (0, 50, 155), self.collision_area)

            self.image_pos[1] += (self.movement[1] - self.movement[0]) * 5
            self.screen.blit(self.image, self.image_pos)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_w:
                        self.movement[0] = True
                    if event.key == pg.K_s:
                        self.movement[1] = True

                if event.type == pg.KEYUP:
                    if event.key == pg.K_w:
                        self.movement[0] = False
                    if event.key == pg.K_s:
                        self.movement[1] = False

            self.clock.tick(fps)
            pg.display.update()

Game().run()