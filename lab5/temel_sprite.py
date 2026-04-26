# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 02:58:16 2026

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

tum_spritelar=pygame.sprite.Group()

# Basit Sprite Sınfı
class Kutu(pygame.sprite.Sprite):
    def __init__(self, renk, x, y, boyut=50):
        super().__init__()
        self.image=pygame.Surface((boyut,boyut),pygame.SRCALPHA)
        pygame.draw.rect(self.image,renk,(0,0,boyut,boyut),border_radius=5)
        self.rect=self.image.get_rect(center=(x,y))
        self.hiz=2
    
    def update(self):
        #talep1
        tuslar = pygame.key.get_pressed()
        if tuslar[pygame.K_UP]:
            self.rect.y-=self.hiz
        if tuslar[pygame.K_RIGHT]:
            self.rect.x+=self.hiz
        if tuslar[pygame.K_DOWN]:
            self.rect.y+=self.hiz
        if tuslar[pygame.K_LEFT]:
            self.rect.x-=self.hiz
            
        ekran_rect=pygame.display.get_surface().get_rect()
        self.rect.clamp_ip(ekran_rect)
        
kutu1=Kutu((0,180,255),200,YUKSEKLIK//2)
kutu2=Kutu((255,180,0),400,YUKSEKLIK//2)
kutu3=Kutu((0,180,0),600,YUKSEKLIK//2)
grup=pygame.sprite.Group(kutu1,kutu2,kutu3)

#talep2
class Top(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.renk=(random.randint(100,255),random.randint(100,255),random.randint(100,255))
        self.image=pygame.Surface((20,20),pygame.SRCALPHA)
        pygame.draw.circle(self.image,self.renk,(10,10),10)
        self.rect=self.image.get_rect(center=(random.randint(50,750),random.randint(50,550)))
        self.hiz_x=random.choice([-3,-2,2,3])
        self.hiz_y=random.choice([-3,-2,2,3])

    def update(self):
        self.rect.x += self.hiz_x
        self.rect.y += self.hiz_y
        if self.rect.left < 0 or self.rect.right > 800:
            self.hiz_x *= -1
        if self.rect.top < 0 or self.rect.bottom > 600:
            self.hiz_y *= -1
            
t_list=[Top() for i in range(15)]
toplar=pygame.sprite.Group(t_list)
            
#talep 3
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
            
yildizlar=pygame.sprite.Group([Yildiz() for i in range(50)])

tum_spritelar.add(grup)
tum_spritelar.add(toplar)
tum_spritelar.add(yildizlar)

font = pygame.font.SysFont("Arial", 16)

çalıştır=True
while çalıştır:
    saat.tick(60)
    for olay in pygame.event.get():
        if olay.type==pygame.QUIT:
            çalıştır=False
        if olay.type == pygame.KEYDOWN:
            #talep 2
            if olay.key == pygame.K_r:
                if len(t_list) >0:
                    t_list.pop()
                    for i in toplar:
                        a=i
                    a.kill()
                    #toplar=pygame.sprite.Group(t_list) # for yerine direkt bunu koysak???
            
    tum_spritelar.update()
    
    ekran.fill((20,20,20))
    
    tum_spritelar.draw(ekran)
    
    top_bilgi=font.render(f"Top Sayısı: {len(t_list)}", True, (255,255,255))
    ekran.blit(top_bilgi,(5,5))
    
    pygame.display.flip()
    
pygame.quit()
sys.exit()