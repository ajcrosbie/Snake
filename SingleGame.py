import math
import random
import tkinter as tk
from tkinter import messagebox
import pygame
import time
import Objects


def GetKeys():
    return pygame.key.get_pressed()


def drawGrid(w, rows, surface):
    SBT = w // rows
    x = 0
    y = 0
    for i in range(rows):
        x = x + SBT
        y = y + SBT

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))

    pass


def redrawWindow(surface, width, rows, s, snack):
    surface.fill((0, 0, 0))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()
    pass


def randomSnack(rows, item):
    positions = item.body
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)

        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue

        else:
            break

    return (x, y)


def message_box(subject, content):
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = Objects.snake((255, 0, 0), (10, 10))
    snack = Objects.cube(randomSnack(rows, s), (0, 255, 0))

    flag = True
    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(60)
        clock.tick(10)
        keys = GetKeys()
        s.move(keys)

        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = Objects.cube(randomSnack(rows, s), colour=(0, 255, 0))
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x+1:])):
                print('Red score: ', len(s.body))
                message_box('you lost', 'play again')
                s.reset((10, 10))
                break
        redrawWindow(win, width, rows, s, snack)

    pass


if __name__ == '__main__':
    main()
