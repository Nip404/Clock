from engine import Clock
import pygame
import datetime

# window size
s = [500, 500]

# initialisations
pygame.init()
screen = pygame.display.set_mode(s, 0, 32)
pygame.display.set_caption("Clock by NIP")

def main():
    # Defaults:
        # Param 1 (REQUIRED): surface = pygame.Surface([500,500])
        # Param 2: fontsize = 20
        # Param 3: radius = 200
        # Param 4: centre = [250,250]
    clock = Clock(screen)

    while True:
        screen.fill((255, 255, 255))

        clock.events()
        clock.update(datetime.datetime.now())
        clock.draw()

        pygame.display.flip()

if __name__ == "__main__":
    main()
        
