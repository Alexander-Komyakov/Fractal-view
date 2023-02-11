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
		turtle.set_angel(60)
		turtle.set_distance(2)
		rules.add_axioma("F--F--F--F")
		rules.add_rule("F", "F+F--F+F")
		for i in range(0, 7):
			rules.smash_expression()
		rules.call_rule()
	elif frac == 2:
		turtle.set_angel(90)
		turtle.set_distance(2)
		rules.add_axioma("F+F+F+F+F+F+F+F")
		rules.add_rule("F", "F+F-F-F+F")
		for i in range(0, 8):
			rules.smash_expression()
		rules.call_rule()
	elif frac == 3:
		turtle.set_angel(60)
		turtle.set_distance(100)
		rules.add_axioma("F")
		rules.add_rule("F", "F-F-F+F+++F+F+F+F-F-F")
		for i in range(0, 5):
			rules.smash_expression()
		rules.call_rule()
	elif frac == 4:
		turtle.set_angel(90)
		turtle.set_distance(10)
		rules.add_symbol("X", print)
		rules.add_symbol("Y", print)
		rules.add_axioma("FX")
		rules.add_rule("X", "X-YF-")
		rules.add_rule("Y", "+FX+Y")
		for i in range(0, 16):
			rules.smash_expression()
		rules.call_rule()
	elif frac == 5:
		turtle.set_distance(2)
		turtle.set_angel(90)
		rules.add_axioma("F")
		rules.add_rule("F", "F+F-F-F+F")
		for i in range(0, 8):
			rules.smash_expression()
		rules.call_rule()
	elif frac == 6:
		turtle.set_distance(6)
		turtle.set_angel(60)
		rules.add_axioma("FXF--FF-FF")
		rules.add_symbol("X", print)
		rules.add_rule("F", "FF")
		rules.add_rule("X", "--FXF++FXF++FXF--")
		for i in range(0, 7):
			rules.smash_expression()
		rules.call_rule()
	elif frac == 7:
		turtle.set_distance(6)
		turtle.set_angel(90)
		rules.add_axioma("F+F+F+F")
		rules.add_rule("F", "-F+F-F-F+F+FF-F+F+FF+F-F-FF+FF-FF+F+F-FF-F-F+FF-F-F+F+F-F+")
		for i in range(0, 3):
			rules.smash_expression()
		rules.call_rule()
	elif frac == 8:
		turtle.set_distance(6)
		turtle.set_angel(60)
		rules.add_axioma("FX")
		rules.add_symbol("X", print)
		rules.add_symbol("Y", print)
		rules.add_rule("X", "X+YF++YF-FX--FXFX-YF+")
		rules.add_rule("Y", "-FX+YFYF++YF+FX--FX-Y")
		for i in range(0, 6):
			rules.smash_expression()
		rules.call_rule()
	elif frac == 9:
		turtle.set_distance(10)
		turtle.set_angel(45)
		rules.add_axioma("F")
		rules.add_rule("F", "-F++F-")
		for i in range(0, 16):
			rules.smash_expression()
		rules.call_rule()
	elif frac == 10:
		turtle.set_distance(15)
		turtle.set_angel(25)
		rules.add_symbol("X", print)
		rules.add_symbol("[", turtle.add_stack)
		rules.add_symbol("]", turtle.pop_stack)
		rules.add_axioma("X")
		rules.add_rule("X", "FFF-[[X]+X]+F[+FX]-X")
		rules.add_rule("F", "FF")
		for i in range(0, 6):
			rules.smash_expression()
		rules.call_rule()
	elif frac == 11:
		turtle.set_distance(60)
		turtle.set_angel(20)
		for i in range(0, 7):
			turtle.left()
		rules.add_symbol("[", turtle.add_stack)
		rules.add_symbol("]", turtle.pop_stack)
		rules.add_axioma("F")
		rules.add_rule("F", "F[+F]F[-F][F]")
		for i in range(0, 5):
			rules.smash_expression()
		rules.call_rule()
	elif frac == 12:
		turtle.set_distance(20)
		turtle.set_angel(22.5)
		for i in range(0, 4):
			turtle.left()
		rules.add_symbol("[", turtle.add_stack)
		rules.add_symbol("]", turtle.pop_stack)
		rules.add_axioma("F")
		rules.add_rule("F", "FF-[-F+F+F]+[+F-F-F]")
		for i in range(0, 5):
			rules.smash_expression()
		rules.call_rule()

	elif frac == 13:
		turtle.set_distance(20)
		turtle.set_angel(20)
		rules.add_symbol("[", turtle.add_stack)
		rules.add_symbol("]", turtle.pop_stack)
		rules.add_axioma("F")
		rules.add_rule("F", "F[+F]F[-F][F]")
		for i in range(0, 5):
			rules.smash_expression()
		rules.call_rule()
	elif frac == 14:
		turtle.set_distance(2)
		turtle.set_angel(25.7)
		turtle.left()
		turtle.left()
		turtle.left()
		rules.add_symbol("[", turtle.add_stack)
		rules.add_symbol("]", turtle.pop_stack)
		rules.add_symbol("X", turtle.direct)
		rules.add_axioma("X")
		rules.add_rule("X", "F[-X][+X]FX")
		rules.add_rule("F", "FF")
		for i in range(0, 10):
			rules.smash_expression()
		rules.call_rule()
	elif frac == 15:
		turtle.set_distance(2)
		turtle.set_angel(22.5)
		rules.add_symbol("[", turtle.add_stack)
		rules.add_symbol("]", turtle.pop_stack)
		rules.add_axioma("[F]+[F]+[F]+[F]+[F]+[F]")
		rules.add_rule("F", "F[++F][--F]FF[+F][-F]FF")
		for i in range(0, 4):
			rules.smash_expression()
		rules.call_rule()
		rules.call_rule()
		rules.call_rule()
	else:
		turtle.set_distance(10)
		turtle.set_angel(45)
		rules.add_axioma("F")
		rules.add_rule("F", "-F++F-")
		for i in range(0, 16):
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

pygame.draw.aalines(main_surface, YELLOW, False, turtle.get_coords(), 4)
pygame.image.save(main_surface, "fractal.png")
main_surface_size = (2000, 2000)
surface_pos = (-main_surface_size[0]/2+WIDTH/2, -main_surface_size[1]/2+HEIGHT/2)

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
	pygame.draw.aalines(main_surface, YELLOW, False, turtle.get_coords(), 4)
	pygame.display.update()
	screen.fill(YELLOW)
	screen.blit(pygame.transform.smoothscale(main_surface, main_surface_size), surface_pos)
