def area(num1, num2, num3):
    semi = 1/2 * (num1 + num2 + num3)
    triangle = (semi * (semi - num1) * (semi - num2) * (semi - num3)) ** 0.5

    return triangle

print(area(3, 4, 5))
