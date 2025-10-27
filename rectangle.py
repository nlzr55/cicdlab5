def area(a, b):
    a = float(a)
    b = float(b)
    if a < 0 or b < 0:
        raise ValueError("Стороны должны быть неотрицательными")
    return a * b


def perimeter(a, b):
    a = float(a)
    b = float(b)
    if a < 0 or b < 0:
        raise ValueError("Стороны должны быть неотрицательными")
    return 2 * (a + b)
