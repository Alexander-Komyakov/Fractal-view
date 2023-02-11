#!/usr/bin/python3

import pygame
import sys, math, time
from random import randrange
from random import choice
from fractal import Fractal
from turtle import Turtle

def billet_fractal(frac: int):
	rules.add_symbol("F", turtle.direct)
	rules.add_symbol("+", turtle.right)
	rules.add_symbol("-", turtle.left)
	if frac == 1:
		turtle.angel = 60
		rules.add_symbol("Y", print)
		rules.add_symbol("X", print)
		rules.add_rule("X", "YF+XF+Y")
		rules.add_rule("Y", "XF-YF-X")
		for i in range(0, 6):
			rules.smash_expression()
		rules.call_rule()
		rules.call_rule()
		rules.call_rule()
		rules.call_rule()
	elif frac == 2:
		turtle.angel = 90
		rules.add_rule("F", "FF+F-F+F+FF")
		for i in range(0, 5):
			rules.smash_expression()
		rules.call_rule()
	elif frac == 3:
		turtle.angel = 90
		rules.add_symbol("X", print)
		rules.add_rule("X", "XF-F+F-XF+F+XF-F+F-X")
		rules.add_rule("F", "F+XF+F+XF")
		for i in range(0, 5):
			rules.smash_expression()
		rules.call_rule()
	elif frac == 4:
		turtle.angel = 90
		rules.add_rule("F", "F+F-F-F-F+F+F+F-F")
		for i in range(0, 5):
			rules.smash_expression()
		rules.call_rule()
	elif frac == 5:
		turtle.angel = 90
		rules.add_symbol("X", print)
		rules.add_rule("F", "XF-F+F-XF+F+XF-F+F-X")
		for i in range(0, 5):
			rules.smash_expression()
		rules.call_rule()
	elif frac == 6:
		turtle.angel = 90
		rules.add_symbol("X", print)
		rules.add_symbol("Y", print)
		rules.add_rule("X", "XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF-")
		rules.add_rule("Y", "+FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF-FX+FX+YFY")
		for i in range(0, 3):
			rules.smash_expression()
		rules.call_rule()
	elif frac == 7:
		turtle.angel = 90
		rules.add_symbol("L", print)
		rules.add_symbol("R", print)
		rules.add_rule("L", "+RF-LFL-FR+")
		rules.add_rule("R", "-LF+RFR+FL-")
		for i in range(0, 9):
			rules.smash_expression()
		rules.call_rule()


pygame.init()

WIDTH = 1920
HEIGHT = 1080

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (166, 194, 95)

main_surface_size = (8000, 8000)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
main_surface = pygame.Surface(main_surface_size)

center = (WIDTH/2, HEIGHT/2)
turtle = Turtle(main_surface_size[0]/2, main_surface_size[1]/2, 0)

rules = Fractal()
if len(sys.argv) > 1:
	billet_fractal(int(sys.argv[1]))
else: 
	billet_fractal(1)
surface_pos = (-main_surface_size[0]/2, -main_surface_size[1]/2)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 4:
				if main_surface_size[0] < 20000:
					main_surface_size = (main_surface_size[0]+600, main_surface_size[1]+600)
					surface_pos = (surface_pos[0]-300, surface_pos[1]-300)
				main_surface.fill(WHITE)
			if event.button == 5:
				if main_surface_size[0] > 300:
					main_surface_size = (main_surface_size[0]-600, main_surface_size[1]-600)
					surface_pos = (surface_pos[0]+300, surface_pos[1]+300)
				main_surface.fill(WHITE)
			if event.button == 1:
				save_mouse_pos = pygame.mouse.get_pos()
		if event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				current_mouse_pos = pygame.mouse.get_pos()
				surface_pos = (surface_pos[0] + (current_mouse_pos[0] - save_mouse_pos[0]),
								surface_pos[1] + (current_mouse_pos[1] - save_mouse_pos[1]))
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				turtle.direct(400)
			elif event.key == pygame.K_a:
				turtle.left()
			elif event.key == pygame.K_d:
				turtle.right()
			elif event.key == pygame.K_LSHIFT:
				rules.call_rule()

	main_surface.fill(BLACK)
	pygame.draw.lines(main_surface, WHITE, False, turtle.get_coords(), 1)
	pygame.display.update()
	screen.fill(YELLOW)
	screen.blit(pygame.transform.smoothscale(main_surface, main_surface_size), surface_pos)
