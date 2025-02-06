import threading

from raton import *

if __name__ == '__main__':

    eve = threading.Event()
    eve.set()
    for i in range(1,15):

        e = Raton(i,eve)
        e.start()