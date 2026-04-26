# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:28:14 2026

@author: Mert
"""

import os
import pygame

pygame.init ()

GENISLIK = 800
YUKSEKLIK = 600

ekran = pygame.display.set_mode( (GENISLIK, YUKSEKLIK) )
pygame.display.set_caption("Gorsel Yukleme Testi")
saat = pygame.time.Clock()

# Dosya dizini
DIZIN = os.path.dirname(os.path.abspath(__file__))
GORSEL = os.path.join(DIZIN, "assets", "images")

def gorsel_yukle(path):
    try:
        return pygame.image.load(path).convert_alpha()
        print(" [OK] Gorsel yuklendi")
    except FileNotFoundError:
        print(" [UYARI] Dosya bulunamadi, placeholder oluşturuluyor")
        placeholder = pygame.Surface((64, 64),pygame.SRCALPHA)
        placeholder.fill((255, 0, 255, 180))
        for i in range(1,4):
            pygame.draw.line(placeholder, (0,0,0), (0,(i*16)), ((i*16),0))
            pygame.draw.line(placeholder, (0,0,0), ((i*16),64), (64,(i*16)))
        pygame.draw.line(placeholder, (0,0,0), (0,64), (64,0))
        return placeholder

# Gorsel yukle
dosya_yolu = os.path.join(GORSEL, "playerShip1_blue.png")
gemi = gorsel_yukle(dosya_yolu)
    
ufo_yolu= os.path.join(GORSEL, "ufoRed.png")
ufo = gorsel_yukle(ufo_yolu)

dusman_yolu= os.path.join(GORSEL, "playerShip3_red.png")
dusman = gorsel_yukle(dusman_yolu)

arkaplan_yolu = os.path.join(GORSEL, "purple.png")
arkaplan = gorsel_yukle(arkaplan_yolu)
arkaplan = pygame.transform.scale(arkaplan, (GENISLIK, YUKSEKLIK))

deneme_y= "deneme.dnm"
deneme = gorsel_yukle(deneme_y)

çalıştır = True
while çalıştır:
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            çalıştır = False
    
    ekran.blit(arkaplan, (0,0))
    ekran.blit(gemi, (GENISLIK // 2 - 32, YUKSEKLIK // 2 - 32))
    ekran.blit(dusman, (75,75))
    ekran.blit(ufo, (50,50))
    ekran.blit(deneme, (GENISLIK-150,YUKSEKLIK-150))
    pygame.display.flip()
    saat.tick(60)

pygame.quit()