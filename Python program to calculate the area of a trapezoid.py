def trapezoid_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area
base1 = 5
base2 = 7
height = 4

area = trapezoid_area(base1, base2, height)
print(f"The area of the trapezoid with bases {base1} and {base2} and height {height} is: {area}")
