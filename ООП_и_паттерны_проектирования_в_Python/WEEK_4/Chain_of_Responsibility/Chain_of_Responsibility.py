E_INT, E_FLOAT, E_STR = "int", "float", "str"

class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""

class NullHandler:

    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj, event):
        if self.__successor is not None:
            self.__successor.handle(obj, event)

class EventGet:

    def __init__(self, pr ):
        self.kind = {int:E_INT, float:E_FLOAT, str:E_STR}[pr]
        self.pr = None


class EventSet:
    def __init__(self, pr):
        self.kind = {int:E_INT, float:E_FLOAT, str:E_STR}[type(pr)]
        self.pr = pr

class IntHandler(NullHandler):
   def handle(self, obj, event):

        if event.kind == E_INT:
            if event.pr is None:
                return obj.integer_field
            else:
                obj.integer_field = event.pr
        else:
            return super().handle(obj, event)

class FloatHandler(NullHandler):
    def handle(self, obj, event):

        if event.kind == E_FLOAT:
            if event.pr is None:
                return obj.float_field
            else:
                obj.float_field = event.pr
        else:
            return super().handle(obj, event)

class StrHandler(NullHandler):

    def handle(self, obj, event):
        if event.kind == E_STR:
            if event.pr is None:

                return obj.string_field
            else:
                obj.string_field = event.pr
        else:
            return super().handle(obj, event)


obj = SomeObject()
obj.integer_field = 42
obj.float_field = 3.14
obj.string_field = "some text"
chain = IntHandler(FloatHandler(StrHandler(NullHandler)))

print(chain.handle(obj, EventGet(int)))
print(chain.handle(obj, EventGet(float)))
print(chain.handle(obj, EventGet(str)))
chain.handle(obj, EventSet(100))
chain.handle(obj, EventSet(1001.1))
print(chain.handle(obj, EventGet(int)))
print(chain.handle(obj, EventGet(float)))
