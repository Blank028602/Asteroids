import pygame
from constants import *
import player
import circleshape
import asteroid
import asteroidfield
import sys
import shot

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
player.Player.containers = (updatable, drawable)
asteroid.Asteroid.containers = (asteroids, updatable, drawable)
asteroidfield.AsteroidField.containers = (updatable)
shot.Shot.containers = (shots, updatable, drawable)

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	time = pygame.time.Clock()
	dt = 0
	player_real = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = asteroidfield.AsteroidField()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		time_passed = time.tick(60)
		dt = time_passed / 1000
		screen.fill("black")
		updatable.update(dt)
		for thing in asteroids:
			if thing.collision(player_real) == True:
				print("Game over!")
				sys.exit()
			for asteroid in asteroids:
				for shot in shots:
					if asteroid.collision(shot):
						shot.kill()
						asteroid.kill()
						asteroid.split()
		for thing in drawable:
			thing.draw(screen)
		pygame.display.flip()

if __name__ == "__main__":
    main()
