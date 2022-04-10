#!/usr/bin/env python


#draw1.py
#A working examples of all the pygame.draw functions

import os, sys, pygame
from pygame.locals import *
from math import pi

WHITE = 255,255,255
GREEN = 0,255,0
BLACK = 0,0,0
BLUE  = 0,0,255
RED   = 255,0,0

#function to convert radians to degrees
def deg(rad):
    return rad * pi/180

size = width, height = 340, 410
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pygame.draw functions ~ examples")
pygame.init()

#draw a few rectangles
rect1 = pygame.draw.rect(screen, WHITE, (20,20,60,60),0) #filled = 0
rect2 = pygame.draw.rect(screen, WHITE, (100,20,60,60),3) # not filled

#draw a few polygons
points = []
points.append((20,100))
points.append((80,100))
points.append((80,160))
poly1 = pygame.draw.polygon(screen, WHITE, points, 0) #filled
points=[]
points.append((100,100))
points.append((160,100))
points.append((160,160))
points.append((100,160))
poly2 = pygame.draw.polygon(screen, WHITE, points, 3) #not filled

#draw a few circles
circ1 = pygame.draw.circle(screen, WHITE, (50,180), 30, 0) #filled
circ2 = pygame.draw.circle(screen, WHITE, (130,180), 30, 3) #filled

#draw an ellipse
ellipse1 = pygame.draw.ellipse(screen, WHITE, (20,220,140,60), 3)

#draw a few arcs
arc1 = pygame.draw.arc(screen, WHITE, (20,290,60,60),deg(0), deg(90), 3)
arc2 = pygame.draw.arc(screen, WHITE, (100,290,60,60),deg(90), deg(270), 3)

#draw a few lines
for n in range(5):
    pygame.draw.line(screen, WHITE, (20,350+(10*n)), (100,350), 2)
    pygame.draw.line(screen, GREEN, (20,390), (100,350+(10*n)), 2)

#draw a few anti aliased lines
for n in range(5):
    pygame.draw.aaline(screen, WHITE, (120,390), (250,350+(10*n)), 1)

#draw a few aaline sequences
CLOSED = 1
OPEN = 0
points=[]
points.append((180,100))
points.append((240,100))
points.append((240,160))
points.append((180,160))
pygame.draw.aalines(screen, GREEN, OPEN, points, 1)    
points.append((260,100))
points.append((320,100))
points.append((320,160))
points.append((260,160))
pygame.draw.aalines(screen, GREEN, CLOSED, points, 1)    

#now we draw onto a new surface, and blit the result to the screen

#create myimage and set transparancy to top left pixel
newsurface = pygame.Surface((80,80))
myimage = newsurface.convert()
ckey = myimage.get_at((0,0))
myimage.set_colorkey(ckey, RLEACCEL)

#draw onto myimage
myimage.fill(BLACK)
pygame.draw.rect(myimage, BLUE, (5,5,70,70),0)   # A BLUE block
pygame.draw.rect(myimage, RED, (20,20,40,40),0)  # A RED block
pygame.draw.line(myimage, WHITE, (10,70), (70,10), 5) #white line
pygame.draw.line(myimage, WHITE, (10,10), (70,70), 5) #white line

#blit 2 copies of myimage to screen
screen.blit(myimage,(175,10))
screen.blit(myimage,(250,10))

#Lets create some text. We could use a loop, but lets keep it simple
font = pygame.font.Font(None, 35)
fontimg1 = font.render("pygame.draw",1,WHITE)
fontimg2 = font.render("functions",1,WHITE)
fontimg3 = font.render("working",1,GREEN)
fontimg4 = font.render("examples",1,GREEN)
screen.blit(fontimg1, (170,196))
screen.blit(fontimg2, (185,230))
screen.blit(fontimg3, (190,260))
screen.blit(fontimg4, (185,290))
                  
while 1:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            sys.exit(0)
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.display.quit()
            sys.exit(0)
    

    pygame.display.update() 
    pygame.time.delay(500)
           
