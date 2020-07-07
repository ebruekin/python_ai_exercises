# -*- coding: utf-8 -*-


import pygame , sys

pygame.init() # ben pygame modulündeki fonksiytonları kullanacagım onları bana getir

pencereBoyutu = (1400,500) # pencerenin pixel olarak boyutlarını verdim


font = pygame.font.SysFont("PrimarySchool",48) # fontumuzu tanımladık bilgisayarımızda kayıtlı olan bi font olması lazım

ekranYazı = font.render("ebru bunlar yalan sen kaşarsın ben tulum bok :,( ",1,(0,0,0),(0,250,0)) # yazının rgb değeri ve arka planın rgb değerini girdim

yazıBoyutuX = ekranYazı.get_size()[0] # yazının boyutunu aldık

print(yazıBoyutuX)

pencere = pygame.display.set_mode(pencereBoyutu) 
x = 0
y = 0
xYon = 1
clock = pygame.time.Clock()
while True:
    clock.tick(40) # fps 
    for event in pygame.event.get(): # bu döngünün amacı pencere üzerinde işlem yapabilmemizi sağlar mause vb ile
        if event.type == pygame.QUIT:sys.exit()
    pencere.fill((0,0,0))   
    
    if x > 1400 - yazıBoyutuX  or  x < 0: #saga çarpıp döbnmesi için 800 den çıkardık
        xYon *= -1
    
    
    
    x+=5 * xYon
    pencere.blit(ekranYazı,(x,y)) # yazımız ekrana yazdırırve konumunu belirtiriz bu aşamada
    pygame.display.update() # pencerenin sürekli olarak açık kalmasını sağlar