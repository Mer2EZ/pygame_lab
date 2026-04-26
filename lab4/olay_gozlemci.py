#-*-coding:utf-8-*-
"""
CreatedonWedApr2216:38:532026

@author:Mert
"""

import pygame
import sys

pygame.init()

GENISLIK=800
YUKSEKLIK=600

ekran=pygame.display.set_mode((GENISLIK,YUKSEKLIK))
pygame.display.set_caption("OlayGozlemci")
saat=pygame.time.Clock()

KOYU_GRI=(40,40,40)

çalıştır=True
while çalıştır:
    for olay in pygame.event.get():
        if olay.type==pygame.QUIT:
            çalıştır=False
        if olay.type == pygame.KEYDOWN :
            print (f"Basildi:{pygame.key.name(olay.key)}")
        elif olay.type == pygame.MOUSEBUTTONDOWN :
            print (f"Fare:dugme={olay.button},konum={olay.pos}")

    ekran.fill(KOYU_GRI)
    pygame.display.flip()
    saat.tick(60)

pygame.quit()
sys.exit()