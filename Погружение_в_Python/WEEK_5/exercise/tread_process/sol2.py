from multiprocessing import Process
def f(name):
    print("hello", name)

p = Process(target = f, args =("Bob,"))
p.start()
p.join()
#another method

class PrintProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        print("hello", self.name)

p1 = PrintProcess("Mike")
p.start()
p.join()
