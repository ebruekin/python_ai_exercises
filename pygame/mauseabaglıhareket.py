# -*- coding: utf-8 -*-

import pygame , sys

pygame.init() # ben pygame modulündeki fonksiytonları kullanacagım onları bana getir

pencereBoyutu = (800,500) # pencerenin pixel olarak boyutlarını verdim

ball = pygame.image.load("ball.png")
pygame.mouse.set_visible(0)

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
    
    mauseX,mauseY=pygame.mouse.get_pos()
    # sınırlar içerisinde hareket etmesini sağladık
    if mauseX +ball.get_size()[0] > 800:
        mauseX = mauseX - ball.get_size()[0]
        
    if mauseY+ball.get_size()[1] > 500:
        mauseY = mauseY - ball.get_size()[1]
    pencere.blit(ball,(mauseX,mauseY))
    pygame.display.update() # pencerenin sürekli olarak açık kalmasını sağlar
