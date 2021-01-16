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
