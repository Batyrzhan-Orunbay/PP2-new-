#1
# class String:
#     def getstring(self):
#         self.sentence=input("Sentense:")
#     def printstring(self):
#         print("With upper case:"+self.sentence.upper())  
# mystring=String()
# mystring.getstring()
# mystring.printstring()


# #2
# class Shape():
#     def area(self):
#         return 0
# class Square(Shape):
#     def __init__(self,length):
#         self.length=length
#     def area(self):
#         return self.length ** 2
# a = float(input("a:"))
# mysquare=Square(a)
# print("sharshy audany:",mysquare.area())
# myshape=Shape()
# print("Basqa:",myshape.area())


# #3
# class Shape:
#     def area(self):
#         return 0
# class Rectangle():
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width
# length = float(input("Length: "))
# width = float(input("Width: "))
# audan=Rectangle(length,width)
# print("Area of the rectangle:",audan.area())


# #4
# import math

# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def show(self):
#         print(f"Coordinates: ({self.x}, {self.y})")

#     def move(self, x1, y1):
#         self.x = x1
#         self.y = y1

#     def dist(self, point2):
#         dx = self.x - point2.x
#         dy = self.y - point2.y
#         distance = math.sqrt(dx**2 + dy**2)
#         return distance
# a=float(input("x:"))
# b=float(input("y:"))
# point1 = Point(a,b)
# point2 = Point(a,b)

# point1.show() 
# k=float(input("x1:"))
# p=float(input("y1:"))
# point1.move(k,p)
# point1.show() 

# distance = point1.dist(point2)
# print(f"Distance between point1 and point2: {distance}")


#5
class Bank():
    def __init__(self, account, money):
        self.money = money
        self.account = account

    def balance(self):
        return self.money
    
    def owner(self):
        return self.account
    
    def deposit(self, money):
        self.money+=money

        return f"You are deposit {money} money"
    
    def withdraw(self, money):
        if self.money - money < 0:
            return "insufficient funds"
        else:
            self.money-=money

            return f"you're balance: {self.money},  and you take {money}"
        
        
bank = Bank("Batyrzhan", 1000)

print(bank.balance())

print(bank.owner())

print(bank.deposit(1000))

print(bank.withdraw(3000))

print(bank.withdraw(2000))


#6
class Prime:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def filter_prime_numbers(self):
        return list(filter(lambda x: self.is_prime(x), self.numbers))

n = int(input("n: "))
mylist = []
for i in range(n):
    number = int(input("number: "))
    mylist.append(number)

prime_filter = Prime(mylist)
print(prime_filter.filter_prime_numbers())