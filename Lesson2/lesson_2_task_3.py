import math as m
def square(side):
    side=22.4
    area=side**2
    if side == int:
        return area
    else:
        return m.ceil(side**2)
print("Площадь квадрата:",square("area"))