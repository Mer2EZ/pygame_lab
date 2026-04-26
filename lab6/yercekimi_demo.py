# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 18:08:03 2026

@author: Mert
"""

import pygame

pygame.init()
GENISLIK,YUKSEKLIK=800,600

ekran=pygame.display.set_mode((GENISLIK,YUKSEKLIK))
pygame.display.set_caption("Yercekimi Simulasyonu")
saat=pygame.time.Clock()
font=pygame.font.SysFont("Arial", 18)

#Fizik sabitleri
YERCEKIMI=0.5
SURTUNME=0.98
ZEMIN_Y=550

class Top(pygame.sprite.Sprite):
    def __init__(self,x,y,renk=(52,152,219)):
        super().__init__()
        self.yaricap=15
        self.image=pygame.Surface((self.yaricap*2,self.yaricap*2),pygame.SRCALPHA)
        pygame.draw.circle(self.image,renk,(self.yaricap,self.yaricap),self.yaricap)
        self.rect=self.image.get_rect(center=(x,y))
        self.hiz_x=0.0
        self.hiz_y=0.0
        
    def update(self):
        #yercekimi uygula
        self.hiz_y += YERCEKIMI
        
        #surtunme (yatay)
        self.hiz_x *= SURTUNME
        
        #konumu güncelle
        self.rect.x += self.hiz_x
        self.rect.y += self.hiz_y
        
        #zemin çarpışma ve geri sekme
        if self.rect.bottom >= ZEMIN_Y:
            self.rect.bottom = ZEMIN_Y
            self.hiz_y *= -0.7 # enerji kaybı ile sekme
            #talep 2
            self.hiz_x*=0.92
            if abs(self.hiz_x) < 0.1 and abs(self.hiz_y < 0.5):
                self.hiz_x=0
                self.hiz_y=0
        
        #duvar çarpışma
        if self.rect.left <0:
            self.rect.left =0
            self.hiz_x*=-0.8
        elif self.rect.right > GENISLIK:
            self.rect.right = GENISLIK
            self.hiz_x*=-0.8
            
#gruplar
tum_spritelar=pygame.sprite.Group()

#Başlangıç Topu
top=Top(GENISLIK//2,100)
tum_spritelar.add(top)

surukleniyor=False
baslangic_pos=(0,0)

çalıştır=True
while çalıştır:
    for olay in pygame.event.get():
        if olay.type == pygame.QUIT:
            çalıştır=False
        elif olay.type == pygame.MOUSEBUTTONDOWN:
            if olay.button==1:
                surukleniyor=True
                baslangic_pos=olay.pos
        elif olay.type == pygame.MOUSEBUTTONUP:
            if olay.button ==1 and surukleniyor:
                surukleniyor=False
                bx,by=baslangic_pos
                ex,ey=olay.pos
                yeni_top=Top(bx,by,(231,76,60))
                yeni_top.hiz_x=(bx-ex)*0.15
                yeni_top.hiz_y=(by-ey)*0.15
                tum_spritelar.add(yeni_top)
                
    #talep 1
    tuslar=pygame.key.get_pressed()
    if tuslar[pygame.K_UP]:
        YERCEKIMI+=0.05
        if YERCEKIMI>2.0:
            YERCEKIMI=2.0
    if tuslar[pygame.K_DOWN]:
        YERCEKIMI-=0.05
        if YERCEKIMI<0.1:
            YERCEKIMI=0.1
    
    tum_spritelar.update()
    
    ekran.fill((20,20,40))
    
    #zemin çizgisi
    pygame.draw.line(ekran,(100,100,100), (0,ZEMIN_Y), (GENISLIK,ZEMIN_Y),2)
    
    #firlatma oku
    if surukleniyor:
        fare=pygame.mouse.get_pos()
        pygame.draw.line(ekran,(241,196,15), baslangic_pos, fare,2)
        
    #talep 3
    """
    for top in tum_spritelar:
        carpisan=pygame.sprite.spritecollide(top, tum_spritelar, False)
        for diger in carpisan:
            if diger != top:
                #hız değiştir
                top.hiz_x, diger.hiz_x = diger.hiz_x, top.hiz_x
                top.hiz_y, diger.hiz_y = diger.hiz_y, top.hiz_y
    """
    # talep 3 # daha iyi çalışıyor
    carpismalar = pygame.sprite.groupcollide(tum_spritelar, tum_spritelar, False, False)

    islenen_ciftler = set()
    
    for top, carpanlar in carpismalar.items():
        for diger in carpanlar:
            if top != diger and (diger, top) not in islenen_ciftler:
                # hız değiştir
                top.hiz_x, diger.hiz_x = diger.hiz_x, top.hiz_x
                top.hiz_y, diger.hiz_y = diger.hiz_y, top.hiz_y
                islenen_ciftler.add((top, diger))
        
    tum_spritelar.draw(ekran)
    
    bilgi=font.render(f"Top Sayısı: {len(tum_spritelar)} | "
                      f"Tıklayıp Sürükle: firlatma",
                      True, (200,200,200))
    ekran.blit(bilgi,(10,10))
    
    yc=font.render(f"Yerçekimi: {YERCEKIMI:.2f}",True,(200,200,200))
    ekran.blit(yc,(10,30))
    
    pygame.display.flip()
    saat.tick(60)
    
pygame.quit()