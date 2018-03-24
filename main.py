import pygame as pg
from pygame.locals import *
import sys

pg.init()

size = (width, height) = (pg.display.Info().current_w, pg.display.Info().current_h)
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
image = pg.image.load("download.jpeg")
rect = image.get_rect()
speed = [5, 5]
color = (100, 100, 0)

def update():
    rect.move_ip(speed)
    if rect.top <= 0:
        speed[1] -= speed[1] * 2
    if rect.left <= 0:
        speed[0] -= speed[0] * 2
    if rect.right >= width:
        speed[0] -= speed[0] * 2
    if rect.bottom >= height:
        speed[1] -= speed[1] * 2


def main():
    while True:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == QUIT:
                sys.exit()
        update()
        screen.fill(color)
        screen.blit(image, rect)
        pg.display.flip()

if __name__ == "__main__":
    main()