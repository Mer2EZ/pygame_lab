# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 04:05:44 2026

@author: Mert
"""

import pygame
import sys
import random

pygame.init()

GENISLIK,YUKSEKLIK=800,600

ekran=pygame.display.set_mode((GENISLIK,YUKSEKLIK))
pygame.display.set_caption("Temel Sprite")
saat=pygame.time.Clock()

METEOR_OLUSTUR = pygame.USEREVENT + 1
pygame.time.set_timer(METEOR_OLUSTUR, 2000)

tum_spritelar=pygame.sprite.Group()

class Oyuncu(pygame.sprite.Sprite):
    def __init__(self, renk, x, y, boyut=25):
        super().__init__()
        self.image=pygame.Surface((boyut,boyut),pygame.SRCALPHA)
        pygame.draw.rect(self.image,renk,(0,0,boyut,boyut),border_radius=5)
        self.rect=self.image.get_rect(center=(x,y))
        self.hiz=5
        
    def update(self):
        tuslar = pygame.key.get_pressed()
        if tuslar[pygame.K_w]:
            self.rect.y-=self.hiz
        if tuslar[pygame.K_d]:
            self.rect.x+=self.hiz
        if tuslar[pygame.K_s]:
            self.rect.y+=self.hiz
        if tuslar[pygame.K_a]:
            self.rect.x-=self.hiz
            
        ekran_rect=pygame.display.get_surface().get_rect()
        self.rect.clamp_ip(ekran_rect)
        
oyuncu=Oyuncu((180,250,250),400,500)
oyuncular=pygame.sprite.Group(oyuncu)
        
class Efekt(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.renk=(random.randint(200,255),random.randint(100,200),0)
        self.image=pygame.Surface((20,20),pygame.SRCALPHA)
        self.image.set_alpha(75)
        pygame.draw.circle(self.image,self.renk,(10,10),10)
        self.rect=self.image.get_rect(center=(x,y))
        self.hiz_x=random.choice([-1.5,-1,1,1.5])
        self.hiz_y=random.choice([-1.5,-1,1,1.5])
        self.olum_zamani = pygame.time.get_ticks() + 250
        
    def update(self):
        self.rect.x += self.hiz_x
        self.rect.y += self.hiz_y
        if pygame.time.get_ticks() > self.olum_zamani:
            self.kill()
            
efektler=pygame.sprite.Group()

class Yildiz(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.boyut=random.randint(1, 3)
        cap=self.boyut*2
        self.image=pygame.Surface((cap,cap),pygame.SRCALPHA)
        parlaklik=100+self.boyut*50
        renk=(parlaklik,parlaklik,parlaklik)
        pygame.draw.circle(self.image,renk,(self.boyut,self.boyut),self.boyut)
        self.rect=self.image.get_rect()
        self.rect.x=random.randint(0,800)
        self.rect.y=random.randint(0,600)
        self.hiz=self.boyut*0.8+random.uniform(0,1)
        
    def update(self):
        self.rect.y += self.hiz
        if self.rect.top > 600:
            self.rect.x = random.randint(0,800)
            self.rect.bottom=0
        #parallax
        if self.boyut == 2:
            self.rect.y += 0.5*self.hiz
        elif self.boyut == 3:
            self.rect.y += self.hiz
            
yildizlar=pygame.sprite.Group([Yildiz() for i in range(60)])

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.boyut=random.randint(1, 3)
        cap=self.boyut*20
        self.image=pygame.Surface((cap,cap),pygame.SRCALPHA)
        renk=(random.randint(225,255),random.randint(150,250),0)
        pygame.draw.circle(self.image,renk,(cap//2,cap//2),cap//2)
        self.rect=self.image.get_rect()
        self.rect.x=random.randint(0,800-cap)
        self.rect.y=-cap
        self.hiz=2.5+random.uniform(0,1)

    def update(self):
        if self.rect.top > 600:
            self.kill()
        if self.boyut == 1:
            self.rect.y += self.hiz
        elif self.boyut == 2:
            self.rect.y += 0.75*self.hiz
        elif self.boyut == 3:
            self.rect.y += 0.5*self.hiz
            
meteorlar=pygame.sprite.Group()

tum_spritelar.add(yildizlar)
tum_spritelar.add(meteorlar)
tum_spritelar.add(efektler)
tum_spritelar.add(oyuncular)

font = pygame.font.SysFont("Arial", 16)

sayac=0
st_t=pygame.time.get_ticks()

çalıştır=True
while çalıştır:
    saat.tick(60)
    for olay in pygame.event.get():
        if olay.type==pygame.QUIT:
            çalıştır=False
        if olay.type == METEOR_OLUSTUR:
            yeni_meteor = Meteor()
            meteorlar.add(yeni_meteor)
            tum_spritelar.add(yeni_meteor)
            
    sayac=(pygame.time.get_ticks()-st_t)/1000
    
    yeni_efekt = Efekt(oyuncu.rect.centerx, oyuncu.rect.centery)
    efektler.add(yeni_efekt)
    tum_spritelar.add(yeni_efekt)
    
    tum_spritelar.update()
    
    ekran.fill((20,20,20))
    
    tum_spritelar.draw(ekran)
    
    sayac_bilgi=font.render(f"Süre(saniye): {sayac:.0f}", True, (255,255,255))
    ekran.blit(sayac_bilgi,(5,5))
    fps_bilgi=font.render(f"FPS: {saat.get_fps():.2f}",True,(255,255,255))
    ekran.blit(fps_bilgi,(730,5))
    
    pygame.display.flip()
    
pygame.quit()
sys.exit()