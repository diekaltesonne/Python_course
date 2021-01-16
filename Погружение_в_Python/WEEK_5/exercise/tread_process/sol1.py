import time
import os

pid = os.fork()
if pid == 0:
    #дочерний процесс
    while True:
        print("child", os.getpid())
        time.sleep(5)
    else:
        # родительский процесс
        print("parent", os.getpid())
        os.wait()

# системный вызов fork()
# создает точную копию родительского процесса
# после отработки два процесса
