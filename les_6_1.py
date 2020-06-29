import time


class TrafficLight:
    def __init__(self):
        self.__color = ["red", "yellow", "green"]

    def running(self):
        while True:
            print("\033[31m {}" .format(self.__color[0]))
            time.sleep(7)
            print("\033[33m {}" .format(self.__color[1]))
            time.sleep(2)
            print("\033[32m {}" .format(self.__color[2]))
            time.sleep(7)
            print("\033[33m {}" .format(self.__color[1]))
            time.sleep(2)


a = TrafficLight()
a.running()
