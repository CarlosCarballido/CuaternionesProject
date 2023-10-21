# import class quaternions from quaternions.py
from quaternions import Quaternions

if __name__ == "__main__":
    quater = Quaternions(0.5, 0.33, 0.77, 0.67)
    print(quater)
    X, Y, Z = quater.to_euler_angles()
    print("Roll:", X)
    print("Roll:", Y)
    print("Roll:", Z)