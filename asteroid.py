import circleshape, pygame, random
from logger import log_event
from constants import *


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        velocity = self.velocity
        self.position += (velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        first_new_asteroid = self.velocity.rotate(angle)
        second_new_asteroid = self.velocity.rotate(-angle)

        old_radius = self.radius
        new_radius = old_radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = first_new_asteroid * 1.2
        asteroid2.velocity = second_new_asteroid * 1.2

