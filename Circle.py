#Get the circumference of a circle and return its area
import math
import os
from time import sleep

circumference = float(input("Enter the circumference of the circle: "))
pi = math.pi

r = circumference / 2 / pi

area = math.pow(r, 2) * pi

print(f"The area of the circle is:{area}")

sleep(5)
os.system('cls')

#Get the area of a circle and return its circumference
area = float(input("Enter the area of the circle: "))
pi = math.pi

r = area / pi
r = math.sqrt(r)

circumference = 2 * pi * r

print(f"The circumference of the circle is:{circumference}")