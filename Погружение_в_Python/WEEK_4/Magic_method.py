import os
import tempfile

class File(object):

    def __init__(self,sourse):
        self.sourse = sourse
        self.start = 0
        if os.path.exists(sourse) is False:
            with open(sourse, 'w', encoding='utf-8') as f:
                pass

        self.size = sum(1 for line in open(sourse, 'r'))

    def write(self,str):
        with open(self.sourse,"w") as f:
            f.write(str)
        self.size = sum(1 for line in open(self.sourse, 'r'))

    def __add__(self, obj):

        base = File(os.path.join(tempfile.gettempdir(),'storage.data'))
        with open(self.sourse, 'r') as f:
            base_1 = f.read()
        with open(obj.sourse, 'r') as f:
            base_2 = f.read()
        base.write(base_1 + base_2)
        return base


    def __iter__(self):
        return self

    def __next__(self):

        with open(self. sourse, 'r') as f:
            data = f.readlines()

        if self.start >= self.size:
            raise StopIteration

        result = data[self.start]
        self.start += 1
        return result

    def __str__(self):
        return self.sourse
