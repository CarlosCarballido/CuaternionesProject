import math


class Quaternions:
    def __init__(self, w, x, y, z):
        self.__w = w
        self.__x = x
        self.__y = y
        self.__z = z

    @property
    def w(self):
        return self.__w

    @w.setter
    def w(self, value):
        self.__w = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, value):
        self.__z = value

    @property
    def __str__(self) -> str:
        print("\tQuaternion coefficients:\nW: " + self.w +
              "\nX: " + self.x + "\nY: " + self.y + "\nZ: " + self.z)


