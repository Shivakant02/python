# return area and circumference of the circle in one function

import math

def circle_stats(radius):
   return math.pi*radius**2,2*math.pi*radius


area,circum=circle_stats(3)

print(f'area: {area:0,.2f}, circme: {circum:0,.2f}')