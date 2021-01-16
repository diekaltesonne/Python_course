
from typing import Any, Union

import pygame
import math
import random

SCREEN_DIM = (800, 600)
SCREEN_DIAG = (SCREEN_DIM[0] ** 2 + SCREEN_DIM[1] ** 2) ** 0.5


class Vec2d:
    def __init__(self, x, y):
        self.__x = x

    def __add__(self, other):
        return Vec2d(self.__x + other.int_pair()[0], self.__y + other.int_pair()[1])
        self.__y = y

    def __sub__(self, other):
        return Vec2d(self.__x - other.int_pair()[0], self.__y - other.int_pair()[1])

    def __mul__(self, other):
        if isinstance(other, Vec2d):
            return self.__x*other.int_pair()[1] + self.__y*other.int_pair()[0]
        return Vec2d(self.__x * other, self.__y * other)

    def len(self):
        return math.sqrt(self.__x * self.__x + self.__y * self.__y)

    def int_pair(self):
        return self.__x, self.__y


class Polyline:
    def __init__(self):
        self.points = []
        self.knots = []
        self.speeds = []

    def set_points(self):
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p].int_pair()[0] > SCREEN_DIM[0] or self.points[p].int_pair()[0] < 0:
                self.speeds[p] = Vec2d(- self.speeds[p].int_pair()[0], self.speeds[p].int_pair()[1])
            if self.points[p].int_pair()[1] > SCREEN_DIM[1] or self.points[p].int_pair()[1] < 0:
                self.speeds[p] = Vec2d(self.speeds[p].int_pair()[0], -self.speeds[p].int_pair()[1])
        self.knots = self.get_knot()

    def draw_points(self, gameDisplay, style="points", width=3, color=(255, 255, 255)):
        if style == "line":
            for p in range(-1, len(self.knots) - 1):
                pygame.draw.line(gameDisplay, color,
                                 (int(self.knots[p].int_pair()[0]), int(self.knots[p].int_pair()[1])),
                                 (int(self.knots[p + 1].int_pair()[0]), int(self.knots[p + 1].int_pair()[1])), width)

        elif style == "points":
            for p in self.points:
                pygame.draw.circle(gameDisplay, color,
                                   (int(p.int_pair()[0]), int(p.int_pair()[1])), width)


class Knot(Polyline):

    search_range = 0.05*SCREEN_DIAG
    count = 35

    def __init__(self):
        super().__init__()

    def add_point(self, pos):
        self.points.append(Vec2d(pos[0], pos[1]))
        self.speeds.append(Vec2d(random.random() * 2, random.random() * 2))
        self.knots = self.get_knot()

    def get_knot(self):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = [(self.points[i] + self.points[i + 1]) * 0.5, self.points[i + 1],
                   (self.points[i + 1] + self.points[i + 2]) * 0.5]
            res.extend(self.get_points(ptn))
            return res

    def get_points(self, base_points):
        alpha = 1 / self.count
        res = []
        for i in range(self.count):
            res.append(self.get_point(base_points, i * alpha))
        return res

    def get_point(self, base_points, alpha, deg=None):
        if deg is None:
            deg = len(base_points) - 1
        if deg == 0:
            return base_points[0]
        return base_points[deg] * alpha + self.get_point(base_points, alpha, deg - 1) * (1 - alpha)

    def change_speed(self, mul):
        for i in range(len(self.speeds)):
            self.speeds[i] *= mul

    def delete_point(self, point):
        point_ind = self.points.index(point)
        self.speeds.pop(point_ind)
        self.points.remove(point)
        self.knots = self.get_knot()

    def nearest_point(self, pos):
        min_len = self.search_range
        min_len_point = None
        for p in self.points:
            current_len = (p - pos).len()
            if current_len < min_len:
                min_len_point = self.points[self.points.index(p)]
                min_len = current_len
        return min_len, min_len_point

    @classmethod
    def draw_help(cls):
        gameDisplay.fill((50, 50, 50))
        font1 = pygame.font.SysFont("courier", 24)
        font2 = pygame.font.SysFont("serif", 24)
        data = []
        data.append(["F1", "Show Help"])
        data.append(["R", "Restart"])
        data.append(["P", "Pause/Play"])
        data.append(["Num+", "More points"])
        data.append(["Num-", "Less points"])
        data.append(["F", "More speed"])
        data.append(["L", "Less speed"])
        data.append(["N", "New line"])
        data.append(["LB", "Add point"])
        data.append(["RB", "Delete point"])
        data.append(["", ""])
        data.append([str(cls.count), "Current points"])

        pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
            (0, 0), (800, 0), (800, 600), (0, 600)], 5)
        for i, text in enumerate(data):
            gameDisplay.blit(font1.render(
                text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
            gameDisplay.blit(font2.render(
                text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    working = True
    show_help = False
    pause = False
    knots_list = [Knot()]
    current_line = 0

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    knots_list = [Knot()]
                    current_line = 0
                if event.key == pygame.K_n:
                    knots_list.append(Knot())
                    current_line = len(knots_list) - 1
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_f:
                    for knot in knots_list:
                        knot.change_speed(1.5)
                if event.key == pygame.K_l:
                    for knot in knots_list:
                        knot.change_speed(0.67)
                if event.key == pygame.K_KP_PLUS:
                    Knot.count += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    Knot.count -= 1 if Knot.count > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    knots_list[current_line].add_point(event.pos)
                elif event.button == 3:
                    position = Vec2d(event.pos[0], event.pos[1])
                    min_len_point_in_knot = None
                    knot_num = 0
                    min_len_total = Knot.search_range
                    nearest_point = None
                    for knot in knots_list:
                        min_len_in_knot: float
                        min_len_in_knot, min_len_point_in_knot = knot.nearest_point(position)
                        if min_len_point_in_knot:
                            if min_len_in_knot < min_len_total:
                                min_len_total = min_len_in_knot
                                nearest_point = min_len_point_in_knot
                                knot_num = knots_list.index(knot)
                    if nearest_point:
                        knots_list[knot_num].delete_point(nearest_point)
                        current_line = knot_num

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        for knot in knots_list:
            knot.draw_points(gameDisplay)
            knot.draw_points(gameDisplay, "line", 3, color)
        if not pause:
            for knot in knots_list:
                knot.set_points()
        if show_help:
            Knot.draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
