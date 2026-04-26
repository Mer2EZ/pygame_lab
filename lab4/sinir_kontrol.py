# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:30:00 2026

@author: Mert
"""

import pygame
import sys

pygame.init()

GENISLIK=800
YUKSEKLIK=600

ekran=pygame.display.set_mode((GENISLIK,YUKSEKLIK))
pygame.display.set_caption("Sinir Kontrolu - Clamp")
saat=pygame.time.Clock()
FPS=60

LACIVERT = (15 , 25 , 60)
TURUNCU = (255 , 160 , 20)
MAVI=(0,0,255)
YESIL=(0,255,0)

# Top özellikleri
top_x = 100.0
top_y = 100.0
Mtop_x= 50.0
Mtop_y=75.0
Ytop_x=125.0
Ytop_y=175.0
top_r = 25      # yaricap
hiz_x = 250.0   # piksel / saniye
hiz_y = 180.0
Mhiz_x = 120.0
Mhiz_y = 120.0
Yhiz_x = 220.0
Yhiz_y = 140.0

çalıştır = True
while çalıştır:
    dt = saat.tick(FPS) / 1000.0
    
    for olay in pygame.event.get() :
        if olay.type == pygame.QUIT:
            çalıştır = False
    
    # Hareketi güncelle
    top_x += hiz_x *dt
    top_y += hiz_y *dt
    Mtop_x+= Mhiz_x *dt
    Mtop_y+= Mhiz_y *dt
    Ytop_x+= Yhiz_x *dt
    Ytop_y+= Yhiz_y *dt
    
    # Clamp: sinir icerisinde tut
    top_x = max(top_r, min(top_x, GENISLIK - top_r))
    top_y = max(top_r, min(top_y, YUKSEKLIK - top_r))
    
    # Bounce
    if Mtop_x - top_r < 0 or Mtop_x + top_r > GENISLIK :
        Mhiz_x = - Mhiz_x
    if Mtop_y - top_r < 0 or Mtop_y + top_r > YUKSEKLIK :
        Mhiz_y = - Mhiz_y
        
    # Wrap
    if Ytop_x - top_r > GENISLIK :
        Ytop_x = - top_r
    elif Ytop_x + top_r < 0:
        Ytop_x = GENISLIK + top_r
    if Ytop_y - top_r > YUKSEKLIK :
        Ytop_y = - top_r
    elif Ytop_y + top_r < 0:
        Ytop_y = YUKSEKLIK + top_r
    
    ekran.fill(LACIVERT)
    pygame.draw.circle(ekran,TURUNCU,(int(top_x),int(top_y)),top_r)
    pygame.draw.circle(ekran,MAVI,(int(Mtop_x),int(Mtop_y)),top_r)
    pygame.draw.circle(ekran,YESIL,(int(Ytop_x),int(Ytop_y)),top_r)
    pygame.display.flip()

pygame.quit ()
sys.exit ()