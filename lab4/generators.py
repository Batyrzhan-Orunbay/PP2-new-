#1
def square_generator(N):
    for i in range(N + 1):
        yield i ** 2
N = 10
for square in square_generator(N):
    print(square)

#2
def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i
n = int(input("Enter a number: "))
print(",".join(str(num) for num in even_generator(n)))

#3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input("Enter a number: "))
for num in divisible_by_3_and_4(n):
    print(num)
    
#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
a, b = 2, 5
for square in squares(a, b):
    print(square)

#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
n = 10
for num in countdown(n):
    print(num)
