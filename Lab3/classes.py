#Task1
class Converter:
    def __init__(self):
        self.some_string = ""

    def getString(self):
        self.some_string = input("Who's G.O.A.T of rap,bruv?")

    def printString(self):
        print("Answer:", self.some_string.upper())

converter = Converter()
converter.getString()
converter.printString()


#Task2
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        print("Area: 0 ")

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        area = int( self.length) ** 2
        print("Area: ", area)

shape = Shape()
shape.area()

square = Square(input("Enter your lenght:"))
square.area()


#Task3
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        print("Area: 0 ")

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        area = int(self.length) * int(self.width)
        print("Area:", area)


shape = Shape()
shape.area()

length = input("Enter your length: ")
width = input("Enter your width: ")
rectangle = Rectangle(length, width)
rectangle.area()

#Task4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Coordinates: {}, {}".format(self.x, self.y))

    def move(self, updated_x, updated_y):
        self.x = updated_x
        self.y = updated_y

    def dist(self, new_points):
        dx = self.x - new_points.x
        dy = self.y - new_points.y
        abs_distance = math.sqrt(dx**2 + dx**2)
        return round(abs_distance, 3)

point1 = Point(5, 4)
point2 = Point(-2, -6)
point1.show()
point2.move(3, 2)
point2.show()
distance = point1.dist(point2)
print("Distance between point1 and point2:", distance)


#Task5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance 

    def deposit(self, amount):
        self.balance += amount
        print("Commissioned:{}".format(amount))
        print("Your Current balance:{}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdraw denied")
        else:
                self.balance-=amount
                print("Withdraw sum:{} ".format(amount))
                print("Your Current Balance:{}".format(self.balance))

    def get_balance(self):
        return self.balance

owner = input("Enter your name: ")
account = Account(owner)
deposit_amount = float(input("Enter the amount to deposit: "))
account.deposit(deposit_amount)
withdraw_amount = float(input("Enter the amount to withdraw: "))
account.withdraw(withdraw_amount)
balance = account.get_balance()


#Task6
def Save_me(please):
    if int(please) < 2:
        return False
    for x in range(2, please):
        if please % x == 0:
            return False
    return True

please = input("Enter your numbers: ")
please_list = please.split()
prime_nums = list(filter(lambda x: Save_me(int(x)), please_list))
print(*prime_nums)


