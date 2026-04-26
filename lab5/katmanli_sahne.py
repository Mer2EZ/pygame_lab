# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:35:41 2026

@author: Mert
"""

import os
import random
import pygame

pygame.init()
GENISLIK, YUKSEKLIK = 800,600
ekran=pygame.display.set_mode((GENISLIK,YUKSEKLIK))
saat=pygame.time.Clock()

DIZIN = os.path.dirname(os.path.abspath(__file__))

def gorsel_yukle(ad, boyut=None):
    yol=os.path.join(DIZIN, "assets", "images", ad)
    try:
        g=pygame.image.load(yol).convert_alpha()
        if boyut:
            g=pygame.transform.scale(g, boyut)
        return g
    except (FileNotFoundError, pygame.error):
        yt=pygame.Surface(boyut or (64,64), pygame.SRCALPHA)
        yt.fill((255,0,255,180))
        return yt
    
arkaplan=pygame.Surface((GENISLIK,YUKSEKLIK))
arkaplan.fill((5,5,25))
for _ in range(150):
    x=random.randint(0,GENISLIK)
    y=random.randint(0,YUKSEKLIK)
    arkaplan.set_at((x,y), (200,200,200))
    
gemi=gorsel_yukle("playerShip1_blue.png", (64,64))
dusman=gorsel_yukle("enemyRed1.png", (48,48))

dusmanlar = [[100+i*160, 100] for i in range(4)] # 4 düşman konumu

font = pygame.font.Font(None, 32)

çalıştır=True
while çalıştır:
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            çalıştır=False
    
    fare_x, fare_y = pygame.mouse.get_pos()
    
    for i in dusmanlar:
        if i[0] - 48 > GENISLIK :
            i[0] = - 48
        elif i[0] + 48 < 0:
            i[0] = GENISLIK + 48
        i[0]+=2.5
    
    
    
    # Z-ORDER: sıra önemli
    ekran.blit(arkaplan,(0,0)) # 1. arkaplan
    
    skor_bilgi = font.render("Skor: ??", True, (255,255,255))
    skor_rect = skor_bilgi.get_rect(center=(50,15))
    ekran.blit(skor_bilgi, skor_rect) # 1.1 skor
    
    fps_bilgi = font.render(f"Skor: {saat.get_fps():.2f}", True, (255,255,255))
    fps_rect = skor_bilgi.get_rect(center=(GENISLIK-80,15))
    ekran.blit(fps_bilgi, fps_rect) # 1.2 fps
    
    #ekran.blit(gemi, (fare_x-32, fare_y-32)) # 3. oyuncu
    for dx, dy in dusmanlar: # 2. düşmanlar
        ekran.blit(dusman, (dx,dy))
    ekran.blit(gemi, (fare_x-32, fare_y-32)) # 3. oyuncu
    
    pygame.display.flip()
    saat.tick(60)
    
pygame.quit()