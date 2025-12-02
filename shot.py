import circleshape, pygame, constants

class Shot(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.SHOT_RADIUS)
    
    def update(self, dt):
        velocity = self.velocity
        self.position += (velocity * dt)