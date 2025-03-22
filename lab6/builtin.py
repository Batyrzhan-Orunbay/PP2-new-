#1
def multiplyList(a):
    res = 1
    for i in a:
        res*=i
    return res
lst = list(map(int, input().split()))
print(multiplyList(lst))


#2
def uplownum(s):
    up = 0
    low = 0
    for i in s:
        if ord(i) > 96:   # ord(i) возвращает ASCII-код символа i.
            low+=1
        else:
            up += 1
    return up,low
s = str(input("Word: "))
print(uplownum(s))


#3
def isPolindrom(s):
    return s == s[::-1]
print(isPolindrom("madam"))


#4
import time
def squar(n, t):
    time.sleep(t/1000)
    return n**0.5
print(squar(25100, 2123))


#5
def allTrue(t):
    return all(t)
print(allTrue((1,1,5.5)))


