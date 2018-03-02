import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600,500))
pygame.display.set_caption('draw circle')

# circle position
pos_x = 200
pos_y = 300

vel_x = 1
vel_y = 2

while True:
    screen.fill((0,0,200))

# move the circle
    pos_x += vel_x
    pos_y += vel_y

# limit the circle on the screen
    if pos_x >500 or pos_x <0:
        vel_x = -vel_x
    if pos_y >400 or pos_y <0:
        vel_y = -vel_y

#draw a circle
    color = 255,255,0
    position = pos_x,pos_y
    radius = 20
    width = 5

    pygame.draw.circle(screen,color,position,radius,width)

    pygame.display.update()
