# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 18:39:43 2026

@author: Mert
"""

import pygame
import math
import random

pygame.init()
GENISLIK,YUKSEKLIK=800,600
FPS=60

skor=0  
canlar=3

SIYAH=(0,0,0)
BEYAZ=(255,255,255)
KIRMIZI=(255,0,0)
MAVI=(0,0,255)
YESIL=(0,255,0)
MOR=(155,90,180)
GRI=(155,155,155)

raket_g,raket_y=120,15
raket_hiz=7.5
raket_renk=(155,55,175)

top_r=8
top_hiz=5
top_renk=BEYAZ

tugla_g,tugla_y=60,30
tugla_bosluk=5
tugla_satir,tugla_sutun=5,10 

ekran=pygame.display.set_mode((GENISLIK,YUKSEKLIK))
pygame.display.set_caption("BreakOut")
saat=pygame.time.Clock()
font=pygame.font.SysFont("Arial", 18)

class Raket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((raket_g,raket_y))
        self.image.fill(raket_renk)
        self.rect=self.image.get_rect()
        self.rect.centerx=GENISLIK//2
        self.rect.bottom=YUKSEKLIK-30
        self.hiz=raket_hiz
        
    def update(self):
        tuslar=pygame.key.get_pressed()
        if tuslar[pygame.K_d]:
            self.rect.x+=self.hiz
        if tuslar[pygame.K_a]:
            self.rect.x-=self.hiz
        
        ekran_rect=pygame.display.get_surface().get_rect()
        self.rect.clamp_ip(ekran_rect)
        

class Top(pygame.sprite.Sprite):
    def __init__(self,raket):
        super().__init__()
        self.image=pygame.Surface((top_r*2,top_r*2),pygame.SRCALPHA)
        pygame.draw.circle(self.image,top_renk,(top_r,top_r),top_r)
        self.rect=self.image.get_rect()
        self.raket=raket
        
        self.rect.midbottom=self.raket.rect.midtop
        self.hiz_x=0
        self.hiz_y=0
        self.aktif=False
        
    def firlat(self):
        if not self.aktif:
            self.aktif=True
            aci=random.uniform(math.radians(220),math.radians(320))
            self.hiz_x=top_hiz*math.cos(aci)
            self.hiz_y=top_hiz*math.sin(aci)
        
    def update(self):
        if not self.aktif:
            self.rect.midbottom=self.raket.rect.midtop
            return
        
        self.rect.x += self.hiz_x
        self.rect.y += self.hiz_y
        
        if self.rect.left <=0:
            self.rect.left =0
            self.hiz_x=abs(self.hiz_x)
        elif self.rect.right >= GENISLIK:
            self.rect.right = GENISLIK
            self.hiz_x=-abs(self.hiz_x)
            
        if self.rect.top <= 0:
            self.rect.top =0
            self.hiz_y =abs(self.hiz_y)
        if self.rect.top > YUKSEKLIK:
            global canlar
            canlar -= 1
            self.aktif = False
            self.rect.midbottom = self.raket.rect.midtop
            self.hiz_x = 0
            self.hiz_y = 0
            
def raket_top_carpisma(top,raket):
    if not top.aktif:
        return
    
    if top.rect.colliderect(raket.rect) and top.hiz_y > 0:
        carpisma_noktasi=((top.rect.centerx-raket.rect.left)/raket.rect.width)
        oran=max(0,min(1,carpisma_noktasi))
        aci=math.radians(150-(oran*120))
        
        hiz=top_hiz
        top.hiz_x=hiz*math.cos(aci)
        top.hiz_y=-abs(hiz*math.sin(aci))
        
        top.rect.bottom=raket.rect.top    
            
tugla_turleri={
    1:(KIRMIZI,1), # 1 vuruş
    2:(MAVI,2), # 2 vuruş
    3:(YESIL,3), # 3 vuruş
    4:(MOR,4), # 4 vuruş
    5:(GRI,5)} # 5 vuruş

class Tugla(pygame.sprite.Sprite):
    def __init__(self,x,y,tur=1):
        super().__init__()
        renk,self.can=tugla_turleri.get(tur,(BEYAZ,1))
        self.max_can=self.can
        self.renk=renk
        self.puan=tur*10
        
        self.image=pygame.Surface((tugla_g,tugla_y))
        self._gorsel_guncelle()
        self.rect=self.image.get_rect(topleft=(x,y))
        
    def _gorsel_guncelle(self):
        self.image.fill(self.renk)
        pygame.draw.rect(self.image,BEYAZ,(0,0,tugla_g,tugla_y),1)
    
    def hasar_al(self):
        if self.can == -1:
            return False
        
        self.can -=1
        if self.can <= 0:
            self.kill()
            return True
        
        self._gorsel_guncelle()
        return False
        
def tugla_olustur(tugla_grubu,tum_spritelar):
    toplam_genislik=(tugla_sutun*(tugla_g+tugla_bosluk)-tugla_bosluk)
    baslangic_x=(GENISLIK-toplam_genislik)//2
    
    for satir in range(tugla_satir):
        for sutun in range(tugla_sutun):
            x=baslangic_x+sutun*(tugla_g+tugla_bosluk)
            y=50+satir*(tugla_y+tugla_bosluk)
            
            tur=tugla_satir-satir
            tugla=Tugla(x,y,tur)
            tugla_grubu.add(tugla)
            tum_spritelar.add(tugla)
     
def top_tugla_carpisma(top,tugla_grubu):
    global skor
    
    if not top.aktif:
        return
    
    carpisan=pygame.sprite.spritecollide(top,tugla_grubu,False)
    
    for tugla in carpisan:
        dx,dy=top.rect.centerx-tugla.rect.centerx,top.rect.centery-tugla.rect.centery
        
        if abs(dx) / tugla.rect.width > abs(dy)/tugla.rect.height:
            top.hiz_x=-top.hiz_x
        else:
            top.hiz_y=-top.hiz_y
            
        kirildi=tugla.hasar_al()
        if kirildi:
            skor+=tugla.puan
            
        break
                
tum_spritelar=pygame.sprite.Group()
tugla_grubu=pygame.sprite.Group()

raket=Raket()
top=Top(raket)
tum_spritelar.add(raket,top)

tugla_olustur(tugla_grubu, tum_spritelar)

oyun_kazanildi=None

çalıştır=True
while çalıştır:
    saat.tick(FPS)
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            çalıştır=False
        elif olay.type == pygame.KEYDOWN:
            if olay.key == pygame.K_SPACE:
                top.firlat()
                
    tum_spritelar.update()
    
    raket_top_carpisma(top,raket)
    
    top_tugla_carpisma(top, tugla_grubu)
            
    kirilmaz=[t for t in tugla_grubu if t.can==-1]
    if len(tugla_grubu)<=len(kirilmaz):
        oyun_kazanildi=True
        
    if canlar < 1:
        oyun_kazanildi=False
    
    ekran.fill((200,200,200))
    tum_spritelar.draw(ekran)
    
    skor_yazi=font.render(f"Skor: {skor}",True,BEYAZ)
    can_yazi=font.render(f"Can: {canlar}",True,BEYAZ)
    ekran.blit(skor_yazi,(10,10))
    ekran.blit(can_yazi,(GENISLIK-100,10))
    
    if oyun_kazanildi == True:
        ekran.fill((0,0,0))
        ekran.blit(font.render("Tebrikler KAZANDINIZ!",True,BEYAZ),(GENISLIK//4,YUKSEKLIK//2-20))
        ekran.blit(skor_yazi,(GENISLIK//4,YUKSEKLIK//2))
        ekran.blit(can_yazi,(GENISLIK//4,YUKSEKLIK//2+20))
    elif oyun_kazanildi == False:
        ekran.fill((0,0,0))
        ekran.blit(font.render("GAME OVER!",True,BEYAZ),(GENISLIK//4,YUKSEKLIK//2-20))
        ekran.blit(skor_yazi,(GENISLIK//4,YUKSEKLIK//2))
        ekran.blit(can_yazi,(GENISLIK//4,YUKSEKLIK//2+20))
    
    pygame.display.flip()
    
pygame.quit()