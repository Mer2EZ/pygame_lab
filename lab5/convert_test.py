# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:08:10 2026

@author: Mert
"""

import os
import time
import pygame

pygame.init()

GENISLIK = 800
YUKSEKLIK = 600

ekran = pygame.display.set_mode((GENISLIK, YUKSEKLIK))
saat = pygame.time.Clock()

DIZIN = os.path.dirname(os.path.abspath(__file__))
dosya = os.path.join(DIZIN, "assets" , "images" , "playerShip1_blue.png")

# 3 farkli yukleme yontemi
try:
    ham = pygame.image.load(dosya)
    donusmus = pygame.image.load(dosya).convert()
    alpha = pygame.image.load(dosya).convert_alpha() # şeffaflığı korur
except FileNotFoundError:
    print("Gorsel bulunamadi, cikiliyor.")
    pygame.quit()
    exit()

# Performans testi
def blit_testi(gorsel, tekrar=10000):
    baslangic = time.time()
    for _ in range(tekrar):
        ekran.blit(gorsel, (0, 0))
    return (time.time()-baslangic) * 1000

print (f"Ham        : {blit_testi (ham)         : .2f} ms")
print (f"convert    : {blit_testi (donusmus)    : .2f} ms")
print (f"convert_a  : {blit_testi (alpha)       : .2f} ms")

#donusmus.set_colorkey((0,0,0))

çalıştır = True
while çalıştır:
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            çalıştır = False
    
    ekran.fill((100,100,100))
    
    ekran.blit(donusmus,(275,300))
    ekran.blit(alpha,(525,300))
    
    pygame.display.flip()
    saat.tick(60)

pygame.quit()