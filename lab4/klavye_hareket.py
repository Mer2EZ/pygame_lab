# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:51:36 2026

@author: Mert
"""

import pygame
import sys

pygame.init()

GENISLIK=800
YUKSEKLIK=600

ekran=pygame.display.set_mode((GENISLIK,YUKSEKLIK))
pygame.display.set_caption("Klavye ile Harket")
saat=pygame.time.Clock()
FPS=60

LACIVERT=(20,30,70)
SARI=(255,220,50)

# Kare Özellikleri
kare_x=GENISLIK//2
kare_y=YUKSEKLIK//2
kare_boy=40
HIZ=500 # Piksel/Saniye

renkler = [(255 ,220 ,50) , (50 ,200 ,100) , (50 ,150 ,255) , (255 ,100 ,100)]
renk_indis = 0

çalıştır=True
while çalıştır:
    dt=saat.tick(FPS)/1000.0 # saniye cinsinden delta time
    for olay in pygame.event.get():
        if olay.type==pygame.QUIT:
            çalıştır=False
        elif olay.type == pygame.KEYDOWN:
            if olay.key == pygame.K_ESCAPE:
                çalıştır=False
            if olay.key == pygame.K_SPACE:
                renk_indis = (renk_indis+1) % len(renkler)
                
    # Surekli girdi kontrolü
    tuslar = pygame.key.get_pressed()
    if tuslar[pygame.K_UP]:
        kare_y -= HIZ*dt
    if tuslar[pygame.K_w]:
        kare_y -= HIZ*dt
    if tuslar[pygame.K_DOWN]:
        kare_y += HIZ*dt
    if tuslar[pygame.K_s]:
        kare_y += HIZ*dt
    if tuslar[pygame.K_LEFT]:
        kare_x -= HIZ*dt
    if tuslar[pygame.K_a]:
        kare_x -= HIZ*dt
    if tuslar[pygame.K_RIGHT]:
        kare_x += HIZ*dt
    if tuslar[pygame.K_d]:
        kare_x += HIZ*dt
        
    ekran.fill(LACIVERT)
    pygame.draw.rect(ekran, renkler[renk_indis], (int(kare_x), int(kare_y), kare_boy, kare_boy))
    pygame.display.flip()
    
pygame.quit()
sys.exit()