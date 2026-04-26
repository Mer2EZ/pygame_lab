# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 02:13:34 2026

@author: Mert
"""

import pygame
import math

pygame.init()
ekran=pygame.display.set_mode((600,400))
pygame.display.set_caption("Dondurme Demo")
saat=pygame.time.Clock()

hiz=2

# üçgen şeklinde görsel
orijinal = pygame.Surface((64,64),pygame.SRCALPHA)
pygame.draw.polygon(orijinal, (255,200,0), [(32,4),(4,60),(60,60)])
aci=0

#talep2
gemi = pygame.Surface((64,64),pygame.SRCALPHA)
pygame.draw.polygon(gemi, (0,200,255), [(32,4),(4,60),(60,60)])
gemi_rect=gemi.get_rect(center=(150,150))
t_aci=0

font = pygame.font.SysFont("Arial", 16)

çalıştır=True
while çalıştır:
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            çalıştır=False
                
    tuslar = pygame.key.get_pressed()
    if tuslar[pygame.K_UP]:
        hiz+=0.1
    if tuslar[pygame.K_DOWN]:
        hiz-=0.1
                
    mouse_pos = pygame.mouse.get_pos()
    dx,dy=mouse_pos[0]-gemi_rect.x,mouse_pos[1]-gemi_rect.y
    t_aci=math.degrees(math.atan2(-dy,dx))-90
       
    aci+=2
    aci+=hiz
    if aci >= 360:
        aci-=360
        
    # Orijinden döndür, center koru
    donmus=pygame.transform.rotate(orijinal,aci)
    rect=donmus.get_rect(center=(300,200))
    
    ekran.fill((20,20,40))
    
    pygame.draw.line(ekran, (200,200,200), (gemi_rect.x+32,gemi_rect.y+32), (mouse_pos[0],mouse_pos[1]), 5)
    
    ekran.blit(donmus,rect)
    
    g_don=pygame.transform.rotate(gemi,t_aci)
    ekran.blit(g_don,gemi_rect)
    
    hiz_bilg = font.render(f"Hız: {hiz:.2f}", True, (255,255,255))
    ekran.blit(hiz_bilg,(5,5))
    
    aci_bilg = font.render(f"Açı: {t_aci:.2f}", True, (255,255,255))
    ekran.blit(aci_bilg,(5,20))
    
    pygame.display.flip()
    saat.tick(60)
    
pygame.quit()