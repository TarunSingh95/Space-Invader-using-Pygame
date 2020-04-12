import pygame

class Ship:

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen                  #Using the alienInvasion.py modules self.screen using an instance of it
        self.screen_rect = ai_game.screen.get_rect()  #converts the surface to a rectangle

        # Load the ship image and get its rect.
        self.image = pygame.image.load('img/spaceship.bmp')  #load the image
        self.rect = self.image.get_rect()             #make a rect of the image loaded

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom   #match the image and screen position.

        #flag to control alien movement
        self.move_right = False
        self.move_left = False
        # self.count_right = 0

        self.speed = ai_game.setting.ship_speed
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
            # self.count_right = self.x
            # print(self.count_right)   #This shows that on pressing Right arrow the x axis value is increasing
                                        #and I stop pressing it counter stops
        if self.move_left and self.rect.left > 0:
            self.x -= self.speed

        self.rect.x = self.x