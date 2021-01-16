import time

class First(object):
    """docstring for First."""
    def __init__(self, arg):
        super(First, self).__init__()
        self.arg = arg

    def __getitem__(self,key):
        if self[key]:
            print("Right")
        else:
            print("Hey")


    def __setitem__(self,value,key):
        self[key] = value

class PascalList:
    def __init__(self,original_list = None):
        self.container = original_list or []

    def __getitem__(self, index):
        return self.container[index - 1]

    def __setitem__(self,index,value):
        self.container[index - 1] = value

    def __str__(self):
        return self.container.__str__()

# итератор метод _1
class SquareIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result

# итератор метод _2
class IndexIterable:

    def __init__(self,obj):
        self.obj = obj

    def __getitem__(self,index):
        return self.obj[index]

class open_file:
    def __init__(self, filename, mode):
        self.f = open(filename,mode)

    def __enter__(self):
        return self.f

    def __exit__():
        self.f.close()


class suppress_exception:
    """docstring for suppress_exception."""
    def __init__(self, exc_type):
        self.exc_type = exc_type

    def __enter__(self):
        return

    def __exit__(self,exc_type,exc_value, traceback):
        if exv_type == self.exc_type:
            print("Nothing happend")
            return True



class Timecheck():
    def __init__(self):
        self.clock = time.time()
    def __enter__(self):
        pass
    def __exit__(self, *args):
        print((time.time() - self.clock, "seconds"))

with Timecheck():
    print([i for i in range(0,100)])
