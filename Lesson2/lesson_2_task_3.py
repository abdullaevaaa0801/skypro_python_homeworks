def square(side):
    if not isinstance(side, int):
        return int(side ** 2 + 0.99)
    else:
        return side ** 2
print(square(3))
print(square(3.2))