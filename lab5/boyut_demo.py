# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 01:29:27 2026

@author: Mert
"""

import pygame

pygame.init()
GENISLIK=800
YUKSEKLIK=600

BEYAZ=(255,255,255)

font = pygame.font.SysFont("Arial", 16)

ekran=pygame.display.set_mode((GENISLIK,YUKSEKLIK))
pygame.display.set_caption("Boyut degistirme")
saat=pygame.time.Clock()

def boyut_oranli(surface,hedef_genislik):
    oran=hedef_genislik/surface.get_width()
    yeni_yuk=int(surface.get_height()*oran)
    return pygame.transform.scale(surface,(hedef_genislik,yeni_yuk))

# yedek gorsel oluştur
orijinal = pygame.Surface((64,64),pygame.SRCALPHA)
pygame.draw.polygon(orijinal, (0,150,255), [(32,4),(4,60),(60,60)])

# farklı boyutlarda kopyalar
kucuk=pygame.transform.scale(orijinal, (32,32))
buyuk=pygame.transform.scale(orijinal, (128,128))
smooth=pygame.transform.smoothscale(orijinal, (128,128))

font = pygame.font.SysFont("Arial", 16)

#talep2
dikdortgen = pygame.Surface((100,50),pygame.SRCALPHA)
pygame.draw.rect(dikdortgen, (0,150,255), (0,0,100,50))
oranli=boyut_oranli(dikdortgen, 200)
bozuk=pygame.transform.scale(dikdortgen, (200,200))

#talep3
kare=pygame.Surface((50,50),pygame.SRCALPHA)
pygame.draw.rect(kare, (255,0,0), (0,0,50,50))
gens,yuks=50,50
karey=pygame.transform.scale(kare,(gens,yuks))

çalıştır=True
while çalıştır:
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            çalıştır=False
        if olay.type == pygame.MOUSEWHEEL:
            if olay.y >0:
                if gens >= 16 and gens <256:
                    gens+=1
                    yuks+=1
                    karey=pygame.transform.scale(kare,(gens,yuks))
            if olay.y <0:
                if gens > 16 and gens <=256:
                    gens-=1
                    yuks-=1
                    karey=pygame.transform.scale(kare,(gens,yuks))
            
    ekran.fill((20,20,20))
    
    #talep1
    kucuk_bilgi = font.render("32x32", True, BEYAZ)
    ekran.blit(kucuk,(100,150))
    ekran.blit(kucuk_bilgi,(100,180))
    
    orj_bilgi = font.render("64x64", True, BEYAZ)
    ekran.blit(orijinal,(250,120))
    ekran.blit(orj_bilgi,(265,180))
    
    buyuk_bilgi = font.render("128x128", True, BEYAZ)
    ekran.blit(buyuk,(400,90))
    ekran.blit(buyuk_bilgi,(440,210))
    
    smooth_bilgi = font.render("128x128", True, BEYAZ)
    ekran.blit(smooth,(600,90))
    ekran.blit(smooth_bilgi,(640,210))
    
    ekran.blit(dikdortgen,(100,300))
    ekran.blit(oranli,(250,300))
    ekran.blit(bozuk,(500,300))
    
    ekran.blit(karey,(375,275))
    
    pygame.display.flip()
    saat.tick(60)
    
pygame.quit()