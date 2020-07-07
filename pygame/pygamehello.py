# -*- coding: utf-8 -*-
"""
Created on Fri May 29 15:33:42 2020

@author: Perona
"""

import pygame , sys

pygame.init() # ben pygame modulündeki fonksiytonları kullanacagım onları bana getir

pencereBoyutu = (800,500) # pencerenin pixel olarak boyutlarını verdim


font = pygame.font.SysFont("PrimarySchool",48) # fontumuzu tanımladık bilgisayarımızda kayıtlı olan bi font olması lazım

ekranYazı = font.render("pygame çalışması ",1,(0,0,0),(0,250,0)) # yazının rgb değeri ve arka planın rgb değerini girdim



pencere = pygame.display.set_mode(pencereBoyutu) 
x = 0
y = 0

clock = pygame.time.Clock()
while True:
    clock.tick(40) # fps 
    for event in pygame.event.get(): # bu döngünün amacı pencere üzerinde işlem yapabilmemizi sağlar mause vb ile
        if event.type == pygame.QUIT:sys.exit()
    pencere.fill((0,0,0))   
    x+=5
    pencere.blit(ekranYazı,(x,y)) # yazımız ekrana yazdırırve konumunu belirtiriz bu aşamada
    pygame.display.update() # pencerenin sürekli olarak açık kalmasını sağlar