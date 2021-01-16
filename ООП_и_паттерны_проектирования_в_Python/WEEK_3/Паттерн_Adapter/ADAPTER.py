
from abc import ABC, abstractmethod
class Light:

    def __init__(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
        self.lights = []
        self.obstacles = []

    def set_dim(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]

    def set_lights(self, lights):
        self.lights = lights
        self.generate_lights()

    def set_obstacles(self, obstacles):
        self.obstacles = obstacles
        self.generate_lights()

    def generate_lights(self):
        return self.grid.copy()



'''
Класс Light создает в методе __init__ поле заданного размера.
-- координата по высоте соответственно.….
'''
class MappingAdapter:

    def __init__(self,adaptee):
        self.adaptee = adaptee

    def lighten(self,map):
        dim = (len(map[0]),len(map))
        lights = []
        obstacles =[]

        #За размер поля отвечает параметр, представляющий из себя кортеж из 2 чисел.
        #Элемент dim[1] отвечает за высоту карты, dim[0] за ее ширину


        # Положение элементов задается списком кортежей.
        # В каждом элементе кортежа хранятся 2 значения:
        # elem[0] -- координата по ширине карты и elem[1]

        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == 1:
                    lights.append((j,i))
                if map[i][j] == -1:
                    obstacles.append((j,i))

        self.adaptee.set_dim(dim)
        self.adaptee.set_lights(lights)
        self.adaptee.set_obstacles(obstacles)
        return self.adaptee.generate_lights()


class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(30)] for _ in range(20)]
        self.map[5][7] = 1 # Источники света
        self.map[5][2] = -1 # Стены

    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten(self.map)

sys = System()
sys.get_lightening(MappingAdapter(Light((5,5))))
