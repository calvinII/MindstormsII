import threading
from time import sleep


def print_a():
    while True:
        print("a")
        sleep(1)


def print_b():
    while True:
        print("b")
        sleep(0.5)

a = threading.Thread(target=print_a())
b = threading.Thread(target=print_b())
a.setDaemon(True)
b.setDaemon(True)
a.start()
print("a started")
b.start()
while True:
    pass
