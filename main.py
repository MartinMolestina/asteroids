import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    
    clock = pygame.time.Clock()
    dt = 0
       
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Correct container assignment
    Player.containers = updatable, drawable

    print("Starting Asteroids!") 
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        
        # Instance methods
        player.rotate(dt)

        # Update and draw all sprites
        updatable.update(dt)
        drawable.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__": 
    main()

