#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
import random
import math
# =======================================================================================
# Функции для работы с векторами
# =======================================================================================

#
# def sub(x, y):
#     """"возвращает разность двух векторов"""
#     return x[0] - y[0], x[1] - y[1]
#
#
# def add(x, y):
#     """возвращает сумму двух векторов"""
#     return x[0] + y[0], x[1] + y[1]
#
#
# def length(x):
#     """возвращает длину вектора"""
#     return math.sqrt(x[0] * x[0] + x[1] * x[1])
#
#
# def mul(v, k):
#     """возвращает произведение вектора на число"""
#     return v[0] * k, v[1] * k
#
#
# def vec(x, y):
#     """возвращает пару координат, определяющих вектор (координаты точки конца вектора),
#     координаты начальной точки вектора совпадают с началом системы координат (0, 0)"""
#     return sub(y, x)
#
#
# # =======================================================================================
# # Функции отрисовки
# # =======================================================================================
#
# def draw_points(points, style="points", width=3, color=(255, 255, 255)):
#     """функция отрисовки точек на экране"""
#     if style == "line":
#         for p_n in range(-1, len(points) - 1):
#             pygame.draw.line(gameDisplay, color,
#                              (int(points[p_n][0]), int(points[p_n][1])),
#                              (int(points[p_n + 1][0]), int(points[p_n + 1][1])), width)
#
#     elif style == "points":
#         for p in points:
#             pygame.draw.circle(gameDisplay, color,
#                                (int(p[0]), int(p[1])), width)
#
#
# def draw_help():
#     """функция отрисовки экрана справки программы"""
#     gameDisplay.fill((50, 50, 50))
#     font1 = pygame.font.SysFont("courier", 24)
#     font2 = pygame.font.SysFont("serif", 24)
#     data = []
#     data.append(["F1", "Show Help"])
#     data.append(["R", "Restart"])
#     data.append(["P", "Pause/Play"])
#     data.append(["Num+", "More points"])
#     data.append(["Num-", "Less points"])
#     data.append(["", ""])
#     data.append([str(steps), "Current points"])
#
#     pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
#         (0, 0), (800, 0), (800, 600), (0, 600)], 5)
#     for i, text in enumerate(data):
#         gameDisplay.blit(font1.render(
#             text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
#         gameDisplay.blit(font2.render(
#             text[1], True, (128, 128, 255)), (200, 100 + 30 * i))
#
#
# # =======================================================================================
# # Функции, отвечающие за расчет сглаживания ломаной
# # =======================================================================================
# def get_point(points, alpha, deg=None):
#     if deg is None:
#         deg = len(points) - 1
#     if deg == 0:
#         return points[0]
#     return add(mul(points[deg], alpha), mul(get_point(points, alpha, deg - 1), 1 - alpha))
#
#
# def get_points(base_points, count):
#     alpha = 1 / count
#     res = []
#     for i in range(count):
#         res.append(get_point(base_points, i * alpha))
#     return res
#
#
# def get_knot(points, count):
#     if len(points) < 3:
#         return []
#     res = []
#     for i in range(-2, len(points) - 2):
#         ptn = []
#         ptn.append(mul(add(points[i], points[i + 1]), 0.5))
#         ptn.append(points[i + 1])
#         ptn.append(mul(add(points[i + 1], points[i + 2]), 0.5))
#
#         res.extend(get_points(ptn, count))
#     return res
#
#
# def set_points(points, speeds):
#     """функция перерасчета координат опорных точек"""
#     for p in range(len(points)):
#         points[p] = add(points[p], speeds[p])
#         if points[p][0] > SCREEN_DIM[0] or points[p][0] < 0:
#             speeds[p] = (- speeds[p][0], speeds[p][1])
#         if points[p][1] > SCREEN_DIM[1] or points[p][1] < 0:
#             speeds[p] = (speeds[p][0], -speeds[p][1])
#


# =======================================================================================
# Основная программа
# =======================================================================================
# if __name__ == "__main__":
#     pygame.init()
#     gameDisplay = pygame.display.set_mode(SCREEN_DIM)
#     pygame.display.set_caption("MyScreenSaver")
#
#     steps = 35
#     working = True
#     points = []
#     speeds = []
#     show_help = False
#     pause = True
#
#     hue = 0
#     color = pygame.Color(0)
#
#     while working:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 working = False
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     working = False
#                 if event.key == pygame.K_r:
#                     points = []
#                     speeds = []
#                 if event.key == pygame.K_p:
#                     pause = not pause
#                 if event.key == pygame.K_KP_PLUS:
#                     steps += 1
#                 if event.key == pygame.K_F1:
#                     show_help = not show_help
#                 if event.key == pygame.K_KP_MINUS:
#                     steps -= 1 if steps > 1 else 0
#
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 points.append(event.pos)
#                 speeds.append((random.random() * 2, random.random() * 2))
#
#         gameDisplay.fill((0, 0, 0))
#         hue = (hue + 1) % 360
#         color.hsla = (hue, 100, 50, 100)
#         draw_points(points)
#         draw_points(get_knot(points, steps), "line", 3, color)
#         if not pause:
#             set_points(points, speeds)
#         if show_help:
#             draw_help()
#
#         pygame.display.flip()
#
#     pygame.display.quit()
#     pygame.quit()
#     exit(0)
#
# =======================================================================================
# ООП РЕФАКТОРИНГ
# =======================================================================================
# =======================================================================================
# Реализовать класс 2-мерных векторов Vec2d [1]. В классе следует определить методы для основных математических операций,
# необходимых для работы с вектором: Vec2d.__add__ (сумма), Vec2d.__sub__ (разность), Vec2d.__mul__ (произведение на число).
# А также добавить возможность вычислять длину вектора с использованием функции len(a) и метод int_pair,
# который возвращает кортеж из двух целых чисел (текущие координаты вектора).
# =======================================================================================

SCREEN_DIM = (800, 600)

class Vec2d():#DONE

    def __init__(self, point =  None):
        if point is None:
             self.point = (0,0)
        else:
            self.point = point

    def __add__ (self,other):
        """возвращает сумму двух векторов"""
        return Vec2d((self.point[0] + other.point[0], self.point[1] + other.point[1]))

    def __sub__ (self,other):
        """"возвращает разность двух векторов"""
        return Vec2d((self.point[0] - other.point[0], self.point[1] - other.point[1]))

    def __mul__ (self, k):
        """возвращает произведение вектора на число"""
        return Vec2d((self.point[0] * k, self.point[1] * k))

    def len(self):
        """возвращает длину вектора"""
        return math.sqrt(self.point[0] * self.point[0] + self.point[1] * self.point[1])

    def int_pair(self):
        """возвращает пару координат, определяющих вектор (координаты точки конца вектора),
        координаты начальной точки вектора совпадают с началом системы координат (0, 0)"""
        return self.point[0], self.point[1]

    def __getitem__(self, key):
        return self.point[key]

    def __setitem__(self, key, value):
        self.point[key] = value

# =======================================================================================
# Реализовать класс замкнутых ломаных Polyline с методами отвечающими за добавление в ломаную точки (Vec2d) c её скоростью,
# пересчёт координат точек (set_points) и отрисовку ломаной (draw_points).
# Арифметические действия с векторами должны быть реализованы с помощью операторов, а не через вызовы соответствующих методов.
# =======================================================================================

class Polyline():

    def __init__(self, points,speed):#DONE
        self.points = [Vec2d(x) for x in points]
        self.speed =  [Vec2d(x) for x in speed]

    def set_points(self):#DONE
        """функция перерасчета координат опорных точек"""
        for p in range(len(points)):
            points[p] = self.points[p]+self.speed[p]
            if points[p][0] > SCREEN_DIM[0] or points[p][0] < 0:
                speeds[p] = Vec2d((- self.speeds[p][0], self.speeds[p][1]))
            if points[p][1] > SCREEN_DIM[1] or points[p][1] < 0:
                speeds[p] = Vec2d((self.speeds[p][0], -self.speeds[p][1]))

        self.points = points
        self.speed = speed

    def draw_points(self,points =[], style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""

        if(len(points)==0):
            points= self.points
        if style == "line":

            for p_n in range(-1, len(points) - 1):
                pygame.draw.line(gameDisplay, color,
                                 (int(points[p_n][0]), int(points[p_n][1])),
                                 (int(points[p_n + 1][0]), int(points[p_n + 1][1])), width)
        elif style == "points":
            for p in points:
                pygame.draw.circle(gameDisplay, color,
                                   (int(p[0]), int(p[1])), width)

    def draw_help(self):
        """функция отрисовки экрана справки программы"""
        gameDisplay.fill((50, 50, 50))
        font1 = pygame.font.SysFont("courier", 24)
        font2 = pygame.font.SysFont("serif", 24)
        data = []
        data.append(["F1", "Show Help"])
        data.append(["R", "Restart"])
        data.append(["P", "Pause/Play"])
        data.append(["Num+", "More points"])
        data.append(["Num-", "Less points"])
        data.append(["", ""])
        data.append([str(steps), "Current points"])

        pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
            (0, 0), (800, 0), (800, 600), (0, 600)], 5)
        for i, text in enumerate(data):
            gameDisplay.blit(font1.render(
                text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
            gameDisplay.blit(font2.render(
                text[1], True, (128, 128, 255)), (200, 100 + 30 * i))

# =======================================================================================
# Реализовать класс Knot (наследник класса Polyline),
# в котором добавление и пересчёт координат инициируют вызов функции get_knot для расчёта точек кривой по добавляемым «опорным» точкам [2].
# =======================================================================================

class Knot(Polyline):

    def get_knot(self,count):
        points = self.points
        if len(points) < 3:
            return []
        res = []
        for i in range(-2, len(points) - 2):
            ptn = []
            ptn.append(((points[i]+points[i + 1])*0.5).int_pair())
            ptn.append((points[i + 1]).int_pair())
            ptn.append(((points[i + 1]+points[i + 2])*0.5).int_pair())
            return res
            res.extend(self.get_points(ptn, count))

    def get_points(self,base_points, count): #WARN
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(self.get_point(base_points, i * alpha))
        return res

    def get_point(self,points, alpha, deg=None): #WARN
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return ((points[deg]*alpha) + (self.get_point(points, alpha, deg - 1) * (1 - alpha)))

#=======================================================================================
#Основная программа
#=======================================================================================

if __name__ == "__main__":

    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    points = []
    speeds = []
    show_help = False
    pause = True
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
                    points = []
                    speeds = []
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                points.append(event.pos)
                speeds.append((random.random() * 2, random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)

        Knot1 = Knot(points,speeds)
        Knot1.draw_points()
        Knot1.draw_points(Knot1.get_knot(steps), "line", 3, color)

        # def __init__(self, points,speed):#DONE
        #     self.points = [Vec2d(x) for x in points]
        #     self.speed =  [Vec2d(x) for x in speed]
        #
        # def set_points(self):#DONE
        #     points = self.points
        #     speed  = self.speed
        #     """функция перерасчета координат опорных точек"""
        #     for p in range(len(points)):
        #         points[p] = points[p]+speeds[p]
        #         if points[p][0] > SCREEN_DIM[0] or points[p][0] < 0:
        #             speeds[p] = Vec2d((- speeds[p][0], speeds[p][1]))
        #         if points[p][1] > SCREEN_DIM[1] or points[p][1] < 0:
        #             speeds[p] = Vec2d((speeds[p][0], -speeds[p][1]))
        #
        #     self.points = points
        #     self.speed = speed


        if not pause:
            Knot1.set_points()
        if show_help:
            Knot1.draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
