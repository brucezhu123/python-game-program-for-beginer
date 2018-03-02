import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600,500))
pygame.display.set_caption('draw rectangles')

pos_x = 300
pos_y = 200

vel_x = 0.2
vel_y = 0.1

while True:
    screen.fill((0,0,200))

#move the rectangle
    pos_x += vel_x
    pos_y += vel_y

#kepp the rectangle on the screen
    if pos_x >500 or pos_x < 0:
        vel_x = -vel_x
    if pos_y >400 or pos_y < 0:
        vel_y = -vel_y

# draw the rectangle
    color = 255,255,0
    width = 0 #solid fill
    position = pos_x,pos_y,100,100

    pygame.draw.rect(screen,color,position,width)

    pygame.display.update()

