import circleshape
import constants
import pygame
import shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        radius = constants.PLAYER_RADIUS
        super().__init__(x, y, radius)
        self.rotation = 0
        self.cooldown = 0
    
    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
    
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * constants.PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    
    def shoot(self):
        if self.cooldown > 0:
            return
        else:
            self.cooldown = constants.PLAYER_SHOOT_COOLDOWN_SECONDS
        new_shot = shot.Shot(self.position.x, self.position.y, constants.SHOT_RADIUS)
        velocity = pygame.Vector2(0, 1)
        velocity.rotate_ip(self.rotation)
        velocity *= constants.PLAYER_SHOOT_SPEED
        new_shot.velocity = velocity