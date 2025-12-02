import pygame, sys
import player, asteroid, asteroidfield, shot
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SHOT_RADIUS
from logger import log_state, log_event

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable, )
    shot.Shot.containers = (shots, updatable, drawable)

    new_player = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    new_asteroidfield = asteroidfield.AsteroidField()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        fps = clock.tick(60)
        dt = fps/1000

        for obj in drawable:
            obj.draw(screen)

        updatable.update(dt)
        new_player.cooldown -= dt
        for obj in asteroids:
            if new_player.collides_with(obj):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for bullet in shots:
            for obj in asteroids:
                if bullet.collides_with(obj):
                    log_event("asteroid_shot")
                    obj.split()
                    bullet.kill()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            new_player.shoot() 
        pygame.display.flip()

if __name__ == "__main__":
    main()
