import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("Error: a cannot be zero. This is not a quadratic equation.")
else:
    delta = b**2 - 4 * a * c
    if delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Two distinct real roots exist:")
        print(f"Root 1: {root1}")
        print(f"Root 2: {root2}")
    elif delta == 0:
        root = -b / (2 * a)
        print("One real root (repeated) exists:")
        print(f"Root: {root}")
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-delta) / (2 * a)
        print("Two complex roots exist:")
        print(f"Root 1: {real_part} + {imaginary_part}i")
        print(f"Root 2: {real_part} - {imaginary_part}i")