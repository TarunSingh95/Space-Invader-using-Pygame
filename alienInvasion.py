import sys
import pygame
from settings import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:

    def __init__(self):
        # Initialize Pygame
        pygame.init()

        #Setting module instance
        self.setting = Setting()

        # setting display size to 1200x800 using a tuple value
        self.screen = pygame.display.set_mode((self.setting.inner_width, self.setting.inner_height))
        pygame.display.set_caption("Alien Invasion")       #setting the caption

        #Ship instance
        self.ship = Ship(self)

        #Bullet List
        self.bullets = pygame.sprite.Group()

        #Alien List
        self.aliens = pygame.sprite.Group()
        self.create_fleet()

    def run_game(self):

        while True:
            #watch for a keyboard event
            self._check_events()

            #handler event for updating ship
            self.ship.update()

            #handler method for Updating bullets
            self._update_bullets()

            #Deleting bullets when it is 10 px from top
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 10:
                    self.bullets.remove(bullet)

            # Redraw the screen during each pass through the loop.
            self._update_screen()

    def _check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keypress_down(event)
            elif event.type == pygame.KEYUP:
                self._keypress_up(event)

    def _update_screen(self):

        self.screen.fill(self.setting.bg_color)

        #drawing ship on the surface
        self.ship.blitme()

        #drawing the bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #drawing the aliens
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _keypress_down(self, event):

        if event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        # a new instance of bullet
        new_bullet = Bullet(self)

        if len(self.bullets) < self.setting.bullet_number:
            # adding instance of bullet to the list
            self.bullets.add(new_bullet)


    def _keypress_up(self, event):

        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False

    def _update_bullets(self):

        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)

    def create_fleet(self):
        #instance of the Alien class
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        horizontal_space_available = self.setting.inner_width - (2*alien_width)
        alien_number = horizontal_space_available//alien_width

        vertical_space_available = self.setting.inner_height - (3*alien_width + self.ship.rect.height)
        row_number = vertical_space_available//(2*alien_height)

        for row in range(row_number+1):
            for column in range(alien_number):
                self._create_alien_row(column, row)

    def _create_alien_row(self, column, row):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        if row % 2 == 1:
            alien.x = alien_width + alien_width * column
        else:
            alien.x = 2*alien_width + alien_width * column
        alien.rect.x = alien.x

        alien.rect.y = alien_height + alien_height * row
        self.aliens.add(alien)

    def _update_aliens(self):

        collision = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if len(collision)%3==0:
            alien = Alien(self)
            alien.rect.y = alien.rect.height + alien.rect.height * 3

if __name__ == '__main__':

 # Make a game instance, and run the game.
 ai = AlienInvasion()
 ai.run_game()