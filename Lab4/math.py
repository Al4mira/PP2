#EX1
import math

def degree_converter():
    x = int(input("Enter your degree: "))
    result = math.radians(x)
    print("Degree in Radians:",result)

degree_converter()


#EX2
def trapezoid_area():
    h = int(input("Enter your height: "))
    a = int(input("Enter first base: "))
    b = int(input("Enter second base: "))
    Area = ((a+b)/2)*h
    print("Your Area: ", Area)

trapezoid_area()


#Ex3
import math

def polygon_area():
    sides = int(input("Enter your sides amount: "))
    lenght = int(input("Enter your side lenght: "))
    Apothem = (lenght/2) * math.tan(math.pi / sides )
    Area = (sides * lenght * Apothem)/2
    print("Your area: ", round(Area))

polygon_area()

#Ex4
import math

def parallelogram_area():
    height = int(input("Enter your height: "))
    base = int(input("Enter your base: "))
    Area = height * base
    print("Your area: ", round(Area))

parallelogram_area()
