import pygame
import random
import math



class Vec2d:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, vect):
        return Vec2d(self.x-vect.x, self.y-vect.y)

    def __add__(self, vect):
        return Vec2d(self.x+vect.x, self.y+vect.y)

    def __mul__(self, alpha):
        return Vec2d(self.x*alpha, self.y*alpha)

    def int_pair(self):
        return (int(self.x), int(self.y))

    def __len__(self):
        return math.sqrt(self.x**2 + self.y**2)


    def len(self):                  # specially to delete point
        return self.__len__()

class Polyline:

    def __init__(self):
        self.points = []
        self.speeds = []

    def add_point(self, addpoint):
        self.points.append(addpoint)

    def add_speed(self, addspeed):
        self.speeds.append(addspeed)

    def set_points(self):
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]

            window_size = Game.get_size()
            if self.points[p].x > window_size[0] or self.points[p].x < 0:
                # without it there is will be bug when we increase speed
                if self.points[p].x > window_size[0]:
                    self.points[p].x = window_size[0]
                else:
                    self.points[p].x = 0
                self.speeds[p] = Vec2d(- self.speeds[p].x, self.speeds[p].y)
            if self.points[p].y > window_size[1] or self.points[p].y < 0:
                # without it there is will be bug when we increase speed
                if self.points[p].y > window_size[1]:
                    self.points[p].y = window_size[1]
                else:
                    self.points[p].y = 0
                self.speeds[p] = Vec2d(self.speeds[p].x, -self.speeds[p].y)


    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        if style == "points":
            for p in self.points:
                pygame.draw.circle(gameDisplay, color, p.int_pair(), width)

    def delete_point(self, point):
        dist = None
        n = 0
        for i in range(len(self.points)):
            if dist == None:
                dist = (point-self.points[i]).len()
                continue
            if (point-self.points[i]).len() < dist:
                n = i
                dist = (point-self.points[i]).len()
        if dist != None:
            self.points.remove(self.points[n])
            self.speeds.remove(self.speeds[n])


class Knot(Polyline):

    def __init__(self, *args, **kwargs):
        super(Knot, self).__init__(*args, **kwargs)
        self.new_points = []

    def get_point(self, base_points, alpha, deg=None):
        if deg is None:
            deg = len(base_points) - 1
        if deg == 0:
            return base_points[0]

        return (base_points[deg]*alpha) + self.get_point(base_points, alpha, deg - 1)*(1 - alpha)


    def get_points(self, base_points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(self.get_point(base_points, i * alpha))
        return res

    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        if style == "line":
            for p_n in range(-1, len(self.new_points) - 1):
                pygame.draw.line(gameDisplay, color,
                                self.new_points[p_n].int_pair(),
                                self.new_points[p_n+1].int_pair(), width)
        else:
            super(Knot, self).draw_points(style, width, color)

    def get_knot(self, count):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = []
            ptn.append((self.points[i]+self.points[i + 1]) * 0.5)
            ptn.append(self.points[i + 1])
            ptn.append((self.points[i + 1]+self.points[i + 2]) * 0.5)

            res.extend(self.get_points(ptn, count))
        self.new_points = res

    def reboot(self):
        self.speeds = []
        self.points = []
        self.new_points = []

    def increase_speed(self):
        for i in range(len(self.speeds)):
            self.speeds[i] *= 2

    def decrease_speed(self):
        for i in range(len(self.speeds)):
            self.speeds[i] *= 0.5

class Game:

    @staticmethod
    def get_size():
        return (800, 600)

    def __init__(self):
        self.working = False
        self.pause = False
        self.show_help = False
        self.delete = True

    def _on_pause(self):
        self.pause = True

    def _off_pause(self):
        self.pause = False

    def change_pause(self):
        self.pause = not self.pause

    def _on_help(self):
        self.show_help = True

    def _off_help(self):
        self.show_help = False

    def change_help(self):
        self.show_help = not self.show_help

    def change_delete(self):
        self.delete = not self.delete

    def run(self):
        self.steps = 35
        self.working = True
        self._off_help()
        self._on_pause()

        self.figures = [Knot()]             # our figures
        self._scheduler = self.figures[0]   # current figure
        self._running_cycle()

        pygame.display.quit()
        pygame.quit()


    def _running_cycle(self):
        hue = 0
        color = pygame.Color(0)
        while self.working:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.working = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.working = False
                    if event.key == pygame.K_r:     # restart
                        for i in range(len(self.figures)):
                            self.figures[i].reboot()
                        self.figures = [Knot()]             # our figures
                        self._scheduler = self.figures[0]
                        self._on_pause()
                    if event.key == pygame.K_p:     # pause
                        self.change_pause()
                    if event.key == pygame.K_y:     # increase speed
                        self._scheduler.increase_speed()
                    if event.key == pygame.K_n:     # decrease speed
                        self._scheduler.decrease_speed()
                    if event.key == pygame.K_a:     # add new figure
                        self.figures.append(Knot())
                        self._scheduler = self.figures[len(self.figures)-1]
                        self.pause = True
                    if event.key == pygame.K_d:     # delete closer point
                        self.change_delete()
                        self.pause = True
                    if event.key == pygame.K_c:
                        self.steps += 1
                    if event.key == pygame.K_F1:
                        self.change_help()
                    if event.key == pygame.K_v:
                        self.steps -= 1 if self.steps > 1 else 0

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.delete == False:
                        self._scheduler.add_point(Vec2d(event.pos[0], event.pos[1]))
                        self._scheduler.add_speed(Vec2d(random.random() * 2, random.random() * 2))
                    else:
                        self._scheduler.delete_point(Vec2d(event.pos[0], event.pos[1]))
                        self.change_delete()
                        # without it we will see the old figure on backgroud (it's bug)
                        if len(self._scheduler.points) < 3:
                            self._scheduler.new_points = []

            gameDisplay.fill((0, 0, 0))
            hue = (hue + 1) % 360
            color.hsla = (hue, 100, 50, 100)
            for i in range(len(self.figures)):
                self.figures[i].draw_points()
                self.figures[i].get_knot(self.steps)
                self.figures[i].draw_points("line", 3, color)

                if not self.pause:
                    self.figures[i].set_points()

            if self.show_help:
                self.draw_help()

            pygame.display.flip()

    def draw_help(self):
        gameDisplay.fill((50, 50, 50))
        font1 = pygame.font.SysFont("courier", 24)
        font2 = pygame.font.SysFont("serif", 24)
        data = []
        data.append(["F1", "Show Help"])
        data.append(["R", "Restart"])
        data.append(["P", "Pause/Play"])
        data.append(["C", "More points"])
        data.append(["V", "Less points"])
        data.append(["Y", "Increase speed"])
        data.append(["N", "Decrease speed"])
        data.append(["A", "Add new figure"])
        data.append(["D", "Delete closer point"])
        data.append(["", ""])
        data.append([str(self.steps), "Current points"])

        pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
            (0, 0), (800, 0), (800, 600), (0, 600)], 5)
        for i, text in enumerate(data):
            gameDisplay.blit(font1.render(
                text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
            gameDisplay.blit(font2.render(
                text[1], True, (128, 128, 255)), (200, 100 + 30 * i))



if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(Game.get_size())
    pygame.display.set_caption("MyScreenSaver")
    game = Game()
    game.run()
    exit(0)
