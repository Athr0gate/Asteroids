import sys
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    if not pygame.get_init:
        pygame.init
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, asteroids, drawable)
    AsteroidField.containers = updateable
    Shot.containers = (updateable, drawable, shots)

    asteroid_field = AsteroidField()
    player = Player(x, y)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        

        for thing in updateable:
            thing.update(dt)

        for thing in asteroids:
            if thing.collision_check(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if thing.collision_check(shot):
                    shot.kill()
                    thing.kill()
    
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        frames = clock.tick(60)
        dt = frames / 1000
        
       
if __name__== "__main__":
    main()