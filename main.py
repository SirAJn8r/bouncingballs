import pygame as pg
from pygame.locals import *
import sys
from ball import *

pg.init()

size = (width, height) = (pg.display.Info().current_w, pg.display.Info().current_h)
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
color = (100, 100, 0)
balls = pg.sprite.Group()
for i in range(100):
    balls.add(Ball((width/2, height/2)))

def main():
    global screen
    while True:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_n:
                    screen = pg.display.set_mode(size, FULLSCREEN)
                if event.key == K_ESCAPE:
                    screen = pg.display.set_mode(size)
        balls.update()
        screen.fill(color)
        balls.draw(screen)
        pg.display.flip()

if __name__ == "__main__":
    main()