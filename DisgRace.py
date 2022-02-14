#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from random import randint
from time import sleep

__author__ = "Berdar Yarkın Yücesoy"
__version__ = "0.2"

DISPLAY_WIDTH = 1500
DISPLAY_HEIGHT = 750

car_width = 57
car_height = 150

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
blue2 = (25, 25, 112)
white = (255, 255, 255)
white2 = (238, 238, 238)

score = .0
high_score = .0

pygame.init()

icon = pygame.image.load(r".\images\triangle.png")
greenCar = pygame.image.load(r".\images\green_car.png")

pygame.mixer.init()
pygame.mixer.music.load(r'.\music\Retro_Platforming_-_David_Fesliyan.mp3')
pygame.mixer.music.play(-1)

font1 = pygame.font.Font(r".\fonts\defused.ttf", 80)
font2 = pygame.font.Font(r".\fonts\LucidaTypewriterRegular.ttf", 50)
font3 = pygame.font.Font(r".\fonts\LucidaTypewriterRegular.ttf", 30)

pautext = font1.render("PAUSED", True, black)
pautext_rect = pautext.get_rect(center=(DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2 - 100))

mainDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("DisgRace  v0.1")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()


def car(a, b):  # blits car
    mainDisplay.blit(greenCar, (a, b))


def game_exit():  # exits pygame and python both
    pygame.quit()
    print('\033[93m' + "-" * 30 + "\n          GAME OVER\n" + "-" * 30 + "\nScore: " + str(
        int(score)) + "   High Score:  " + str(int(hc_func(score))) + '\033[0m')
    sleep(3)
    quit()


def game_over():
    go_message()
    game_loop()


def go_message():  # shows game over message including score and high score
    text = font1.render("GAME OVER", True, black)
    text_rect = text.get_rect(center=(DISPLAY_WIDTH / 2, 95))

    scotext = font1.render("SCORE: {}".format(int(score)), True, black)
    start3 = font2.render("Starting in 3", True, black)
    start2 = font2.render("Starting in 2", True, black)
    start1 = font2.render("Starting in 1", True, black)
    start_rect = start1.get_rect(center=(DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2))

    mainDisplay.blit(text, text_rect)
    mainDisplay.blit(scotext, (450, 150))
    mainDisplay.blit(start3, start_rect)
    pygame.display.update()
    pygame.time.delay(1000)
    mainDisplay.fill(white2)
    show_score(score)

    mainDisplay.blit(text, text_rect)
    mainDisplay.blit(scotext, (450, 150))
    mainDisplay.blit(start2, start_rect)
    pygame.display.update()
    pygame.time.delay(1000)
    mainDisplay.fill(white2)
    show_score(score)

    mainDisplay.blit(text, text_rect)
    mainDisplay.blit(scotext, (450, 150))
    mainDisplay.blit(start1, start_rect)
    pygame.display.update()
    pygame.time.delay(1000)


def pause():
    mainDisplay.blit(pautext, pautext_rect)
    pygame.display.update()


def hc_func(new_score):
    global high_score
    if new_score > high_score:
        high_score = new_score
    return high_score


def show_score(sc):
    sc_widget = font3.render("Score: " + str(int(sc)), True, black)
    mainDisplay.blit(sc_widget, (0, 0))


def draw_rect(objlist, speed):  # creates, moves and draws rectangle obstacles
    if len(objlist) < 2:
        objlist.append(Rectangle())
    for objct in objlist:
        objct.y += speed
        pygame.draw.rect(mainDisplay, blue2, (objct.x, objct.y, objct.width, objct.height))
        if objct.y > DISPLAY_HEIGHT:
            objlist.remove(objct)


def coll(o_list, car_x, car_y):  # checks for collusions
    x = car_x
    y = car_y
    for obj in o_list:
        if (y + car_height) > obj.y > (y - obj.height):
            print("y crossover")
            if (x + car_width) > obj.x > (x - obj.width):
                print("x crossover")
                game_over()


class Rectangle:
    def __init__(self):
        self.height = 150
        self.width = randint(200, 400)
        self.x = randint(-self.width, DISPLAY_WIDTH)
        self.y = -150


def game_loop():  # main loop
    rect1 = Rectangle()
    rect1.y = -150
    rect2 = Rectangle()
    rect2.y = -400
    rect3 = Rectangle()
    rect3.y = -650
    rect3 = Rectangle()
    rect3.y = -900

    objs = [rect1, rect2]

    x = DISPLAY_WIDTH / 2
    y = DISPLAY_HEIGHT - car_height - 10

    left_hold = False
    right_hold = False
    running = True
    paused = False

    n = 15
    s = 10
    global score
    score = .0

    while running:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left_hold = True
                if event.key == pygame.K_RIGHT:
                    right_hold = True
                if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    paused = not paused
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left_hold = False
                if event.key == pygame.K_RIGHT:
                    right_hold = False

        if paused:
            pause()
            continue

        if left_hold:
            x -= n
        if right_hold:
            x += n

        if x > DISPLAY_WIDTH - car_width:
            x = DISPLAY_WIDTH - car_width
        elif x < 0:
            x = 0

        n += 0.002
        s += 0.002
        score += s / 60
        hc_func(score)

        mainDisplay.fill(white2)
        show_score(score)
        draw_rect(objs, s)
        car(x, y)
        coll(objs, x, y)

        pygame.display.update()
        clock.tick(60)
    game_exit()


def main():  # Will have features like: quit, restart, change language, fullscreen mode...
    game_loop()
    game_exit()


if __name__ == '__main__':
    main()
