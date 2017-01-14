from threading import Thread
from time import sleep


class myClassA(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        while True:
            print('A')
            sleep(1)

class myClassB(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            print('B')
            sleep(0.5)


myClassA()
myClassB()
while True:
    pass