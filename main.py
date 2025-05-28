import pygame
from constants import *
import player
import circleshape

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
player.Player.containers = (updatable, drawable)

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	time = pygame.time.Clock()
	dt = 0
	player_real = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		time_passed = time.tick(60)
		dt = time_passed / 1000
		screen.fill("black")
		updatable.update(dt)
		for thing in drawable:
			thing.draw(screen)
		pygame.display.flip()

if __name__ == "__main__":
    main()
