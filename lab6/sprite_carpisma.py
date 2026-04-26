# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 06:30:14 2026

@author: Mert
"""

import pygame
import random

pygame.init()
GENISLIK,YUKSEKLIK=800,600

ekran=pygame.display.set_mode((GENISLIK,YUKSEKLIK))
pygame.display.set_caption("Sprite Çarpışma")
saat=pygame.time.Clock()
font=pygame.font.SysFont("Arial", 20)

class Oyuncu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((50,50),pygame.SRCALPHA)
        pygame.draw.rect(self.image,(52,152,219), (0,0,50,50),border_radius=5)
        self.rect=self.image.get_rect(center=(GENISLIK//2,YUKSEKLIK-80))
        
    def update(self):
        tuslar=pygame.key.get_pressed()
        if tuslar[pygame.K_a]:
            self.rect.x-=5
        if tuslar[pygame.K_d]:
            self.rect.x+=5
        if tuslar[pygame.K_w]:
            self.rect.y-=5
        if tuslar[pygame.K_s]:
            self.rect.y+=5
        
        self.rect.clamp_ip(ekran.get_rect())
        
        
class Dusman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.tip=random.randint(1, 2)
        if self.tip ==1:
            self.hiz = random.uniform(3,5)
            self.image=pygame.Surface((20,20),pygame.SRCALPHA)
            pygame.draw.rect(self.image,(60,76,231), (0,0,20,20),border_radius=3)
        elif self.tip ==2:
            self.hiz = random.uniform(1,2)
            self.image=pygame.Surface((50,50),pygame.SRCALPHA)
            pygame.draw.rect(self.image,(231,76,60), (0,0,50,50),border_radius=3)
        self.rect=self.image.get_rect(center=(random.randint(50 , 750) ,random.randint(-200 , -30)))
        
    def update(self):
        self.rect.y += self.hiz
        if self.rect.top > YUKSEKLIK:
            self.kill()
            
class Mermi(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.Surface((4,12),pygame.SRCALPHA)
        self.image.fill((241,196,15))
        self.rect=self.image.get_rect(center=(x,y))
        
    def update(self):
        self.rect.y -=8
        if self.rect.bottom < 0:
            self.kill()
            
# Gruplar
tum_spritelar=pygame.sprite.Group()
dusmanlar=pygame.sprite.Group()
mermiler=pygame.sprite.Group()

oyuncu=Oyuncu()
tum_spritelar.add(oyuncu)

# Dusman zamanlayici
DUSMAN_OLAY = pygame.USEREVENT+1
pygame.time.set_timer(DUSMAN_OLAY, 800)

skor=0
saglik=3

son_mermi=0

oyun=True

çalıştır=True
while çalıştır:
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            çalıştır=False
        elif olay.type == DUSMAN_OLAY:
            d=Dusman()
            tum_spritelar.add(d)
            dusmanlar.add(d)
        elif olay.type == pygame.KEYDOWN:
            if olay.key == pygame.K_SPACE:
                #talep 2
                simdiki_zaman=pygame.time.get_ticks()
                if simdiki_zaman - son_mermi > 250:
                    m=Mermi(oyuncu.rect.centerx, oyuncu.rect.top)
                    tum_spritelar.add(m)
                    mermiler.add(m)
                    son_mermi=simdiki_zaman
                
    tum_spritelar.update()
    
    # Mermi-Düşman Çarpışma (ikisi de silinecek)
    vurulanlar=pygame.sprite.groupcollide(mermiler, dusmanlar, True, True)
    #talep 3
    for mermi, carpisilan_dusmanlar in vurulanlar.items():
        for dusman in carpisilan_dusmanlar:
            if dusman.tip == 1:
                skor += 1
            elif dusman.tip == 2:
                skor += 3
    
    
    # Oyuncu-Düşman Çarpışma (düşmanı sil)
    carpisan=pygame.sprite.spritecollide(oyuncu, dusmanlar, True)
    if carpisan:
        saglik-=1
        skor=max(0,skor-2)
        
    ekran.fill((10,10,30))
    tum_spritelar.draw(ekran)
    
    yazi=font.render(f"Skor: {skor}", True, (255,255,255))
    ekran.blit(yazi,(10,10))
    
    can_b=font.render(f"Can: {saglik}", True, (255,255,255))
    ekran.blit(can_b,(740,10))
    
    #talep 1
    if saglik<=0:
        oyun=False
        
    if oyun==False:
        ekran.fill((0,0,0))
        go=font.render("GAME OVER",True,(250,250,250))
        ekran.blit(go,(GENISLIK//2-40,YUKSEKLIK//2-10))
        ekran.blit(yazi,(GENISLIK//2-20,YUKSEKLIK//2-30))
    
    pygame.display.flip()
    saat.tick(60)
    
pygame.quit()