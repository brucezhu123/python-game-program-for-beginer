import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600,500))
pygame.display.set_caption('draw line')

# line position
pos_x = 100
pos_y = 100

pos_x2 = 500
pos_y2 = 400


vel_x = 0.1
vel_y = 0.1
vel_x2 = 1
vel_y2 = 0
while True:
    screen.fill((0,0,200))
    # move the line
    pos_x += vel_x
    pos_y += vel_y
    pos_x2 += vel_x2
    pos_y2 += vel_y2

# limit the circle on the screen
    if pos_x >500 or pos_x <0 or pos_x2 >500 or pos_x2 <0:
        vel_x = -vel_x
        vel_x2 = -vel_x2
    if pos_y >600 or pos_y <0 or pos_y2 >600 or pos_y2 <0:
        vel_y = -vel_y
        vel_y2 = -vel_y2
# draw the line
    color = 100,225,200
    width = 5

    pygame.draw.line(screen,color,(pos_x,pos_y),(pos_x2,pos_y2),width)

    pygame.display.update()
