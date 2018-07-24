from clock import Clock
import pygame
import datetime

# window size
s = [500,500]

# initialisations
pygame.init()
screen = pygame.display.set_mode(s,0,32)
pygame.display.set_caption("Clock by NIP")

numfont = pygame.font.SysFont("Garamond MS",20)

def main():
    clock = Clock(screen,numfont,[s[0]/2,s[1]/2+100],[s[0]/2,s[1]/2-100],200,[i/2 for i in s])

    while True:
        screen.fill((255,255,255))

        clock.events()
        clock.update(datetime.datetime.now())
        clock.draw()

        pygame.display.flip()

if __name__ == "__main__":
    main()
        
