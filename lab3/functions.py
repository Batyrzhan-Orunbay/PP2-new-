#1
def grams_to_ounces(grams):
    return 28.3495231 * grams
print(grams_to_ounces(100))


#2
def fahrenheit_to_centigrade(F):
    return (5 / 9) * (F - 32)
print(fahrenheit_to_centigrade(98))


#3
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return "No answer"
print(solve(35, 94))


#4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]
print(filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


#5
from itertools import permutations
def get_permutations(s):
    all_permutations = permutations(s)
    return ["".join(a) for a in all_permutations]
user_input = input("word: ")
result = get_permutations(user_input)
for perm in result:
    print(perm)
    
    
#6
def reverse(sentence):
    words = sentence.split()
    reversed_sentence = " ".join(reversed(words))
    return reversed_sentence
user_input = input("Sentence: ")
print(reverse(user_input))


#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))     
print(has_33([1, 3, 1, 3]))    
print(has_33([3, 1, 3]))       
print(has_33([3, 3, 1]))       


#8
def contains_007(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False
print(contains_007([1, 2, 0, 0, 7, 5])) 
print(contains_007([1, 0, 0, 8, 7]))     
print(contains_007([0, 0, 7]))           
print(contains_007([7, 0, 0]))           


#9
import math
def area(r):
    return 4/3 *math.pi * r**3
r=int(input())
print(area(r))


#10
def uniquelist(arr):
    arr.sort()
    unique_arr=[]
    for i in arr:
        if i not in unique_arr:
            unique_arr.append(i)
    print(*unique_arr)
    return unique_arr
uniquelist([1, 4, 5, 2, 5, 3, 1, 5, 8, 5, 3, 4, 5, 1, 7])


#11
def is_polindrom(s):
    revs = s[::-1]
    if revs == s:
        return True
    return False
r=str(input())
print(is_polindrom(r))


#12
def histogram(length):
    for i in length:
        print('*' * i)
histogram([4, 9, 7])


#13
import random
def guess_num():
    n = random.randint(1,21)
    print("Hello! What is your name?")
    name = input("")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.")
    g = int(input())
    while g != n:
        if g < n:
            print("\nYour guess is too low.\nTake a guess.")
        else:
            print("\nYour guess is too low.\nTake a guess.")
        g = int(input())
    print(f"Good job, KBTU! You guessed my number in {n} guesses!")

