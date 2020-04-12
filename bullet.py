import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):

        super().__init__()

        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.color =self.setting.bullet_color

        self.rect = pygame.Rect(0,0, self.setting.bullet_width, self.setting.bullet_height)

        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):

        self.y -= self.setting.bullet_speed #we know the bullet's y position and to move it upwards we want to
                                            # 1 from it. The update method will run continuosly thus making go upwards
        self.rect.y = self.y                # updating the position

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)