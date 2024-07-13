import math

def cylinder_surface_volume(radius, height):
    surface_area = 2 * math.pi * radius**2 + 2 * math.pi * radius * height
    
    volume = math.pi * radius**2 * height
    
    return surface_area, volume
radius = 5
height = 10

surface_area, volume = cylinder_surface_volume(radius, height)
print(f"For a cylinder with radius {radius} and height {height}:")
print(f"Surface Area: {surface_area:.2f} square units")
print(f"Volume: {volume:.2f} cubic units")
