# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:06:04 2026

@author: Mert
"""

import pygame
import random
import sys

pygame.init()

GENISLIK=800
YUKSEKLIK=600

HUCRE=20
SATIR=YUKSEKLIK//HUCRE
SUTUN=GENISLIK//HUCRE

ekran=pygame.display.set_mode((GENISLIK,YUKSEKLIK))
pygame.display.set_caption("Yılan")
saat=pygame.time.Clock()
FPS=12

ARKAPLAN=(200,200,200)
YILAN=(100,250,100)
YILAN_BASI=(10,150,10)
YEM=(200,0,0)
SIYAH=(0,0,0)
BEYAZ=(255,255,255)

ADIM=10
sayac=0

YUKARI = (0, -1)
ASAGI = (0, 1)
SOL = (-1, 0)
SAG = (1, 0)

def yem_olustur(yilan):
    while True:
        konum = (random.randint(0, SUTUN - 1), random.randint(0, SATIR - 1))
        if konum not in yilan:
            return konum
        
def hucreye_ciz(ekran, konum, renk):
    x = konum[0] * HUCRE
    y = konum[1] * HUCRE
    pygame.draw.rect(ekran, renk, (x, y, HUCRE, HUCRE))
    
def sifirla():
    skor = 0
    baslangic_x = SUTUN // 2
    baslangic_y = SATIR // 2
    yilan = [(baslangic_x, baslangic_y),
             (baslangic_x - 1, baslangic_y)]
    yon = SAG
    yem = yem_olustur(yilan)
    oyun_bitti = False
    return yilan, yon, skor, yem, oyun_bitti

yilan, yon, skor, yem, oyun_bitti = sifirla()

font = pygame.font.Font(None, 32)

çalıştır = True
while çalıştır:
    saat.tick(FPS)
    for olay in pygame.event.get():
        if olay.type==pygame.QUIT:
            çalıştır=False
        if olay.type == pygame.KEYDOWN:
            if olay.key == pygame.K_ESCAPE:
                çalıştır=False
            if oyun_bitti:
                if olay.key == pygame.K_r:
                    yilan, yon, skor, yem, oyun_bitti = sifirla()
                continue
            
            if olay.key == pygame.K_w and yon != ASAGI:
                yon = YUKARI
            elif olay.key == pygame.K_s and yon != YUKARI:
                yon = ASAGI
            elif olay.key == pygame.K_a and yon != SAG:
                yon = SOL
            elif olay.key == pygame.K_d and yon != SOL:
                yon = SAG
            
    if not oyun_bitti:
        bas_x, bas_y = yilan[0]
        yeni_bas = (bas_x + yon[0], bas_y + yon[1])
        
        yb_x, yb_y = yeni_bas
        if yb_x < 0 or yb_x >= SUTUN:
            oyun_bitti = True
        elif yb_y < 0 or yb_y >= SATIR:
            oyun_bitti = True
        # Kendine carpma kontrolu
        elif yeni_bas in yilan:
            oyun_bitti = True
            
        if not oyun_bitti:
            yilan.insert(0, yeni_bas)
            
            if yeni_bas == yem:
                skor += 1
                yem = yem_olustur(yilan)
            else:
                yilan.pop()
    
    ekran.fill(ARKAPLAN)
    
    for x in range(0, GENISLIK, HUCRE):
        pygame.draw.line(ekran, SIYAH, (x, 0), (x, YUKSEKLIK))
    for y in range(0, YUKSEKLIK, HUCRE):
        pygame.draw.line(ekran, SIYAH, (0, y), (GENISLIK, y))
    
    hucreye_ciz(ekran, yem, YEM)
    
    for i, vucut in enumerate(yilan):
        if i == 0:
            hucreye_ciz(ekran, vucut, YILAN_BASI)
        else:
            hucreye_ciz(ekran, vucut, YILAN)
    
    skor_yazi = font.render(f"Skor: {skor}", True, BEYAZ)
    ekran.blit(skor_yazi, (10, 10))
    
    if oyun_bitti:
        ekran.fill(SIYAH)
        
        skor_bilgi = font.render(f"Skor: {skor}", True, BEYAZ)
        skor_rect = skor_bilgi.get_rect(center=(GENISLIK // 2, YUKSEKLIK // 2 -25))
        ekran.blit(skor_bilgi, skor_rect)
        
        tekrar_yazi = font.render("r'ye basarak tekrar başlatabilirsiniz!", True, BEYAZ)
        tekrar_rect = tekrar_yazi.get_rect(center=(GENISLIK // 2, YUKSEKLIK // 2 + 25))
        ekran.blit(tekrar_yazi, tekrar_rect)
    
    pygame.display.flip()

pygame.quit ()
sys.exit ()