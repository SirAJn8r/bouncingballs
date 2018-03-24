import pygame
import random #remember to random size and speed

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("download.jpeg")
        #self.image = pygame.image.load("photo.jpg")
        temp = random.randint(20, 100)
        self.image = pygame.transform.smoothscale(self.image, (temp, temp)) #size
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = pygame.math.Vector2(0, random.randint(4, 10)) #speed
        self.speed.rotate_ip(random.randint(0, 359)) #direction

    def update(self):
        self.rect.move_ip(self.speed)
        (width, height) = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        if self.rect.top <= 0 or self.rect.bottom >= height:
            self.speed[1] *= -1
        if self.rect.left <= 0 or self.rect.right >= width:
            self.speed[0] *= -1