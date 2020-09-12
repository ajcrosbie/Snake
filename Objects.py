import math
import random
import tkinter as tk
from tkinter import messagebox
import pygame
import time


class cube(object):
    rows = 20
    w = 500

    def __init__(self, start, colour, dirnx=1, dirny=0):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.colour = colour

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]
        t = (i*dis+1, j*dis+1, dis-2, dis-2)
        pygame.draw.rect(surface, self.colour,
                         (i*dis+1, j*dis+1, dis-2, dis-2))

        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius, j*dis+8)
            circleMiddle2 = (i*dis + dis - radius*2, j*dis+8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)


class snake(object):

    def __init__(self, colour, pos, player=1):
        self.colour = colour
        self.body = []
        self.head = cube(pos, self.colour)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
        self.player = player
        self.turns = {}

    def move(self, keys):
        # v = False
        # t = 0
        # while not v:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_a] and self.player == 0:
                # print('y')
                self.dirnx = -1
                self.dirny = 0
                # v = True
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            elif keys[pygame.K_d] and self.player == 0:
                self.dirnx = 1
                self.dirny = 0
                # v = True
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            elif keys[pygame.K_s] and self.player == 0:
                self.dirnx = 0
                self.dirny = 1
                # v = True
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            elif keys[pygame.K_w] and self.player == 0:
                self.dirnx = 0
                self.dirny = -1
                # v = True
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            elif keys[pygame.K_LEFT] and self.player == 1:
                self.dirnx = -1
                self.dirny = 0
                # v = True
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            elif keys[pygame.K_RIGHT] and self.player == 1:
                self.dirnx = 1
                self.dirny = 0
                # v = True
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            elif keys[pygame.K_DOWN] and self.player == 1:
                self.dirnx = 0
                self.dirny = 1
                # v = True
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            elif keys[pygame.K_UP] and self.player == 1:
                self.dirnx = 0
                self.dirny = -1
                # v = True
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)

            else:
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1:
                    c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1:
                    c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows-1)
                else:
                    c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        self.head = cube(pos, self.colour)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1, tail.pos[1]), self.colour))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1, tail.pos[1]), self.colour))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0], tail.pos[1]-1), self.colour))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0], tail.pos[1]+1), self.colour))
        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)
