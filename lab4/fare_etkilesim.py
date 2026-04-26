# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:06:05 2026

@author: Mert
"""

import pygame
import sys

pygame.init()

GENISLIK = 800
YUKSEKLIK = 600

ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK) )
pygame.display.set_caption("Fare ile Etkilesim")
saat = pygame.time.Clock()

KOYU_MAVI = (15, 25, 60)
MAVI= (50, 120, 255)
KIRMIZI= (220, 60, 60)

daireler = [] # (x, y) pozisyonlarini tut

çalıştır = True
while çalıştır:
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            çalıştır = False
        if olay.type == pygame.KEYDOWN:
            if olay.key == pygame.K_c:
                daireler.clear()
        elif olay.type == pygame.MOUSEBUTTONDOWN:
            if olay.button == 1: # Sol tikla
                daireler.append((olay.pos[0],olay.pos[1],MAVI))
            if olay.button == 3: # Sağ tikla
                daireler.append((olay.pos[0],olay.pos[1],KIRMIZI))
    
    ekran.fill(KOYU_MAVI)
    
    fare_x,fare_y = pygame.mouse.get_pos()
    pygame.draw.circle(ekran , (255 , 255 , 100) , ( fare_x , fare_y ) , 12)
    
    for konum in daireler:
        pygame.draw.circle(ekran, konum[2], (konum[0],konum[1]), 20)

    pygame.display.flip()
    saat.tick(60)

pygame.quit()
sys.exit()