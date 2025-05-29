import pygame
import circleshape
import random
import constants

class Asteroid(circleshape.CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y , radius)

	def draw(self, screen):
		center = (int(self.position.x), int(self.position.y))
		pygame.draw.circle(screen, "white", center, self.radius, width = 2)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		if self.radius <= constants.ASTEROID_MIN_RADIUS:
			return
		velocity_1 = self.velocity.copy().rotate(random.uniform(20, 50))
		velocity_2 = self.velocity.copy().rotate(-random.uniform(20, 50))
		new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
		new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
		new_asteroid_1.velocity = velocity_1 * 1.2
		new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
		new_asteroid_2.velocity = velocity_2 * 1.2
