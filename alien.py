from pygame.sprite import Sprite
import pygame

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen

        self.image = pygame.image.load("img/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    # def update(self):
    #     if self.rect.x < self.screen.right:
    #         self.x += 1
    #         self.rect.x = self.x

