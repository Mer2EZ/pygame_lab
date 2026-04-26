# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 02:47:09 2026

@author: Mert
"""

import pygame

pygame.init()
ekran=pygame.display.set_mode((600,400))
pygame.display.set_caption("Cevirme Demo")
saat=pygame.time.Clock()

aci=-90

# üçgen şeklinde görsel
orijinal = pygame.Surface((64,64),pygame.SRCALPHA)
pygame.draw.polygon(orijinal, (255,200,0), [(32,4),(4,60),(60,60)])

font = pygame.font.SysFont("Arial", 16)

çalıştır=True
while çalıştır:
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            çalıştır=False
        if olay.type == pygame.KEYDOWN:
            if olay.key == pygame.K_UP:
                aci=0
            elif olay.key == pygame.K_RIGHT:
                aci=-90
            elif olay.key == pygame.K_DOWN:
                aci=180
            elif olay.key == pygame.K_LEFT:
                aci=90
                
    donmus=pygame.transform.rotate(orijinal,aci)
    rect=donmus.get_rect(center=(300,200))
    
    ekran.fill((20,20,40))
    
    ekran.blit(donmus,rect)
    
    yansima=pygame.transform.flip(donmus,False,False)
    yansima.set_alpha(80)
    ekran.blit(yansima,(donmus.get_width()+208,donmus.get_height()+108))
    
    pygame.display.flip()
    saat.tick(60)
    
pygame.quit()