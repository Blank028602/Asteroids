import pygame
import circleshape

class Shot(circleshape.CircleShape):
	def __init__(self, position, radius, velocity):
		super().__init__(position.x, position.y, radius)
		self.velocity = velocity

	def draw(self, screen):
		center = (int(self.position.x), int(self.position.y))
		pygame.draw.circle(screen, "white", center, self.radius, width = 2)

	def update(self, dt):
		self.position += self.velocity * dt

