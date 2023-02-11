#!/usr/bin/python3

import pygame
import sys, math, time
from random import randrange

pygame.init()


screen = pygame.display.set_mode((800, 600))
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

old_coord = [400, 400]
new_coord = (old_coord[0]+randrange(-10, 11), old_coord[1]+randrange(-10, 11))

lines = []
lines.append((old_coord, new_coord))
old_coord = new_coord
back_numb = 0
screen.fill(WHITE)
while True:
	back_numb += 1
	if back_numb == 500:
		back_numb = 0
		old_coord = (400, 400)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	for i in lines:
		pygame.draw.line(screen, (0, 0, randrange(0, 255)), i[0], i[1], 4)
	new_coord = (old_coord[0]+randrange(-20, 21), old_coord[1]-randrange(-20, 21))
	lines.append((old_coord, new_coord))
	old_coord = new_coord
	pygame.display.flip()
	screen.fill(WHITE)
	#time.sleep(0.005)
	time.sleep(0.5)
