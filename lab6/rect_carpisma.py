# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 05:34:23 2026

@author: Mert
"""

import pygame
import random

pygame.init()

ekran=pygame.display.set_mode((800,600))
pygame.display.set_caption("Rect Çarpışma Testi")
saat=pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

oyuncu=pygame.Rect(100,250,60,60)
engel1=pygame.Rect(350,250,80,80)
engel2=pygame.Rect(400,350,60,30)
engel3=pygame.Rect(520,400,50,100)
hiz=4

liste=[0,0,0]
sayac=0

engeller=[]

çalıştır=True
while çalıştır:
    for olay in pygame.event.get():
        if olay.type==pygame.QUIT:
            çalıştır=False
        if olay.type==pygame.KEYDOWN:
            if olay.key == pygame.K_ESCAPE:
                çalıştır=False
        #talep3
        if olay.type == pygame.MOUSEBUTTONDOWN:
            if olay.button == 1:
                g,y=random.randint(40, 100),random.randint(40, 100)
                e=pygame.Rect(random.randint(1, 800-g),random.randint(1, 600-y),g,y)
                engeller.append(e)
            if olay.button == 3:
                fare_konumu = pygame.mouse.get_pos()
                for i in range(len(engeller)):
                    if engeller[i].collidepoint(fare_konumu):
                        engeller.pop(i)
                        break
            
    tuslar=pygame.key.get_pressed()
    if tuslar [pygame.K_a]: oyuncu.x -= hiz
    if tuslar [pygame.K_d]: oyuncu.x += hiz
    if tuslar [pygame.K_w]: oyuncu.y -= hiz
    if tuslar [pygame.K_s]: oyuncu.y += hiz
    
    fare_x,fare_y=pygame.mouse.get_pos()
    fare_engelde1=engel1.collidepoint(fare_x, fare_y)
    fare_engelde2=engel2.collidepoint(fare_x, fare_y)
    fare_engelde3=engel3.collidepoint(fare_x, fare_y)
    
    carpisma1=oyuncu.colliderect(engel1)
    carpisma2=oyuncu.colliderect(engel2)
    carpisma3=oyuncu.colliderect(engel3)
    
    ekran.fill((20,20,40))
        
    renk_engel1=(231,76,60) if carpisma1 else (46,204,113)
    renk_engel2=(231,76,60) if carpisma2 else (46,204,113)
    renk_engel3=(231,76,60) if carpisma3 else (46,204,113)
    renk_oyuncu=(231,76,60) if carpisma1 or carpisma2 or carpisma3 else (52,152,219)
    
    pygame.draw.rect(ekran,renk_engel1,engel1)
    pygame.draw.rect(ekran,renk_engel2,engel2)
    pygame.draw.rect(ekran,renk_engel3,engel3)
    pygame.draw.rect(ekran,renk_oyuncu,oyuncu)
    
    if fare_engelde1:
        pygame.draw.rect(ekran,(241,196,15),engel1,3)
    if fare_engelde2:
        pygame.draw.rect(ekran,(241,196,15),engel2,3)
    if fare_engelde3:
        pygame.draw.rect(ekran,(241,196,15),engel3,3)
        
    durum="CARPISMA VAR!" if carpisma1 or carpisma2 or carpisma3 else "CARPISMA YOK!"
    ekran.blit(font.render(durum,True,(255,255,255)),(10,10))
    if fare_engelde1 or fare_engelde2 or fare_engelde3:
        ekran.blit(font.render("Fare Engelde!",True,(241,196,15)),(10,40))
        
    #talep2
    if carpisma1:
        liste[0]=1 
    if carpisma2:
        liste[1]=1 
    if carpisma3:
        liste[2]=1 
        
    sayac=sum(liste)
        
    ekran.blit(font.render(f"Carpisma: {sayac}", True, (255,255,255)),(700,10))
        
    for i in engeller:
        pygame.draw.rect(ekran,(50,50,50),i)
    
    pygame.display.flip()
    saat.tick(60)
    
pygame.quit()