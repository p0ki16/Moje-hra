import pygame
import sys
from letadlo import Letadlo


clock = pygame.time.Clock()
stihacka = pygame.image.load("stíhačka_do_hry.png")
Pohyblive_pozadi = pygame.image.load("Pozadí_pohyblivé.png")
pohyb_pozadí = 0
rozdil_pozadi = 1920
výška, šířka = 1080, 1920
obrazovka = pygame.display.set_mode((šířka, výška))
pygame.display.set_caption("zkouška")
pozadi_barva = (0, 255, 255)

# Initialize the letadlo object
letadlo = Letadlo(šířka, výška)

while True:
    pohyb_pozadí -= 50
    umisteni_pozadi1 = pohyb_pozadí % rozdil_pozadi
    umisteni_pozadi2 = (pohyb_pozadí % rozdil_pozadi) - rozdil_pozadi
    
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        letadlo.y += 10  # Move downward
    if keys[pygame.K_w]:
        letadlo.y -= 10  # Move upward
    if keys[pygame.K_a]:
        letadlo.x -= 10  # Move left
    if keys[pygame.K_d]:
        letadlo.x += 10  # Move right

    obrazovka.fill(pozadi_barva)
    obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi1, výška - 100))
    obrazovka.blit(Pohyblive_pozadi, (umisteni_pozadi2, výška - 100))
    obrazovka.blit(stihacka, (letadlo.x, letadlo.y))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
