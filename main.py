# This module is used to do mathematical operations (pass to dregrees, tan, sen, cos, etc).
import math

# This class is used to create a quaternion object.
class Quaternions:
    def __init__(self, w:float, x:float, y:float, z:float):
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
        return "\tQuaternion coefficients:\nW: " + str(self.w) + "\nX: " + str(self.x) + "\nY: " + str(self.y) + "\nZ: " + str(self.z)

    # This method is used to convert a quaternion to euler angles.
    def to_euler_angles(self) -> tuple[float, float, float]:
        t0 = +2.0 * (self.w * self.x + self.y * self.z)
        t1 = +1.0 - 2.0 * (self.x * self.x + self.y * self.y)
        X = math.degrees(math.atan2(t0, t1))

        t2 = +2.0 * (self.w * self.y - self.z * self.x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        Y = math.degrees(math.asin(t2))

        t3 = +2.0 * (self.w * self.z + self.x * self.y)
        t4 = +1.0 - 2.0 * (self.y * self.y + self.z * self.z)
        Z = math.degrees(math.atan2(t3, t4))

        return X, Y, Z


q = Quaternions(0.5, 0.33, 0.77, 0.67)
X, Y, Z = q.to_euler_angles()
print("Roll:", X)
print("Roll:", Y)
print("Roll:", Z)