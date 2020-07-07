# -*- coding: utf-8 -*-


import pygame , sys

pygame.init() # ben pygame modulündeki fonksiytonları kullanacagım onları bana getir

pencereBoyutu = (800,500) # pencerenin pixel olarak boyutlarını verdim

ball = pygame.image.load("ball.png")

topX = ball.get_size()[0] # topun boyutunu aldık
topY = ball.get_size()[1]
print(topX)

pencere = pygame.display.set_mode(pencereBoyutu) 
x = 0
y = 0
xYon = 1
yYon = 1
clock = pygame.time.Clock()
while True:
    clock.tick(40) # fps 
    for event in pygame.event.get(): # bu döngünün amacı pencere üzerinde işlem yapabilmemizi sağlar mause vb ile
        if event.type == pygame.QUIT:sys.exit()
    pencere.fill((255,255,255))   
    
    if x > 800 - topX  or  x < 0: #saga çarpıp döbnmesi için 800 den çıkardık
        xYon *= -1
    
    if y > 500 - topY or y<0:
        yYon *= -1
    
    
    x+=5 * xYon
    y+=5 * yYon
    pencere.blit(ball,(x,y)) # yazımız ekrana yazdırırve konumunu belirtiriz bu aşamada
    pygame.display.update() # pencerenin sürekli olarak açık kalmasını sağlar
